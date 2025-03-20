import time
import os
import random

# a simple implementation for clearing the terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


#a simple implementation for writing a test character by character
def printtextanimation(text, animation_speed=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(animation_speed)
    print()

def start_at_point():
    printtextanimation("Choose a room to enter:")
    printtextanimation("1. First Cell")
    printtextanimation("2. Kitchen")
    printtextanimation("3. Ventilation System")
    printtextanimation("4. Guard Room")
    printtextanimation("5. Quiet Escape")
    printtextanimation("6. Kitchen Room")
    printtextanimation("7. Yard Escape")
    printtextanimation("8. Roof Escape")
    printtextanimation("9. Guard Disguise")
    printtextanimation("10. Infirmary Room")
    printtextanimation("11. Library Room")
    printtextanimation("12. Secret Passage")
    printtextanimation("13. Infirmary Room")
    printtextanimation("14. Workshop Room")
    printtextanimation("15. Cafeteria Room")
    printtextanimation("16. Laundry Room")
    printtextanimation("17. Gym Room")
    printtextanimation("18. Chapel Room")

    choice = input("Enter your choice: ")
    if choice == '1':
        cls()
        first_cell()
    elif choice == '2':
        cls()
        kitchen_room()
    elif choice == '3':
        cls()
        ventilation_room()
    elif choice == '4':
        cls()
        guard_room()
    elif choice == '5':
        cls()
        quiet_escape()
    elif choice == '6':
        cls()
        kitchen_room()
    elif choice == '7':
        cls()
        yard_escape()
    elif choice == '8':
        cls()
        roof_escape()
    elif choice == '9':
        cls()
        guard_disguise()
    elif choice == '10':
        cls()
        infirmary_room()
    elif choice == '11':
        cls()
        library_room()
    elif choice == '12':
        cls()
        secret_passage()
    elif choice == '13':
        cls()
        infirmary_room()
    elif choice == '14':
        cls()
        workshop_room()
    elif choice == '15':
        cls()
        cafeteria_room()
    elif choice == '16':
        cls()
        laundry_room()
    elif choice == '17':
        cls()
        gym_room()
    elif choice == '18':
        cls()
        chapel_room()
    else:
        printtextanimation("Invalid choice. Try again.")
        home_screen()

def credits():
    printtextanimation("""              
                       Created by Sebastian Gudmundss, 2025
                       Story written by Sebastian Gudmundsson
                       Music composed by Sebastian Gudmundsson
                       Artwork by Sebastian Gudmundsson
                       Developed using Python 3.9.10 by Sebastian Gudmundsson""", animation_speed=0.001)
    input("\npress enter to go back to home screen")
    cls()
    home_screen()


sav1 = ""
sav2 = ""
sav3 = ""

def save_screen():
    global save1, save2, save3

    print("save 1", sav1)
    print("save 2", sav2)
    print("save 3", sav3)
    a = input("\nchoos a save file. 1-3")
    if a == "1":
        save = save1
        save_file(guard_room())
    elif a == "2":
        save = save2
    elif a == "3":
        save = save3
    return save



def save_file(room):
    global save
    try:
        with open(save, "x") as f:
            f.write(room)
            print("Game saved!")
    except Exception as e:
        print(f"Error saving game: {e}")

def title():
    printtextanimation("""  
  _____      _                       ____                 _        
 |  __ \    (_)                     |  _ \               | |       
 | |__) | __ _ ___ ___  ___  _ __   | |_) |_ __ ___  __ _| | __
 |  ___/ '__| / __/ __|/ _ \| '_ \  |  _ <| '__/ _ \/ _` | |/ /
 | |   | |  | \__ \__ \ (_) | | | | | |_) | | |  __/ (_| |   <
 |_|   |_|  |_|___/___/\___/|_| |_| |____/|_|  \___|\__,_|_|\_|
                                                                   """, animation_speed=0.0001)
    
def home_screen():
    cls()
    print("""
  _____      _                       ____                 _        
 |  __ \    (_)                     |  _ \               | |       
 | |__) | __ _ ___ ___  ___  _ __   | |_) |_ __ ___  __ _| | __
 |  ___/ '__| / __/ __|/ _ \| '_ \  |  _ <| '__/ _ \/ _` | |/ /
 | |   | |  | \__ \__ \ (_) | | | | | |_) | | |  __/ (_| |   <
 |_|   |_|  |_|___/___/\___/|_| |_| |____/|_|  \___|\__,_|_|\_|
                                                                   
 play (1)    start at a specific point (2)     credits (3)

    """)
    a = input("")
    if a == "1":
        cls()
        save_screen()
    elif a == "2":
        cls()
        start_at_point()
    
    elif a == "3":
        cls()
        credits()
    else:
        cls()
        printtextanimation("Invalid")
        home_screen()

def start():
    time.sleep(1)
    printtextanimation("\n Press enter to continue")
    x = input()
    if x == "":
        cls()
        print("\n")
        printtextanimation("PRISON BREAK")
        time.sleep(1)
        print("\n")
        printtextanimation("Your sentence has been ruled")
        time.sleep(1)
        print("\n")
        printtextanimation("You have been taken to the jail cell")
        time.sleep(1)
        print("\n")
        printtextanimation("You will be given 30 minutes to escape")
        time.sleep(1)
        print("\n")
        printtextanimation("Good luck!")
        time.sleep(1)
        print("\n")
        printtextanimation("Press enter to continue")
        input()
        cls()
        first_cell()
    else:
        printtextanimation("Invalid")
        cls()
        start()

def first_cell():
    printtextanimation("\nYou find yourself in a dark and dusty cell.")
    time.sleep(1)
    printtextanimation("A heavy door is locked behind you.")
    time.sleep(1)
    printtextanimation("You look around seeing if there's something you can use to your advantage.")
    time.sleep(1)
    printtextanimation("searching ......... searching.......\n")
    time.sleep(1)
    printtextanimation("Inside the mattress you find a small hand file and when looking at the window, you can see some scratch marks from someone else filing.\n Maybe you can file your way out through the window")
    printtextanimation("\nYou can also see that a panel on the ventilation system is loose. You can probably use that file to screw loose the rest of the screws and escape through the ventilation system.")
    printtextanimation("\nYou look out through the cell bars and see a guard to the left at the end of the corridor and a wall to the right with what looks like a mirror. \n You can probably call the guard near the cell and grab him.")
    
    printtextanimation("\nWhat do you want to do?")
    printtextanimation("1. File the window")
    printtextanimation("2. Unscrew the ventilation panel")
    printtextanimation("3. Call the guard")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        window_room()
    elif choice == "2":
        ventilation_room()
    elif choice == "3":
        guard_room()
    else:
        printtextanimation("Invalid choice. Try again.")
        first_cell()

def window_room():
    printtextanimation("\nYou start filing the window bars. It's a slow process, but you're making progress.")
    time.sleep(1)
    printtextanimation("After a while, you hear footsteps approaching.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Keep filing, but more quietly")
    printtextanimation("2. Hide the file and pretend to sleep")
    printtextanimation("3. Try to quickly finish and escape")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("You continue filing quietly, but the guard notices and you're caught. Game Over.")
        game_over()
    elif choice == "2":
        quiet_escape()
    elif choice == "3":
        printtextanimation("In your haste, you make too much noise. The guard catches you. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        window_room()

def ventilation_room():
    printtextanimation("\nYou manage to unscrew the ventilation panel and crawl inside.")
    time.sleep(1)
    printtextanimation("You find yourself at a junction in the ventilation system.")
    printtextanimation("\nWhich way do you go?")
    printtextanimation("1. Left")
    printtextanimation("2. Right")
    printtextanimation("3. Straight ahead")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        kitchen_room()
    elif choice == "2":
        workshop_room()
    elif choice == "3":
        library_room()
    else:
        printtextanimation("Invalid choice. Try again.")
        ventilation_room()

def guard_room():
    printtextanimation("\nYou call the guard over. As he approaches, you prepare to make your move.")
    time.sleep(1)
    printtextanimation("The guard is now right in front of your cell.")
    printtextanimation("\nWhat's your next move?")
    printtextanimation("1. Try to grab his keys")
    printtextanimation("2. Attempt to knock him out")
    printtextanimation("3. Pretend you're sick and need help")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("You manage to grab the keys, but the guard raises an alarm. You're caught. Game Over.")
        game_over()
    elif choice == "2":
        guard_disguise()
    elif choice == "3":
        infirmary_room()
    else:
        printtextanimation("Invalid choice. Try again.")
        guard_room()

def quiet_escape():
    printtextanimation("\nThe guard passes by without noticing anything suspicious.")
    time.sleep(1)
    printtextanimation("You resume filing the window bars and eventually create an opening.")
    printtextanimation("\nWhat's your next move?")
    printtextanimation("1. Squeeze through the opening immediately")
    printtextanimation("2. Wait for nightfall to escape")
    printtextanimation("3. Create a rope from bedsheets before escaping")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("You're spotted by a guard in the yard. Game Over.")
        game_over()
    elif choice == "2":
        yard_escape()
    elif choice == "3":
        roof_escape()
    else:
        printtextanimation("Invalid choice. Try again.")
        quiet_escape()

def kitchen_room():
    printtextanimation("\nYou emerge from the ventilation system into the prison kitchen.")
    time.sleep(1)
    printtextanimation("It's currently empty, but you hear voices approaching.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Hide in a large pot")
    printtextanimation("2. Disguise yourself as a kitchen worker")
    printtextanimation("3. Try to sneak out through the back door")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        cafeteria_room()
    elif choice == "2":
        laundry_room()
    elif choice == "3":
        yard_escape()
    else:
        printtextanimation("Invalid choice. Try again.")
        kitchen_room()



def yard_escape():
    printtextanimation("\nYou've made it to the prison yard under the cover of darkness.")
    time.sleep(1)
    printtextanimation("The high walls loom before you.")
    printtextanimation("\nHow do you proceed?")
    printtextanimation("1. Try to climb the wall")
    printtextanimation("2. Look for a weak spot in the fence")
    printtextanimation("3. Hide in a delivery truck")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("You're spotted by a guard tower while climbing. Game Over.")
        game_over()
    elif choice == "2":
        freedom()
    elif choice == "3":
        printtextanimation("The truck is thoroughly checked before leaving, and you're discovered. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        yard_escape()

def roof_escape():
    printtextanimation("\nYou've made it to the roof using your makeshift rope.")
    time.sleep(1)
    printtextanimation("You can see the outside world, but you're not free yet.")
    printtextanimation("\nWhat's your plan?")
    printtextanimation("1. Use the rope to descend the outer wall")
    printtextanimation("2. Jump to a nearby building")
    printtextanimation("3. Wait for a helicopter to fly by and try to grab onto it")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        freedom()
    elif choice == "2":
        printtextanimation("The jump is too far and you fall. Game Over.")
        game_over()
    elif choice == "3":
        printtextanimation("No helicopter comes. You're discovered on the roof in the morning. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        roof_escape()

def guard_disguise():
    printtextanimation("\nYou knoced the guard out and took his clothes. Now disguised as a guard, You blend in somewhat, but you're not out yet and some may till recognize you.")
    time.sleep(1)
    printtextanimation("You need to find a way out of the prison complex.")
    printtextanimation("\nWhere do you go?")
    printtextanimation("1. Head to the main gate")
    printtextanimation("2. Try to sneak into the warden's office")
    printtextanimation("3. Go to the guard break room")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("Your disguise isn't good enough to fool the gate guards. You're caught. Game Over.")
        game_over()
    elif choice == "2":
        warden_office()
    elif choice == "3":
        printtextanimation("Real guards in the break room quickly realize you don't belong. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        guard_disguise()

def laundry_room():
    printtextanimation("\nDisguised as a kitchen worker, you make your way to the laundry room.")
    time.sleep(1)
    printtextanimation("You see an opportunity to escape through the laundry chute.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Slide down the laundry chute")
    printtextanimation("2. Hide in a laundry cart")
    printtextanimation("3. Try to blend in with the laundry workers")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("The chute leads to a dead end. You're discovered and caught. Game Over.")
        game_over()
    elif choice == "2":
        freedom()
    elif choice == "3":
        printtextanimation("A supervisor notices you're not supposed to be there. You're caught. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        laundry_room()

def warden_office():
    printtextanimation("\nYou've managed to sneak into the warden's office.")
    time.sleep(1)
    printtextanimation("You see a computer, a safe, and a window overlooking the prison yard.")
    printtextanimation("\nWhat's your next move?")
    printtextanimation("1. Try to access the computer")
    printtextanimation("2. Attempt to crack the safe")
    printtextanimation("3. Look out the window for escape routes")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("You trigger an alarm while using the computer. Guards rush in. Game Over.")
        game_over()
    elif choice == "2":
        printtextanimation("The safe contains evidence of corruption. You use it to blackmail your way to freedom.")
        freedom()
    elif choice == "3":
        printtextanimation("While looking out the window, the warden returns and catches you. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        warden_office()

def freedom():
    printtextanimation("\nCongratulations! You've successfully escaped from prison!")
    time.sleep(1)
    printtextanimation("You're now free, but be careful out there...")
    printtextanimation("Thanks for playing Prison Break!")
    exit()

def game_over():
    printtextanimation("\nGame Over. Try again?")
    choice = input("Enter 'yes' to restart: ").lower()
    if choice == 'yes':
        cls()
        start()
    else:
        exit()

def library_room():
    printtextanimation("\nYou find yourself in the prison library, filled with books and a few inmates.")
    time.sleep(1)
    printtextanimation("You notice a suspicious book that seems out of place.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Pull the book")
    printtextanimation("2. Ignore it and look for another way out")
    printtextanimation("3. Ask an inmate for help")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        secret_passage()
    elif choice == "2":
        printtextanimation("You find nothing else of interest. You're caught by guards. Game Over.")
        game_over()
    elif choice == "3":
        printtextanimation("The inmate betrays you to the guards. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        library_room()

def secret_passage():
    printtextanimation("\nThe bookcase slides open, revealing a secret passage.")
    time.sleep(1)
    printtextanimation("You enter the passage and find yourself in a dimly lit tunnel.")
    printtextanimation("\nWhich direction do you go?")
    printtextanimation("1. Left")
    printtextanimation("2. Right")
    
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        printtextanimation("You encounter a dead end. You're caught. Game Over.")
        game_over()
    elif choice == "2":
        printtextanimation("The tunnel leads to a hidden exit. You're free!")
        freedom()
    else:
        printtextanimation("Invalid choice. Try again.")
        secret_passage()

def infirmary_room():
    printtextanimation("\nYou sneak into the infirmary, hoping to find a way out.")
    time.sleep(1)
    printtextanimation("You see a window slightly ajar and a medicine cabinet.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Climb out the window")
    printtextanimation("2. Search the cabinet for useful items")
    printtextanimation("3. sneak out into a corridor")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("You successfully escape through the window!")
        freedom()
    elif choice == "2":
        printtextanimation("You find nothing useful and are caught. Game Over.")
        game_over()
    elif choice == "3":
        printtextanimation("You wait too long and are discovered. Game Over.")
        library_room()
    else:
        printtextanimation("Invalid choice. Try again.")
        infirmary_room()

def workshop_room():
    printtextanimation("\nYou enter the workshop, filled with tools and materials.")
    time.sleep(1)
    printtextanimation("You could potentially craft something useful.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Create a makeshift weapon")
    printtextanimation("2. Build a tool to aid your escape")
    printtextanimation("3. try a door in the right corner of the room")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("The weapon is discovered during a search. Game Over.")
        game_over()
    elif choice == "2":
        printtextanimation("You craft a tool and use it to escape!")
        freedom()
    elif choice == "3":
        gym_room()
    else:
        printtextanimation("Invalid choice. Try again.")
        workshop_room()

def cafeteria_room():
    printtextanimation("\nYou find yourself in the cafeteria, bustling with activity.")
    time.sleep(1)
    printtextanimation("You notice a door marked 'Staff Only'.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Enter the staff door")
    printtextanimation("2. Blend in with the crowd")
    printtextanimation("3. Cause a distraction and leave thrue a door")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("The staff door leads to a service corridor. You're free!")
        freedom()
    elif choice == "2":
        printtextanimation("You're recognized and caught. Game Over.")
        game_over()
    elif choice == "3":
        chapel_room()
    else:
        printtextanimation("Invalid choice. Try again.")
        cafeteria_room()

def laundry_room():
    printtextanimation("\nDisguised as a kitchen worker, you make your way to the laundry room.")
    time.sleep(1)
    printtextanimation("You see an opportunity to escape through the laundry chute.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Slide down the laundry chute")
    printtextanimation("2. Hide in a laundry cart")
    printtextanimation("3. Try to blend in with the laundry workers")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("The chute leads to a dead end. You're discovered and caught. Game Over.")
        game_over()
    elif choice == "2":
        freedom()
    elif choice == "3":
        printtextanimation("A supervisor notices you're not supposed to be there. You're caught. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        laundry_room()


def gym_room():
    printtextanimation("\nYou enter the prison gym, filled with equipment and a few inmates.")
    time.sleep(1)
    printtextanimation("You notice a vent that could lead to freedom.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Climb into the vent")
    printtextanimation("2. Challenge an inmate to a fight")
    printtextanimation("3. Look for another exit")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("The vent leads to the outside. You're free!")
        freedom()
    elif choice == "2":
        printtextanimation("The fight attracts guards. You're caught. Game Over.")
        game_over()
    elif choice == "3":
        printtextanimation("You find a hidden door leading outside!")
        freedom()
    else:
        printtextanimation("Invalid choice. Try again.")
        gym_room()

def chapel_room():
    printtextanimation("\nYou find yourself in the prison chapel, a quiet and serene place.")
    time.sleep(1)
    printtextanimation("You notice a trapdoor under the altar.")
    printtextanimation("\nWhat do you do?")
    printtextanimation("1. Open the trapdoor")
    printtextanimation("2. Pray for guidance")
    printtextanimation("3. Search for another exit")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        printtextanimation("The trapdoor leads to a tunnel. You're free!")
        freedom()
    elif choice == "2":
        printtextanimation("You feel a sense of peace, but no escape. Game Over.")
        game_over()
    elif choice == "3":
        printtextanimation("You find a hidden passage leading outside!")
        freedom()
    else:
        printtextanimation("Invalid choice. Try again.")
        chapel_room()

# Start the game
title()
home_screen()
start()