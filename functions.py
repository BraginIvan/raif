from estates import RealEstate
import numpy as np
from functools import partial


def get_price_general(target_estate: RealEstate,
                neighbor_estate: RealEstate,
                distance: float,
                max_distance = 10,
                reform_mean_year_building_1000_coeff = 0,
                total_square_coeff = 0,
                multiply_square = False):
    if distance > max_distance:
        return 0
    square_frac = neighbor_estate.row["total_square"] / target_estate.row["total_square"]
    if square_frac > 3 or square_frac < 0.33:
        return 0

    coeff = 1
    reform_mean_year_building_1000 = 1 + (reform_mean_year_building_1000_coeff * (target_estate.row["reform_mean_year_building_1000"] - neighbor_estate.row["reform_mean_year_building_1000"]) / 1000)
    reform_mean_year_building_1000 = np.clip(reform_mean_year_building_1000, 0.95, 1.05)
    coeff *= reform_mean_year_building_1000
    total_square = 1 + (total_square_coeff * ( neighbor_estate.row["total_square"] - target_estate.row["total_square"]) / 100)
    coeff *= total_square
    result =  neighbor_estate.row["per_square_meter_price"]*coeff
    if multiply_square:
        result *= neighbor_estate.row["total_square"]
    # print("coeff", coeff)

    return result

def get_square_general(target_estate: RealEstate,
                neighbor_estate: RealEstate,
                distance: float,
                max_distance = 10,
                diff = False,
                frac=False
                ):
    if distance > max_distance:
        return 0

    if diff:
        result = neighbor_estate.row["total_square"] - target_estate.row["total_square"]
    elif frac:
        result = neighbor_estate.row["total_square"] / target_estate.row["total_square"]
    else:
        result = neighbor_estate.row["total_square"]

    return result


def get_catering_points_general(target_estate: RealEstate,
                neighbor_estate: RealEstate,
                distance: float,
                max_distance = 10,
                ):
    if distance > max_distance:
        return 0


    result = neighbor_estate.row["osm_catering_points_in_0.005"]

    return result



functions = {
    "F_simple_price": get_price_general,
    "F_catering_points_general": get_catering_points_general
}


f = partial(get_price_general, reform_mean_year_building_1000_coeff = 5)
functions["F_reform_mean_year_building_1000_" + str(5)] = f

f = partial(get_price_general, total_square_coeff = 9)
functions["F_total_square_" + str(9)] = f

f = partial(get_price_general, multiply_square = True)
functions["F_total_price"] = f

f = partial(get_price_general, max_distance=2/5)
functions["F_max_distance_" + str(2)] = f

for i in [True, False]:
    f = partial(get_square_general, diff=i)
    functions["F_square_" + str(i)] = f

for i in [True, False]:
    f = partial(get_square_general, frac=i)
    functions["F_square_frac_" + str(i)] = f