from seminar2.Factory.item_factory_param import ItemFactoryParam
from seminar2.Products.items import Bone, Coal, Glass, Stone, Wood, Gold, Silver, Gem


class ItemGeneratorParam(ItemFactoryParam):

    def create_item(self, name):
        item_dict = {'Bone': Bone(), 'Coal': Coal(), 'Gem': Gem(), 'Glass': Glass(),
                     'Gold': Gold(), 'Silver': Silver(), 'Stone': Stone(), 'Wood': Wood()}
        return item_dict[name]
