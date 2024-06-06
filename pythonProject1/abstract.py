from abc import abstractmethod
from abc import ABCMeta
class Character(metaclass=ABCMeta):
    count = 0
    def __init__(self, name, level, health, damage):
        self.__name = name
        self.__level = level
        self.__health = health
        self.__damage = damage
        self.temp = 1

    @abstractmethod
    def attack(self, character):
        pass

    @staticmethod
    def reg_damage():
        Character.count += 1
    @staticmethod
    def get_reg_damage():
        return Character.count

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_health(self):
        return self.__health

    def get_damage(self):
        return self.__damage

    def take_damage(self,new_damage):
        Character.reg_damage()
        self.__health -= new_damage
        print(f"{self.__name} takes damage {new_damage}")

        if self.__health <= 0:
            self.death ()

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        if(value < 0):
            self.__damage = 0
        else:
            self.__damage = value

    def new_level(self, new_level):
         self.__level += new_level
         print(f"{self.__name} now has reached level {new_level} ")

    def new_health(self, new_health):
        self.__health = new_health
        print(f"{self.__name} now has {new_health} Health left")

    def death(self):
        print(f"{self.__name} has died")

class Warrior(Character):
    def __init__(self, name, level, health, damage):
        super().__init__(name, level, health, damage)

    def attack(self, character):
        print(f"The warrior {self.get_name()} throws a sword attack to {character.get_name()}.")
        character.take_damage(self.get_damage())
class Mage(Character):
    def __init__(self, name, level, health, damage):
        super().__init__(name, level, health, damage)

    def attack(self, character):
        print(f"The mage {self.get_name()} throws a spell attack to {character.get_name()}.")
        character.take_damage(self.get_damage())
class Ranger(Character):
    def __init__(self, name, level, health, damage):
        super().__init__(name, level, health, damage)

    def attack(self, character):
        print(f"The ranger {self.get_name()} shoots an arrow at {character.get_name()}.")
        character.take_damage(self.get_damage())

warrior1 = Warrior('Vegeta', 1, 100, 30)
mage1 = Mage("Lord", 2, 100, 100)
ranger1 = Ranger("Conan", 1, 100, 25)

warrior1.attack(mage1)
mage1.attack(warrior1)
ranger1.attack(mage1)
warrior1.damage = -5
print(warrior1.damage)

print(Character.get_reg_damage())
print(Ranger.get_reg_damage())
#ch = Character('Vegeta', 1, 100, 30)