from character import enemy, hero

running = True
while running:

    if (hero.health > 0):
        print(f"{hero.name} Attacks!")
        hero.attack(enemy)
    
        if (enemy.health <= 0):
            print(f"The {hero.name} Wins!")
            running = False
    input()

    if (enemy.health > 0):
        print(f"{enemy.name} Attacks!")
        enemy.attack(hero)

        if (enemy.health <= 0): 
            print(f"The {hero.name} Loses...")
            running = False

    input()

