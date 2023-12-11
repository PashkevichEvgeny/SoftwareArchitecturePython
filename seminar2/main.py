from random import randint, choices

from seminar2.Factory.abstract_generator import BigGoldGenerator, SmallGoldGenerator
from seminar2.Factory.item_generator_param import ItemGeneratorParam
from seminar2.Factory.item_generator import CoalGenerator, GlassGenerator, \
    StoneGenerator, WoodGenerator, BoneGenerator, SilverGenerator, GemGenerator, GoldGenerator


def chance(list_items, list_chances):
    """
    Собственная реализация метода
    :type list_chances: list
    :type list_items: list
    """
    if len(list_chances) != len(list_items):
        raise Exception("Списки не равны по длине")
    elif not list_chances:
        raise Exception("Списки пусты")

    lst = []

    for i, c in zip(list_items, list_chances):
        for _ in range(c):
            lst.append(i)

    return lst


def what_in_box(box):
    i = iter(box)
    next(i).create_box().open()
    next(i).create_item().look()


if __name__ == '__main__':

    print('Фабричный метод')
    items = [BoneGenerator(), CoalGenerator(), GlassGenerator(), StoneGenerator(),
             WoodGenerator(), SilverGenerator(), GemGenerator(), GoldGenerator()]
    chances = [10, 10, 10, 10, 10, 5, 3, 1]
    generators = chance(items, chances)
    boxes = [generators[randint(0, len(generators)) - 1].create_item() for _ in range(10)]
    [box.look() for box in boxes]

    print("\n\nПараметризированный фабричный метод")
    names = ['Bone', 'Coal', 'Glass', 'Stone', 'Wood', 'Gem', 'Silver', 'Gold']
    chances = [10, 10, 10, 10, 10, 3, 2, 1]
    boxes = [ItemGeneratorParam().create_item(i) for i in choices(names, weights=chances, k=10)]
    [box.look() for box in boxes]

    print()
    box = BigGoldGenerator().create()
    what_in_box(box)
    box = SmallGoldGenerator().create()
    what_in_box(box)
