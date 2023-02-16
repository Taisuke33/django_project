from weapon_item import Weapon_Item

class Armor(Weapon_Item):
    def __init__(self, name, price):
        super().__init__(name, price)