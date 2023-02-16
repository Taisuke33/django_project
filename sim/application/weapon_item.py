class Weapon_Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': □' + str(self.price)
