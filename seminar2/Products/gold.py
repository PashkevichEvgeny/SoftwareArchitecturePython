from seminar2.Products.game_item import GameItem


class Gold(GameItem):
    def open(self):
        print('Gold!', end=' ')
