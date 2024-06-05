

class Character:
    def __init__(self, name, level, health, damage):
        self.__name = name
        self.__level = level
        self.__health = health
        self.__damage = damage
    def get_name(self):
        return self.__name
    def get_level(self):
        return self.__level
    def get_health(self):
        return self.__health
    def get_damage(self):
        return self.__damage





    def take_damage(self,new_damage):
        self.__health -= new_damage
        print(f"{self.__name} takes damage {new_damage}")

        if self.__health <= 0:
            self.death ()

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
        Character.__init__(self, name, level, health, damage)


    def sword_attack(self,second_character):
        print(f"The warrior {self.get_name()} throws a sword attack to {second_character.get_name()}.")
        second_character.take_damage(self.get_damage()* 2)

        #lvel missing

        print(f"{self.get_name()} just reached this new level {self.get_level()+1}")

        #print(f"{self.get_name()} just reached this new level {self.new_level(2)}")

        second_character.new_health(second_character.get_health())

        #second_character.get_health(self.get_damage() *2 )  #neww


class Mage(Character):
    def __init__(self, name, level, health, damage):
        Character.__init__(self, name, level, health, damage)

    def cast_spell(self, second_character):
        print(f"The mage {self.get_name()} throws a spell attack to {second_character.get_name()}.")
        second_character.take_damage(self.get_damage())
        second_character.new_health(second_character.get_health())
        print(f"{self.get_name()} just reached this new level {self.get_level()+1}")

class Ranger(Character):
    def __init__(self, name, level, health, damage):
        Character.__init__(self, name, level, health, damage)

    def attackwith_arrow(self, second_character):
        print(f"The ranger {self.get_name()} shoots an arrow at {second_character.get_name()}.")
        second_character.take_damage(self.get_damage())
        second_character.new_health(second_character.get_health())
        self.new_level(1)


warrior1 = Warrior('Vegeta', 1, 100, 30)
mage1 = Mage("Lord", 2, 100, 100)
ranger1 = Ranger("Conan", 1, 100, 25)


warrior1.sword_attack(mage1)
mage1.cast_spell(warrior1)
ranger1.attackwith_arrow(mage1)





