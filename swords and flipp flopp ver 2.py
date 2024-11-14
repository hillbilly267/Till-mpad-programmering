import random
import time
import os

# Clear Terminal Function
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game Variables
balance = 500
weapon = "N/A"
shield = "N/A"
armor_inventory = {"helmet": None, "chestplate": None, "leggings": None, "boots": None}


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

# Armor Shop
armor = {
    "helmet": {
        "leather": [20, 1, 1],
        "chainmail": [40, 2, 2],
        "plate": [60, 4, 4],
        "tank": [80, 8, 8]
    },
    "chestplate": {
        "leather": [40, 2, 1],
        "chainmail": [60, 4, 2],
        "plate": [80, 6, 4],
        "tank": [100, 12, 8]
    },
    "leggings": {
        "leather": [32, 2, 1],
        "chainmail": [52, 4, 2],
        "plate": [72, 6, 4],
        "tank": [88, 12, 8]
    },
    "boots": {
        "leather": [16, 1, 1],
        "chainmail": [36, 2, 2],
        "plate": [56, 4, 4],
        "tank": [76, 8, 8]
    }
}

# player stats
vigor = 0
strength = 0
dexterity = 0
reaction = 0
skill_points = 50
player_level = 1

# Start Game
clear_terminal()
print("Loading game...")
time.sleep(2)
print("Welcome to Swords and Flip-Flops!")

# Character Creation
gender = input("\nPlease select gender (male, female or walmart bag): ")
name = input("Enter your character's name: ")
clear_terminal()
print(f"Your character is {gender.capitalize()} and named {name}.\n")
clear_terminal()



# Stats Distribution
def stat_distribution():
    global skill_points, vigor, strength, dexterity
    while True:
        skill_points3 = skill_points
        skill_points2 = skill_points
        choice = input("stat distribution screen. if you want information type (info). to continue, press enter")
        if choice.lower() == "info":
            print("Vigor: increases the amount of health you have / damage you can absorb.")
            print("Strength: increase the base amount of damage you deal")
            print("Dexterity: increases the amount of energy you have to do actions .")
        else:
            print(f"You have {skill_points2} points to distribute between vigor, strength, dexterity, and reaction.")
            ed_vigor = int(input(f"Enter additional vigor: "))
            skill_points2 -= ed_vigor
            print(f"you have {skill_points2} left")
            ed_strength = int(input(f"Enter additional strength: "))
            skill_points2 -= ed_strength
            print(f"you have {skill_points2} left")
            ed_dexterity = int(input(f"Enter additional dexterity: "))
            skill_points2 -= ed_dexterity

            if ed_vigor + ed_strength + ed_dexterity <= skill_points3:
                vigor += ed_vigor
                strength += ed_strength
                dexterity += ed_dexterity
                time.sleep(2)
                print(f"Your stats: Vigor: {vigor}, Strength: {strength}, Dexterity: {dexterity},\nskil points un-used: {skill_points2}")
                choice = input("Are you satisfied with your stats (yes/no)? ")
                if choice.lower() == "yes" or "":
                    skill_points = skill_points2
                    return vigor, strength, dexterity, skill_points
                    break
                else:
                    clear_terminal()
            else:
                clear_terminal()
                print("You have exceeded the skill points limit. Please try again.")

        



stat_distribution()
clear_terminal()

# Armory Functions
def buy_weapon():
    global balance, weapon, shield
    print(f"Balance: {balance} gold coins")
    print("Available Weapons:")
    
    # Show each weapon's details
    for name, stats in weapons.items():
        print(f"{name.capitalize()} - Damage: {stats[0]}, Dexterity Cost: {stats[1]}, Price: {stats[2]}")
    
    # Get user input
    choice = input("Enter weapon name to buy or 'back' to go back: ").lower()
    
    if choice in weapons == "shield":
        price = weapons[choice][2]
        if balance >= price:
            balance -= price
            shield = choice
            print(f"You bought a {choice.capitalize()} for {price} gold!")
            time.sleep(1)
        else:
            print("Not enough gold.")
    elif choice in weapons:
        price = weapons[choice][2]
        if balance >= price:
            balance -= price
            weapon = choice
            print(f"You bought a {choice.capitalize()} for {price} gold!")
            time.sleep(1)

    elif choice != "back":
        print("Invalid option.")


def buy_armor():
    global balance
    print(f"Balance: {balance} gold coins")
    print("Armor Categories: Helmet, Chestplate, Leggings, Boots")
    armor_type = input("Choose armor category to buy or 'back' to return: ").lower()
    
    if armor_type in armor:
        clear_terminal()
        print(f"Available {armor_type.capitalize()} Types:")
        for armor_quality, stats in armor[armor_type].items():
            print(f"{armor_quality.capitalize()}: Price: {stats[0]}, Defense: {stats[1]}, Weight: {stats[2]}")
        
        armor_choice = input("Enter the type of armor to buy or 'back' to return: ").lower()
        if armor_choice in armor[armor_type]:
            price = armor[armor_type][armor_choice][0]
            if balance >= price:
                balance -= price
                armor_inventory[armor_type] = armor_choice
                print(f"You bought a {armor_choice.capitalize()} {armor_type} for {price} gold!")
            else:
                print("Insufficient funds.")
        elif armor_choice != "back":
            print("Invalid armor type.")
    elif armor_type != "back":
        print("Invalid armor category.")

def sell_equipment():
    global balance, weapon
    print("Items you can sell:")
    for armor_type, armor_quality in armor_inventory.items():
        if armor_quality:
            sell_price = armor[armor_type][armor_quality][0]
            print(f"{armor_quality.capitalize()} {armor_type.capitalize()} - Sell Price: {sell_price}")

    if weapon != "N/A":
        weapon_sell_price = weapons[weapon][2]
        print(f"{weapon.capitalize()} - Sell Price: {weapon_sell_price}")
    equipment = input("Enter the equipment type to sell or 'back' to go back: ").lower()
    if equipment in armor_inventory and armor_inventory[equipment]:
        armor_quality = armor_inventory[equipment]
        sell_price = armor[equipment][armor_quality][0]
        balance += sell_price
        armor_inventory[equipment] = None
        print(f"You sold your {armor_quality.capitalize()} {equipment.capitalize()} for {sell_price} gold!")
    elif equipment == weapon:
        sell_price = weapons[weapon][2]
        balance += sell_price
        weapon = "N/A"
        print(f"You sold your {equipment.capitalize()} for {sell_price} gold!")
    elif equipment != "back":
        print("Invalid choice or no item to sell in that category.")




# Battle functions

def battle_choise():
    global weapon, dexterity, strength, balance
    print("\n1: quick attack: 2 dextarity cost")
    print("2: normal attack: 4 dextarity cost")
    print("3: heavy attack: 6 dextarity cost")
    print("4: recover dexterity")
    choice = input("Choose option: ")

    if choice == "1" or choice.lower() == "quick attack":
        clear_terminal()
        if random.random() > 10 and dexterity > 2:
            damage = 0.4 * strength + weapon[0]
            dex_cost = 2
            print(f"You did {damage} to apponent")
        else:
            print("Attack failed.")

    elif choice == "2" or choice.lower() == "normal attack":
        clear_terminal()
        if random.random() > 40 and dexterity > 4:
            damage = 0.6 * strength + weapon[0]
            dex_cost = 4
            print(f"You did {damage} to apponent")
        else:
            print("Attack failed.")

    elif choice == "3" or choice.lower() == "heavy attack":
        clear_terminal()
        if random.random() > 40 and dexterity > 6:
            damage = strength + weapon[0]
            dex_cost = 6
            print(f"You did {damage} to apponent")
        else:
            print("Attack failed.")

    elif choice == "4" or choice.lower() == "recover dexterity":
        regeneration = 0.3 * dexterity
        dexterity += regeneration
        print(f"Dexterity regenerates by {regeneration} points.")

    elif choice == 4 or choice.lower() == "give up":
        print("You give up but will be punished")
        balance -= 100 

    else:
        clear_terminal()
        print("Invalid choice.")

    return dex_cost, damage, balance, choice
    

def npc_battle_choise():
    global npc_dexterity, npc_strength
    if npc_dexterity < 6:
        npc_choice == 4
    else:
        npc_choice = random.randint(1,4)

    if npc_choice == "1" or choice.lower() == "quick attack":
        clear_terminal()
        if random.random(0, 100) > 10 and npc_dexterity > 2:
            npc_damage = 0.4 * strength + weapon[0]
            dex_cost = 2
            print(f"he did {npc_damage} to apponent")
        else:
            print("npc attack failed.")

    elif npc_choice == "2" or choice.lower() == "normal attack":
        clear_terminal()
        if random.random(0, 100) > 40 and npc_dexterity > 4:
            npc_damage = 0.6 * strength + weapon[0]
            dex_cost = 4
            print(f"he did {npc_damage} to apponent")
        else:
            print("npc attack failed.")

    elif npc_choice == "3" or choice.lower() == "heavy attack":
        clear_terminal()
        if random.random(0, 100) > 40 and npc_dexterity > 6:
            npc_damage = strength + weapon[0]
            dex_cost = 6
            print(f"he did {npc_damage} to apponent")
        else:
            print("npc attack failed.")

    elif npc_choice == "4" or choice.lower() == "recover dexterity":
        regeneration = 0.3 * dexterity
        npc_dexterity += regeneration
        print(f"Dexterity regenerates by {regeneration} points.")

    return dex_cost, npc_damage, npc_choice


def calculate_damage_reduction():
    global armor_inventory, armor_type, armor_quality, shield, dexterity
    total_reduction = 0
    for armor_type, armor_quality in armor_inventory.items():
        if armor_quality and shield == "shield":
            total_reduction += armor[armor_type][armor_quality][1] + shield[1]
            dexterity -= shield[2]
        elif armor_quality:
            total_reduction += armor[armor_type][armor_quality][1]
    return total_reduction, dexterity




def generate_npc():
  global player_level
  npc_skillpoint = 30 
  npc_skillpoint += player_level * 2
  npc_skillpoint2 = npc_skillpoint
  npc_vigor = random.randint(5,npc_skillpoint2)
  npc_skillpoint2 -= npc_vigor
  npc_strength = random.randint(1, npc_skillpoint2)
  npc_skillpoint2 -= npc_strength
  npc_dexterity = random.randint(1, npc_skillpoint2)

  npc_name = "gladiator"
  if random.randint(0, 100) > 20:
      npc_name = "Gladiator"
  elif random.randint(0, 100) > 50:
      npc_name = "Wolf"
  else:
      npc_name = "Bear"

  return {npc_name, npc_vigor, npc_strength, npc_dexterity, npc_reaction,}

npc_name = 0
npc_vigor = 0
npc_strength = 0
npc_dexterity = 0
npc_reaction = 0


# Battle Arena
def battle_arena():
    global skill_points, balance, player_level, vigor, dexterity, strength, weapon, reaction, armor_inventory
    global npc_name, npc_vigor, npc_strength, npc_dexterity, npc_reaction
    global armor_inventory, armor_type, armor_quality, shield, dexterity
    
    npc_data = generate_npc()
    npc_name, npc_vigor, npc_strength, npc_dexterity, npc_reaction = npc_data
    
    print(f"You are fighting against {npc_name}!")
    print("Battle starts now!")
    
    # Battle timer setup
    start_time = time.time()
    time_limit = 320
    
    while True:
        # Check for time limit
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Time is up! The bravest gladiator wins!")
            skill_points += 1
            break

        # Display time left and health stats
        print(f"\nTime left: {time_limit - elapsed_time:.2f} seconds")
        print(f"Your health: {vigor}, Your dexterity: {dexterity}")
        print(f"{npc_name} health: {npc_vigor}, {npc_name} dexterity: {npc_dexterity}")

        # Player's turn
        player_action = battle_choise()
        if player_action:
            dex_cost, damage, balance, choice = player_action
            if dex_cost <= dexterity:
                dexterity -= dex_cost 
                npc_vigor -= damage
                print(f"You inflicted {damage} damage to {npc_name}!")

                # Check if NPC is defeated
                if npc_vigor <= 0:
                    print(f"Congratulations! You defeated {npc_name}.")
                    skill_points += 5
                    player_level += 1
                    balance += 100
                    break
            else:
                print("Not enough dexterity for that action.")
        else:
            print("Invalid choice. Try again.")
        
        # NPC's turn
        npc_action = npc_battle_choise()
        if npc_action:
            npc_dex_cost, npc_damage, npc_choice = npc_action
        if npc_dex_cost <= npc_dexterity:
            npc_dexterity -= npc_dex_cost
            total_reduction, dexterity = calculate_damage_reduction()
            npc_damage -= total_reduction
            vigor -= npc_damage
            print(f"{npc_name} inflicted {npc_damage} damage on you!")

                # Check if player is defeated
            if vigor <= 0:
                    print("You have been defeated. Better luck next time!")
                    skill_points -= 1
                    balance -= 50  # Penalty for losing
                    break
            else:
                print(f"{npc_name} tried to attack but didn't have enough dexterity.")

        # Check for end conditions
        if vigor <= 0 or npc_vigor <= 0:
            break

        


# Main Game Loop
while True:
    clear_terminal()
    print("\nGame Lobby:\n1) Armory\n2) Battle Arena\n3) Sell Equipment\n4) Stat distrobution \n5)Exit")
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
        battle_arena()
    elif choice == "3":
        clear_terminal()
        sell_equipment()
    elif choice == "4" and skill_points >0:
        clear_terminal()
        stat_distribution()
    elif choice == "5":
        clear_terminal()
        print("Exiting game.")
        break
    else:
        print("Invalid choice.")
