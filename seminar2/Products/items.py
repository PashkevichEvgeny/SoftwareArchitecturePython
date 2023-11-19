from seminar2.Products.game_item import GameItem


class Bone(GameItem):
    def open(self):
        print('Bone', end=' ')


class Coal(GameItem):
    def open(self):
        print('Coal', end=' ')


class Gem(GameItem):
    def open(self):
        print('Gem!', end=' ')


class Glass(GameItem):
    def open(self):
        print('Glass', end=' ')


class Gold(GameItem):
    def open(self):
        print('Gold!', end=' ')


class Silver(GameItem):
    def open(self):
        print('Silver!', end=' ')


class Stone(GameItem):
    def open(self):
        print('Stone', end=' ')


class Wood(GameItem):
    def open(self):
        print('Wood', end=' ')


