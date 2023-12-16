weapon_list = []
class Weapon:
    def __init__(self, name: str, type: str, damage: list, value: int) -> None:
        self.name = name
        self.type = type
        self. damage = damage
        self. value = value
        weapon_list.append(self)


iron_sword = Weapon(name="Iron Sword", 
                    type="Blades", 
                    damage=[4, 5, 6], 
                    value= 4)

dagger = Weapon(name="Dagger", 
                type="Blades", 
                damage=[5, 6, 7], 
                value= 4)

bow = Weapon(name="Bow", 
             type="Ranged", 
             damage=[6,7,8], 
             value= 8)

long_bow = Weapon(name="Long Bow", 
                  type="Ranged", 
                  damage=[8, 9, 10], 
                  value= 10)

fists = Weapon(name="Fists", 
                 type="Bare", 
                 damage=[1, 2], 
                 value= 0)

def list_weapons():
    count = 1
    for weapon in weapon_list:
        print(f"[{count}]: {weapon.name}: \n Dmg: {weapon.damage},\n Val: {weapon.value} \n")
        count += 1