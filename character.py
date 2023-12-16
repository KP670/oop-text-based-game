from random import choice
from weapon import *

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health

    

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
    
    def equip(self, weapons):
    
    def drop():
        

    def attack(self, target) -> None:
        weapon = choice(self.weapons)
        print(f"{self.name} has chosen {weapon.name}!")

        damage = choice(weapon.damage)
        target.health -= damage
        target.health = max(target.health, 0)

        print(f"{target.name} has been inflicted with -{damage}HP, leaving {target.name} with {target.health}HP!")


class Enemy(Character):
    def __init__(self, name: str, health: int, weapons: list) -> None:


        super().__init__(name=name, health=health)
        self.weapons = weapons

    def attack(self, target) -> None:
        weapon = choice(self.weapons)
        print(f"{self.name} has chosen {weapon.name}!")

        damage = choice(weapon.damage)
        target.health -= damage
        target.health = max(target.health, 0)

        print(f"{target.name} has been inflicted with -{damage}HP, leaving {target.name} with {target.health}HP!")

hero = Hero(name="Hero", health=100, weapons=[fists, iron_sword, dagger, bow])
enemy = Enemy(name="Enemy", health=100, weapons=[fists, bow])
