from seminar2.Factory.item_factory import ItemFactory
from seminar2.Products.items import Wood, Stone, Glass, Coal, Bone, Silver, Gold, Gem


class BoneGenerator(ItemFactory):
    def create_item(self):
        return Bone()


class CoalGenerator(ItemFactory):
    def create_item(self):
        return Coal()


class GemGenerator(ItemFactory):
    def create_item(self):
        return Gem()


class GoldGenerator(ItemFactory):
    def create_item(self):
        return Gold()


class GlassGenerator(ItemFactory):
    def create_item(self):
        return Glass()


class SilverGenerator(ItemFactory):
    def create_item(self):
        return Silver()


class StoneGenerator(ItemFactory):
    def create_item(self):
        return Stone()


class WoodGenerator(ItemFactory):
    def create_item(self):
        return Wood()
