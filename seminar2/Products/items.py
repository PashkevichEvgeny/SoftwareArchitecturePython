from seminar2.Products.game_item import GameItem


class Bone(GameItem):
    def look(self):
        print('Bone', end=' ')


class Coal(GameItem):
    def look(self):
        print('Coal', end=' ')


class Gem(GameItem):
    def look(self):
        print('Gem!', end=' ')


class Glass(GameItem):
    def look(self):
        print('Glass', end=' ')


class Gold(GameItem):
    def look(self):
        print('Gold!', end=' ')


class Silver(GameItem):
    def look(self):
        print('Silver!', end=' ')


class Stone(GameItem):
    def look(self):
        print('Stone', end=' ')


class Wood(GameItem):
    def look(self):
        print('Wood', end=' ')


