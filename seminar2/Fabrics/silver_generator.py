from seminar2.Fabrics.item_fabric import ItemFabric
from seminar2.Products.silver import Silver


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()
