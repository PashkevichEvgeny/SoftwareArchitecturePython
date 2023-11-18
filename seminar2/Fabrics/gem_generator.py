from seminar2.Fabrics.item_fabric import ItemFabric
from seminar2.Products.gem import Gem


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()
