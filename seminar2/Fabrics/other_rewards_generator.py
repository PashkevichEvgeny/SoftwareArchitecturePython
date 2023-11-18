from seminar2.Fabrics.item_fabric import ItemFabric
from seminar2.Products.other_rewards import Wood, Stone, Glass, Coal, Bone


class BoneGenerator(ItemFabric):
    def create_item(self):
        return Bone()


class CoalGenerator(ItemFabric):
    def create_item(self):
        return Coal()


class GlassGenerator(ItemFabric):
    def create_item(self):
        return Glass()


class StoneGenerator(ItemFabric):
    def create_item(self):
        return Stone()


class WoodGenerator(ItemFabric):
    def create_item(self):
        return Wood()
