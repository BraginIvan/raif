from sklearn.metrics.pairwise import haversine_distances
from indices import MainDataset

class Neighborhoods2:
    def __init__(self, train_dataset: MainDataset):
        self.index = train_dataset.index

    # todo: don't extract different count all times
    def get_deckard_closest(self, estate, count):
        return list(self.index.nearest(estate.bounds, count))[1:]

    def get_haversine_closest(self, estate, count):
        distances = []
        deckard_closests = self.get_deckard_closest(estate, count)
        for deckard_closest in deckard_closests:
            d = haversine_distances([[deckard_closest.rad_lat, deckard_closest.rad_lon], [estate.rad_lat, estate.rad_lon]])[0][1] * 6371
            distances.append(d)
        return sorted(zip(deckard_closests, distances), key= lambda x: x[1])



