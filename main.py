from character import enemy, Player



player = Player(name="Hero", health=100)

def player_action(player, target):
    try:
        player_choice = int(input("Select your action: \n[1] Attack\n[2] Equip\n[3] Drop Current Weapon\n[4] Skip Turn\n:"))
    except ValueError:
        print("Value must be a string")
        return player_action(player, target)
    
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
        return player_action(player, target)


player.equip()

running = True
while running:
    player_action(player, enemy)

    enemy.attack(player)

    if (player.health <= 0):
        print(f"{player.name} Loses...")
        running = False
    elif (enemy.health <= 0):
        print(f"{player.name} has Won!")
        running = False

    input()