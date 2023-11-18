from seminar2.Fabrics.item_fabric import ItemFabric
from seminar2.Products.gold import Gold


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()
