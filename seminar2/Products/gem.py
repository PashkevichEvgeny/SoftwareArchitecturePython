from seminar2.Products.game_item import GameItem


class Gem(GameItem):
    def open(self):
        print('Gem!', end=' ')