from math import radians

from shapely.geometry import Point


class RealEstate:
    def __init__(self,
                 index: int,
                 id_: str,
                 price_type: int,
                 floor: int,
                 row,
                 lat: float,
                 lon: float,
                 ):
        self.price_type = price_type
        self.floor = floor
        self.lat = lat
        self.lon = lon
        self.index = index
        self.id_ = id_
        self.row = row
        self.neighbors_scores = {}


    @property
    def rad_lat(self):
        return radians(self.lat)

    @property
    def rad_lon(self):
        return radians(self.lon)

    @property
    def point(self):
        return Point(self.lon, self.lat)

    @property
    def bounds(self):
        return self.point.bounds

    def getX(self):
        x = []
        for _, score in self.neighbors_scores.items():
            x.append(score)
        x.append(self.lat)
        x.append(self.lon)
        return x

    def getY(self):
        return self.row["per_square_meter_price"]

def create_estate(index, row):
    return RealEstate(
        index=index,
        id_=row["id"],
        price_type=row["price_type"],
        floor=row["floor"],
        row=row,
        lat=row["lat"],
        lon=row["lng"]
    )
