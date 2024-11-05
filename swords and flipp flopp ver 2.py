import random
import time
import os

# Clear Terminal Function
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game Variables
balance = 50
weapon = "N/A"
armor_inventory = {"helmet": None, "chestplate": None, "leggings": None, "boots": None}
armor_stats = {
    "leather": 2,
    "chainmail": 4,
    "plate": 6,
    "tank": 8
}

# Weapons and Armor Shops
weapons = {
    "sword": [4, 4, 20],
    "axe": [4, 4, 25],
    "dagger": [1, 1, 5],
    "mace": [6, 6, 35],
    "shield": [0, 12, 10],
    "staff": [2, 2, 12],
    "flail": [6, 6, 35]
}

armor_shop = {
    "helmet": {"leather": 20, "chainmail": 40, "plate": 60, "tank": 80},
    "chestplate": {"leather": 40, "chainmail": 60, "plate": 80, "tank": 100},
    "leggings": {"leather": 32, "chainmail": 52, "plate": 72, "tank": 88},
    "boots": {"leather": 16, "chainmail": 36, "plate": 56, "tank": 76}
}

# player stats
vigor = 0
strength = 0
dexterity = 0
reaction = 0
skill_points = 30
player_level = 1

# Start Game
clear_terminal()
print("Loading game...")
time.sleep(2)
print("Welcome to Swords and Flip-Flops!")

# Character Creation
gender = input("\nPlease select gender (male or female): ").lower()
name = input("Enter your character's name: ")
clear_terminal()
print(f"Your character is {gender.capitalize()} and named {name}.\n")
clear_terminal()


# Stats Distribution
def stat_distribution():
    global skill_points, vigor, strength, dexterity, reaction
    while True:
        skill_points2 = skill_points
        vigor = strength = dexterity = reaction = 0
        choice = input("stat distribution screen. if you want information type (info). to continue, press enter")
        if choice == "info":
            print("Vigor: increases the amount of health you have / damage you can absorb.")
            print("Strength: increase the base amount of damage you deal")
            print("Dexterity: increases the amount of energy you have to do actions .")
            print("Reaction: increases the chance of dodging an attack.")
        else:
            print(f"You have {skill_points2} points to distribute between vigor, strength, dexterity, and reaction.")
            ed_vigor = int(input(f"Enter additional vigor: "))
            ed_strength = int(input(f"Enter additional strength: "))
            ed_dexterity = int(input(f"Enter additional dexterity: "))
            ed_reaction = int(input(f"Enter additional reaction: "))

            if ed_vigor + ed_strength + ed_dexterity + ed_reaction <= skill_points2:
                vigor += ed_vigor
                strength += ed_strength
                dexterity += ed_dexterity
                reaction += ed_reaction
                skill_points2 -= ed_vigor + ed_strength + ed_dexterity + ed_reaction
                time.sleep(2)
                print(f"Your stats: Vigor: {vigor}, Strength: {strength}, Dexterity: {dexterity}, Reaction: {reaction}")
                choice = input("Are you satisfied with your stats (yes/no)? ")
                if choice.lower() == "yes":
                    skill_points = skill_points2
                    break
            else:
                print("You have exceeded the skill points limit. Please try again.")

        




clear_terminal()

# Armory Functions
def buy_weapon():
    global balance, weapon
    print(f"Balance: {balance} gold coins\nAvailable Weapons:")
    for weapon_name, stats in weapons.items():
        print(f"{weapon_name.capitalize()} - Damage: {stats[0]}, Dexterity Cost: {stats[1]}, Price: {stats[2]}")
    
    weapon_choice = input("Enter the weapon name to buy or type 'back' to go back: ").lower()
    if weapon_choice in weapons:
        price = weapons[weapon_choice][2]
        if balance >= price:
            balance -= price
            weapon = weapon_choice
            print(f"You bought a {weapon_choice.capitalize()} for {price} gold!")
        else:
            print("Insufficient funds.")
    elif weapon_choice != "back":
        print("Invalid option.")

def buy_armor():
    global balance
    print(f"Balance: {balance} gold coins\nArmor Categories: Helmet, Chestplate, Leggings, Boots")
    armor_type = input("Choose armor category to buy or 'back' to return: ").lower()
    
    if armor_type in armor_shop:
        print(f"Available {armor_type.capitalize()} Types: Leather, Chainmail, Plate, Tank")
        for quality, price in armor_shop[armor_type].items():
            print(f"{quality.capitalize()} - Price: {price}")
        
        armor_choice = input("Enter the type of armor to buy or 'back' to return: ").lower()
        if armor_choice in armor_shop[armor_type]:
            price = armor_shop[armor_type][armor_choice]
            if balance >= price:
                balance -= price
                armor_inventory[armor_type] = armor_choice
                print(f"You bought a {armor_choice.capitalize()} {armor_type.capitalize()} for {price} gold!")
            else:
                print("Insufficient funds.")
    elif armor_type != "back":
        print("Invalid armor category.")

def sell_equipment():
    global balance
    print("Items you can sell:")
    for armor_type, armor_quality in armor_inventory.items():
        if armor_quality:
            sell_price = armor_shop[armor_type][armor_quality] // 2
            print(f"{armor_quality.capitalize()} {armor_type.capitalize()} - Sell Price: {sell_price}")

    equipment = input("Enter the equipment type to sell or 'back' to go back: ").lower()
    if equipment in armor_inventory and armor_inventory[equipment]:
        armor_quality = armor_inventory[equipment]
        sell_price = armor_shop[equipment][armor_quality] // 2
        balance += sell_price
        armor_inventory[equipment] = None
        print(f"You sold your {armor_quality.capitalize()} {equipment.capitalize()} for {sell_price} gold!")
    elif equipment != "back":
        print("Invalid choice or no item to sell in that category.")

# Battle Arena
def calculate_damage_reduction():
    total_reduction = 0
    for armor in armor_inventory.values():
        if armor:
            total_reduction += armor_stats[armor]
    return total_reduction

def generate_npc():
    vigor = random.randint(10, 30)
    strength = random.randint(1, 5)
    dexterity = random.randint(5, 15)
    return {"name": "Gladiator", "vigor": vigor, "strength": strength, "dexterity": dexterity}

# Random Animal NPCs
def generate_animal():
    animals = [
        {"name": "Tiger", "vigor": random.randint(15, 25), "strength": random.randint(2, 6), "dexterity": random.randint(10, 15)},
        {"name": "Bear", "vigor": random.randint(20, 30), "strength": random.randint(3, 7), "dexterity": random.randint(5, 10)}
    ]
    return random.choice(animals)

# Battle function
def battle(npc):
    global skill_points, balance, player_level, vigor, dexterity, strength, weapon, reaction

    print(f"You are fighting against {npc['name']}!")
    print("Battle starts now!")
    
    start_time = time.time()
    time_limit = 120

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Time is up! The bravest gladiator wins!")
            skill_points += 1
            break

        print(f"\nYour Vigor: {vigor}, Dexterity: {dexterity},         Enemy Vigor: {npc['vigor']}")
        print("Choose your action:")
        print("1. Quick Attack (90% chance)")
        print("2. Normal Attack (60% chance)")
        print("3. Heavy Attack (40% chance)")
        print("4. Recover")
        print("5. Surrender")

        action = input("Enter your choice: ")
        attack_cost = weapons[weapon][1] if weapon != "N/A" else 0

        if action == "5":
            print("You have surrendered!")
            balance -= 20
            break

        elif dexterity - attack_cost < 0:
            print("Not enough dexterity to perform that action!")
            continue

        if action == "1":
            hit_chance, min_damage, max_damage = 0.9, 1, (strength + weapons[weapon][0])
        elif action == "2":
            hit_chance, min_damage, max_damage = 0.6, (strength + weapons[weapon][0]), (strength + weapons[weapon][0])
        elif action == "3":
            hit_chance, min_damage, max_damage = 0.4, (strength + weapons[weapon][0]), strength + weapons[weapon][0]
        elif action == "4":
            recovery = random.randint(5, 10)
            dexterity = min(dexterity + recovery, 20)
            print(f"You recovered {recovery} dexterity!")
            continue

        if random.random() <= hit_chance:
            damage = random.randint(min_damage, max_damage)
            npc['vigor'] -= damage
            dexterity -= attack_cost
            print(f"You dealt {damage} damage to {npc['name']}!")
        else:
            print("Your attack missed!")

        if npc['vigor'] <= 0:
            print(f"You have defeated {npc['name']}!")
            skill_points += 2
            player_level += 1
            print(f"You leveled up to {player_level}.")
            break

        dodge_chance = min(20, reaction) / 100
        if random.random() < dodge_chance:
            print(f"You dodged {npc['name']}'s attack!")
            continue

        npc_damage = random.randint(1, npc['strength'])
        damage_reduction = calculate_damage_reduction() / 100
        reduced_damage = max(1, int(npc_damage * (1 - damage_reduction)))
        vigor -= reduced_damage
        print(f"{npc['name']} attacked and dealt {reduced_damage} damage (after reduction)!")
        
        if vigor <= 0:
            print("You have been defeated!")
            balance -= 20
            break

# Main Game Loop
def enter_battle_arena():
    while True:
        npc = generate_npc() if random.choice([True, False]) else generate_animal()
        battle(npc)
        if input("Do you want to fight again? (yes/no): ").lower() != "yes":
            break

# Main Game Loop
while True:
    clear_terminal()
    print("\nGame Lobby:\n1) Armory\n2) Battle Arena\n3) Sell Equipment\n4) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        clear_terminal()
        print("Armory:\n1) Buy Weapons\n2) Buy Armor\n3) Exit")
        armory_choice = input("Choose an option: ")
        if armory_choice == "1":
            buy_weapon()
        elif armory_choice == "2":
            buy_armor()
    elif choice == "2":
        clear_terminal()
        enter_battle_arena()
    elif choice == "3":
        clear_terminal()
        sell_equipment()
    elif choice == "4":
        clear_terminal()
        print("Exiting game.")
        break
    else:
        print("Invalid choice.")
