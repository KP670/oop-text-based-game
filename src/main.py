from character import Enemy, Player
from weapon import *
import os


def play_again():
    
    try:
        player_choice = input("Play again?: ").upper()
    except ValueError:
        print("Invalid response")
        return play_again()

    if(player_choice == "YES"):
        return game_loop()
    if(player_choice == "NO"):
        input("|END SCENE|")
        raise SystemExit
    else:
        print("Invalid input")
        return play_again()

def player_action(player, target):
    try:
        player_choice = int(input("Select your action: \n[1] Attack\n[2] Equip\n[3] Drop Current Weapon\n[4] Skip Turn\n:"))
    except ValueError:
        print("Value must be a string")
        input("Press ENTER to continue")
        return player_action(player, target)
    except KeyboardInterrupt:
        print("You have ended this game early")
        return play_again()


    if (player_choice == 1):
        player.attack(target)
    elif (player_choice == 2):
        player.equip()
    elif (player_choice == 3):
        player.drop()
    elif (player_choice == 4):
        print(f"\n{player.name} has skipped their turn!\n")
        return None
    else:
        print("Invalid value, pick a valid value")
        input("Press ENTER to continue")
        return player_action(player, target)

def game_loop():
    player_name = input("What is your name?: ")
    player = Player(name=player_name, health=100)
    enemy = Enemy(name="Enemy", health=100, weapons=[fists, bow, bow])
    player.equip()
    running = True
    while running:
        os.system("cls")
        player.health_bar.draw()
        enemy.health_bar.draw()
        
        player_action(player, enemy)
        if (player.health <= 0):
            print(f"{player.name} Loses...")
            running = False
            break

        try:
            input("Press ENTER to continue: ")
        except KeyboardInterrupt:
            print("\nYou have ended this game early")
            break

        enemy.attack(player)
        if (enemy.health <= 0):
            print(f"{player.name} has Won!")
            running = False
            break

        try:
            input("Press ENTER to continue: ")
        except KeyboardInterrupt:
            print("\nYou have ended this game early")
            break
    play_again()

game_loop()