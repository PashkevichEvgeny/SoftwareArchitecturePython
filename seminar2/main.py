from random import randint, choices

from seminar2.Fabrics.gem_generator import GemGenerator
from seminar2.Fabrics.gold_generator import GoldGenerator
from seminar2.Fabrics.silver_generator import SilverGenerator
from seminar2.Fabrics.other_rewards_generator import CoalGenerator, GlassGenerator, \
    StoneGenerator, WoodGenerator, BoneGenerator


def chance(list_chances, list_items):
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

    for p, g in zip(list_chances, list_items):
        for _ in range(p):
            lst.append(g())

    return lst


if __name__ == '__main__':
    chances = [10, 10, 10, 10, 10, 10, 3, 1]
    items = [BoneGenerator, CoalGenerator, GlassGenerator, StoneGenerator,
             WoodGenerator, SilverGenerator, GemGenerator, GoldGenerator]

    generators = chance(chances, items)

    [generators[randint(0, len(generators)) - 1].create_item().open() for _ in range(10)]

    print()

    # встроенный метод из библиотеки random
    [i().create_item().open() for i in choices(items, weights=chances, k=10)]
