from random import choice
from weapon import *
from health_bar import HealthBar
from pygame import mixer

mixer.init()

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health

    

class Player(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
        self.weapon = fists
        self.health_bar = HealthBar(self, color="green")
        
    def equip(self) -> None:
        print(f"Your current weapon is: {self.weapon.name} \n")

        print("[0]: to keep your current weapon\n")
        list_weapons()

        try:
            player_selected_weapon = int(input("Your choice is: ")) - 1
        except ValueError:
            print("Invalid value")
            input("Press ENTER to continue")
            return self.equip()
        except IndexError:
            print("Value is out of range")

        if (player_selected_weapon == 0):
            print("The player has decided to keep their current weapon!")
        else:
            self.weapon = weapon_list[player_selected_weapon]
            print(f"\n{self.name} has selected {self.weapon.name}!\n")


    def drop(self) -> None:
        self.weapon = fists
        print(f"You have dropped your weapon. Your weapon is now: {self.weapon.name}")

    def attack(self, target) -> None:
        print(f"{self.name} has chosen to Attack with {self.weapon.name}!")

        damage = choice(self.weapon.damage)
        target.health -= damage
        target.health = max(target.health, 0)

        print(f"{target.name} has been inflicted with -{damage}HP, leaving {target.name} with {target.health}HP!")
        target.health_bar.update()


class Enemy(Character):
    def __init__(self, name: str, health: int, weapons: list) -> None:


        super().__init__(name=name, health=health)
        self.weapons = weapons
        self.health_bar = HealthBar(self, color="red")


    def attack(self, target) -> None:
        weapon = choice(self.weapons)
        print(f"{self.name} has chosen {weapon.name}!")

        damage = choice(weapon.damage)
        target.health -= damage
        target.health = max(target.health, 0)

        print(f"{target.name} has been inflicted with -{damage}HP, leaving {target.name} with {target.health}HP!")
        target.health_bar.update()