import pandas as pd
import rtree.index

from estates import create_estate


class MainDataset:
    def __init__(self, path, need_index = True):
        self.dataset = pd.read_csv(path,
                                   # nrows=1000
                                   )
        if need_index:
            self.dataset = self.dataset[(self.dataset['per_square_meter_price'] > 10000) | (self.dataset['price_type'] == 1)].reset_index()
        self.all_objects = [create_estate(index, row) for index, row in self.dataset.iterrows()]
        if need_index:
            self.index = rtree.index.Rtree()
            for i, o in enumerate(self.all_objects):
                if o.row["price_type"] == 0:
                    self.index.insert(o.index, o.bounds, obj=o)

            self.index1 = rtree.index.Rtree()
            for i, o in enumerate(self.all_objects):
                if o.row["price_type"] == 1:
                    self.index1.insert(o.index, o.bounds, obj=o)





