

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

    def attack(self, secondcharacter):
        print(f"{self.__name} attacks {secondcharacter.get_name()})

        # metodo de atacar un personaje
        #recibir daño de personaje
        # subir de nivel

   # definir life
   #definir new life

   #define new level
   # degine new health
 # define attack
 #define death

def health_change(self,new_health):
    self.__health = new_health

def take_damage(self,new_damage):
    self.__damage = new_damage

def new_level(self, new_level)
    self.__level += new_level

def death(self):
    print(f"{self.__name} has died")

class Warrior(Character):
    def __init__(self, sword):
        self.__sword = sword
    def sword_attack(self,secondcharacter):
    print(f" The warrior {get_name()} throws a sword attack to {secondcharacter.get_name()}.")
    secondcharacter.take_damage(self.get_damage())

class Mage(Character):
    def __init__(self, cast):
        self.__cast = cast
    def cast_spell(self):


class range(character):
    def __init__(self,arrow):
        self.__arrow = arrow
    def attackwith_arrow(self):

warrior1 = Warrior('Vegeta', 1, 100, 30)
mage1 = Mage("Lord", 2, 100, 25)
Ranger1 = range("conan", 1, 100, 20)




