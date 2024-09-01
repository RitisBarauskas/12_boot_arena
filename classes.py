class BaseObject:
    """Базовый класс всех объектов"""
    def __init__(self, name, hp, attack, protection):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.protection = protection


class Thing(BaseObject):
    """Класс вещей"""
    pass


class Person(BaseObject):
    """Класс обычного персонажа"""
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp, attack, protection)
        self.things = []

    def set_things(self, things):
        if len(things) <= 4:
            for thing in things:
                self.hp += thing.hp
                self.attack += thing.attack
                self.protection = round(self.protection + thing.protection, 2)
                self.things.append(thing)
        else:
            print('Игрок может держать при себе не более 4 вещей.')

    def get_damage(self, attack_damage):
        self.hp -= round(
            (attack_damage - (attack_damage * self.protection))
        )

    def __str__(self):
        return self.name


class Paladin(Person):
    """Класс паладина"""
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp*2, attack, protection*2)


class Warrior(Person):
    """Класс воителя"""
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp, attack*2, protection)