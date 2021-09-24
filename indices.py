import pandas as pd
import rtree.index

from estates import create_estate


class MainDataset:
    def __init__(self, path, is_train = True):
        dataset = pd.read_csv(path,
                                   # nrows=1000
                                   )
        dataset["day"] = pd.to_datetime(dataset.date).dt.dayofyear
        if is_train:
            self.dataset = dataset[(dataset['per_square_meter_price'] > 10000) | (dataset['price_type'] == 1)].reset_index()
            self.train_dataset = self.dataset[self.dataset.day < 175]
            self.val_dataset = self.dataset[self.dataset.day >= 175]

            self.all_train_objects = [create_estate(index, row) for index, row in self.train_dataset.iterrows()]
            self.all_val_objects = [create_estate(index, row) for index, row in self.val_dataset.iterrows()]

            self.index = rtree.index.Rtree()
            for i, o in enumerate(self.all_train_objects):
                if o.row["price_type"] == 0:
                    self.index.insert(o.index, o.bounds, obj=o)

            self.index1 = rtree.index.Rtree()
            for i, o in enumerate(self.all_train_objects):
                if o.row["price_type"] == 1:
                    self.index1.insert(o.index, o.bounds, obj=o)



