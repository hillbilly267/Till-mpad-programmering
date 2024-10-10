import random
import time 
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

dice=[1,2,3,4,5,6,7,8,9,10]

diff = "N/A"
lev_violence = 0
gender= "N/A"

#starter stats
vigor = 20
strength = 2
dexterity = 20
reaction = 1
total_points = 20




# print("loading disk")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print("loading done")
# time.sleep(1)
# print("welcome to swords and flipp flopps")
# time.sleep(1)
# print("please select difficulty: easy, normal, hard.")
# time.sleep(1)
# a2 = input("if you want more info on what changes with the difficulty type 1, if not hit enter: ")

# if a2 == "1":
#     print("\nThe difficulty changes the stats given to the NPC´s, increases the chances of you succeeding and lowers theirs.\nLowers the judgment of the public and king.")

# while True:
#     a1 = input("\nEnter difficulty: ")
#     if a1 == "easy":
#         diff = "easy" 
#         print("you have selected easy")
#         break 
#     elif a1 == "normal":
#         diff = "normal" 
#         print("you have selected normal")
#         break
#     elif a1 == "hard":
#         diff = "hard"
#         print("you have selected hard")
#         break
#     else:
#         print("Invalid option, please select again.")
# clear_terminal()




# print("Please select level of voilenc 1 if your under the age of 18 and 2 if your over the age of 18")

# while True:
#     a3=int(input())
#     if a3==1:
#         lev_violence = 1
#         break
#     elif a3==2:
#         lev_violence = 2
#         break
#     else:
#         print("invalid option, try again")
# time.sleep(1)
# clear_terminal()
# print("precessing")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print("chracter creation screen")
# time.sleep(1)
# print("please select gender, male ore female")
# while True:
#     a4=input("")
#     if a4=="male":
#         gender = "male"
#         print("you have chosen male")
#         break
#     elif a4=="female":
#         gender = "female"
#         print("you have chosen female")
#         break
#     else:
#         print("invalid gender, try again")
# time.sleep(1)
# name=input("please enter your name: ")
# time.sleep(1)
# print("Your name is:", name)
# time.sleep(1)
# clear_terminal()








# print("stat distrobution screen")
# time.sleep
# a5 = input("if you want more info about what stat does type 1, if not hit enter: ")
# if a5 == "1":
#     clear_terminal()
#     print("Vigor is the amount of hit points you have, and you have a base of 20.\n"
#           "Strength is the amount of damage you will deliver, and base is 2.")
#     time.sleep(10)
#     print("\nDexterity is the amount of energy you have. Each attack takes an amount of energy; the base is 20, Note: weapons add additional energy usage.\n"
#           "Reaction is the percentage you have to dodge an attack. The base is a 10% chance to dodge, and each point adds an extra 5% upp to 50%.")
#     time.sleep(5)
# print("\nYou have 20 starter points. Please distribute the points between vigor, strength, dexterity, and reaction\n.")








# satisfied = "no"

# while satisfied.lower() == "no":
#     print("Starting stats -> Vigor:", vigor, "Strength:", strength, "Dexterity:", dexterity, "Reaction:", reaction)
#     print("Total points to distribute:", total_points)

#     vigor = 20
#     strength = 2
#     dexterity = 20
#     reaction = 1
#     total_points = 20
    

#     while total_points > 0:
#         add_vigor = input("Enter additional vigor points: ")
        
#         if not add_vigor:
#             print("No points added.")
#             time.sleep(1)
#             break
        
#         add_vigor = int(add_vigor)
        
#         if add_vigor > total_points:
#             print("Can't be more than your total points.")
#         else:
#             vigor += add_vigor
#             total_points -= add_vigor
#             print("Remaining points:", total_points)
#             break

#     while total_points > 0:
#         add_strength = input("Enter additional strength points: ")
        
#         if not add_strength:
#             print("No points added.")
#             time.sleep(1)
#             break
        
#         add_strength = int(add_strength)
        
#         if add_strength > total_points:
#             print("Can't be more than your total points.")
#         else:
#             strength += add_strength
#             total_points -= add_strength
#             print("Remaining points:", total_points)
#             break

#     while total_points > 0:
#         add_dexterity = input("Enter additional dexterity points: ")
        
#         if not add_dexterity:
#             print("No points added.")
#             time.sleep(1)
#             break
        
#         add_dexterity = int(add_dexterity)
        
#         if add_dexterity > total_points:
#             print("Can't be more than your total points.")
#         else:
#             dexterity += add_dexterity
#             total_points -= add_dexterity
#             print("Remaining points:", total_points)
#             break

#     while total_points > 0:
#         add_reaction = input("Enter additional reaction points: ")
        
#         if not add_reaction:
#             print("No points added.")
#             time.sleep(1)
#             break
        
#         add_reaction = int(add_reaction)
        
#         if add_reaction > total_points:
#             print("Can't be more than your total points.")
#         else:
#             reaction += add_reaction
#             total_points -= add_reaction
#             print("Remaining points:", total_points)
#             break

#     print("This is your final point distribution + base stats:")
#     print("Vigor:",vigor ,"Strength:",strength ,"Dexterity:",dexterity ,"Reaction:",reaction)

#     satisfied = input("Are you satisfied with your point distribution? (yes/no): ")
#     if satisfied=="no":
#         total_points = 20
#         clear_terminal
        



# clear_terminal
# time.sleep(1)
# print("Loading lobby...")
# time.sleep(2)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)
# print(".")
# time.sleep(1)



#weapons

weapons = ["sword", "axe", "dagger", "mace", "shield", "staff", "flail"]

# armor
helmet_armor = ["leather helmet", "chainmail helmet", "iron helmet", "tank helmet"]
chest_plate_armor = ["leather chestplate", "chainmail chestplate", "iron chestplate", "tank chestplate"] 

#NPC

# player_info
balance = 50
weapon = "N/A",
helmet = "N/A",
chest_plate = "N/A"



# # print("Welcome to the game lobby!\n make sure you use numbers when selecting if not stated otherwise")

while True:
    print("Choose an option:")
    print("1. smith")
    print("2. Armory")
    print("3. Battle Arena")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        clear_terminal
        print("You have entered the Smith. Here you can upgrade and repair weapons and armour.")
        while True:
            print("choose an option:")
            print("1. Upgrade equipment")
            print("2. repair equipment")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Upgrade")
        
            elif choice == 2:
                print("Upgrade")

            elif choice == 3:
                print("Returning to the lobby: ")
                time.sleep(1)
                break
        else:
            print("Invalid option. Please try again.")




    elif choice == 2:
        clear_terminal()
        print("\nYou have entered the Armory. Here you can buy and sell armor and weapons.")
        while True:
          print("choose an option:")
          print("1. buy weapons")
          print("2. buy armor")
          print("3. sell equipment")
          print("4. Exit")
          choice = int(input("enter your choice: "))
          if choice == 1:
            clear_terminal()
            print("\nyou have enterd the weapon section.\n")
            print("your balance:", balance,)
            print("\nlist of weapons:\n",weapons)
            weapon_option=input("if you want more information about a weapon, type its name.\n If you want to buy a weapon, type: buy (weapons mane)\n: ")
            if weapon_option == "sword":
                print("\n:An iron sword is the most basic and commoly used weapon.\nIt it well balanced between damage:4 and dexterity:4.\n")
            elif weapon_option == "axe":
               print("\n: The axe is like the sword.\nIt is well balanced between damage:4 and dexterity:4.\n")
            elif weapon_option == "dagger":
               print("\n: A dagger is a small, light weapon.\nIt it does less damage:1 but also less dexterity:1.\n")
            elif weapon_option == "mace":
               print("\n:Mace is a heavy weapon.\nIt it does more damage:6 but also more dexterity:6.\n")
            elif weapon_option == "shield":
               print("\n: A shield is a protective tool that can be used alongside other weapons.\nIt does no damage but and will increas dextarity:4 but is another way to get more armor:4.\n")
            elif weapon_option == "staff":
               print("\n: A staff is a bit heavier then dagger but lighter then sword.\nIt it does less damage:2 but also less dexterity:2.\n")
            elif weapon_option == "flail":
               print("\n: A flail is a heavy weapon.\nIt it does more damage:6 but also more dexterity:6.\n")

            elif weapon_option == "buy sword":
                yes_No = input("\n: A sword costs 20 gold coins.\n\nDo you want to buy it? (yes/no): ")
                if yes_No == "yes" and balance >= 20:
                    balance -= 20
                    print("\n: You have bought a sword.")
                    weapon = "sword"
                elif yes_No == "no":
                    print("\n: Oh well.\n")
                
                elif weapon_option == "axe":
                    yes_No = input("\n: An axe costs 15 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 20:
                        balance -= 20
                        print("\n: You have bought an axe.")
                        weapon = "axe"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "dagger":
                    yes_No = input("\n: A dagger costs 5 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 5:
                        balance -= 5
                        print("\n: You have bought a dagger.")
                        weapon = "dagger"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "mace":
                    yes_No = input("\n: A mace costs 30 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 30:
                        balance -= 30
                        print("\n: You have bought a mace.")
                        weapon = "mace"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "shield":
                    yes_No = input("\n: A shield costs 10 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 10:
                        balance -= 10
                        print("\n: You have bought a shield.")
                        weapon = "shield"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "staff":
                    yes_No = input("\n: A staff costs 12 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 10:
                        balance -= 12
                        print("\n: You have bought a staff.")
                        weapon = "staff"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "flail":
                    yes_No = input("\n: A flail costs 35 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 30:
                        balance -= 35
                        print("\n: You have bought a flail.")
                        weapon = "flail"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")

          elif choice == 2:
            clear_terminal()
            print("you have entered the armor section")
            print("your balance:", balance,)
            print("\nlist of armors:\nhelmets: ",helmet_armor,"\nchest plates: ", chest_plate_armor,"\n")
            armor_option=input("if you want more information about a armour, type its name, note armor value is prosental so armor:4 means you will take 4% less damage\n If you want to buy armour, type: buy (armours mane)\n: ")
            if armor_option == "leather helmet":
                print("\n:the leather helmet is the the most basic of armour. Its is the weakest so armor:2\n")
            elif armor_option == "chainmail helmet":
               print("\n: The Chainmail Helmet is a step up from leather helmet, offering better armor:4.\n")
            elif armor_option == "iron helmet":
               print("\n: The Iron Helmet is solid and dependable, offering significantly more armor:6.\n")
            elif armor_option == "tank helmet":
               print("\n: The Tank Helmet is the most formidable headgear, designed for players who prioritize defense above all. Its thick metal plating provides unmatched armor:8\n Note becouse its so heavy it will increas dextarity usage by 10.\n")
            elif armor_option == "shield":
               print("\n: A shield is a protective tool that can be used alongside other weapons.\nIt does no damage but and will increas dextarity:4 but is another way to get more armor:4.\n")
            elif armor_option == "staff":
               print("\n: A staff is a bit heavier then dagger but lighter then sword.\nIt it does less damage:2 but also less dexterity:2.\n")
            elif armor_option == "flail":
               print("\n: A flail is a heavy weapon.\nIt it does more damage:6 but also more dexterity:6.\n")

            elif weapon_option == "buy sword":
                yes_No = input("\n: A sword costs 20 gold coins.\n\nDo you want to buy it? (yes/no): ")
                if yes_No == "yes" and balance >= 20:
                    balance -= 20
                    print("\n: You have bought a sword.")
                    weapon = "sword"
                elif yes_No == "no":
                    print("\n: Oh well.\n")
                
                elif weapon_option == "axe":
                    yes_No = input("\n: An axe costs 15 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 20:
                        balance -= 15
                        print("\n: You have bought an axe.")
                        weapon = "axe"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "dagger":
                    yes_No = input("\n: A dagger costs 5 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 5:
                        balance -= 5
                        print("\n: You have bought a dagger.")
                        weapon = "dagger"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "mace":
                    yes_No = input("\n: A mace costs 30 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 30:
                        balance -= 30
                        print("\n: You have bought a mace.")
                        weapon = "mace"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "shield":
                    yes_No = input("\n: A shield costs 10 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 10:
                        balance -= 10
                        print("\n: You have bought a shield.")
                        weapon = "shield"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "staff":
                    yes_No = input("\n: A staff costs 12 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 10:
                        balance -= 12
                        print("\n: You have bought a staff.")
                        weapon = "staff"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
                
                elif weapon_option == "flail":
                    yes_No = input("\n: A flail costs 35 gold coins.\n\nDo you want to buy it? (yes/no): ")
                    if yes_No == "yes" and balance >= 30:
                        balance -= 35
                        print("\n: You have bought a flail.")
                        weapon = "flail"
                    elif yes_No == "no":
                        print("\n: Oh well.\n")
                    else:
                        print("\n: Invalid option.")
          elif choice == 3:
            clear_terminal()
            print("hello")
          elif choice == 4:
            clear_terminal
            print("Returning to the lobby.")
            time.sleep(1)
            break
          else:
            print("Invalid option. Please try again.")




    elif choice == 3:
        clear_terminal
        print("You have entered the Battle Arena.")
        print("Are you sure you want to battle? (yes/no)")
        confirmation = input("Enter your choice: ")

        if confirmation == "yes":
            print("not implemented yet")
            
            
        elif confirmation == "no":
            print("Returning to the lobby.")
        else:
            print("Invalid option. Please try again.")


    elif choice == 4:
        print("Exiting the game lobby. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")

