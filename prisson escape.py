import time
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printtextanimation(text, animation_speed=0.03
,):
    repetitions=1
    for _ in range(repetitions):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(animation_speed)
        print()


def title():
    printtextanimation("""  
  _____      _                       ____                 _        
 |  __ \    (_)                     |  _ \               | |       
 | |__) | __ _ ___ ___  ___  _ __   | |_) |_ __ ___  __ _| | _____ 
 |  ___/ '__| / __/ __|/ _ \| '_ \  |  _ <| '__/ _ \/ _` | |/ / _ |
 | |   | |  | \__ \__ \ (_) | | | | | |_) | | |  __/ (_| |   <  __/
 |_|   |_|  |_|___/___/\___/|_| |_| |____/|_|  \___|\__,_|_|\_\___|
                                                                   """, animation_speed=0.0001)

def start():
    time.sleep(1)
    printtextanimation("\n Press enter to continue")
    x=input ()
    if x=="":
        cls()
        print("\n")
        printtextanimation("PRISON BREAK")
        time.sleep(1)
        print("\n")
        printtextanimation("You'r sentance has been ruled")
        time.sleep(1)
        print("\n")
        printtextanimation("You have ben taken to the jail cell")
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
        x = input()
        if x=="":
            cls()
            first_cell()
        else:
            printtextanimation("Invalid")
            cls()
            start()
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
        printtextanimation("You end up in a dead end and have to turn back. You're caught by guards. Game Over.")
        game_over()
    elif choice == "3":
        guard_room()
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
        printtextanimation("You successfully knock out the guard, but the commotion attracts attention. You're caught. Game Over.")
        game_over()
    elif choice == "3":
        sick_escape()
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
        printtextanimation("You're discovered when a cook tries to use the pot. Game Over.")
        game_over()
    elif choice == "2":
        laundry_room()
    elif choice == "3":
        yard_escape()
    else:
        printtextanimation("Invalid choice. Try again.")
        kitchen_room()

def sick_escape():
    printtextanimation("\nThe guard believes you're sick and opens the cell to help.")
    time.sleep(1)
    printtextanimation("You now have an opportunity to escape.")
    printtextanimation("\nWhat's your next move?")
    printtextanimation("1. Overpower the guard and take his uniform")
    printtextanimation("2. Make a run for it down the corridor")
    printtextanimation("3. Pretend to faint and wait for more opportunities")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        guard_disguise()
    elif choice == "2":
        printtextanimation("You're quickly caught by other guards in the corridor. Game Over.")
        game_over()
    elif choice == "3":
        printtextanimation("The guard calls for medical help, ruining your escape plan. Game Over.")
        game_over()
    else:
        printtextanimation("Invalid choice. Try again.")
        sick_escape()

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
    printtextanimation("\nYou're now disguised as a guard. You blend in, but you're not out yet.")
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
    printtextanimation("\nGame Over! Better luck next time.")
    printtextanimation("Do you want to play again? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        cls()
        first_cell()
    else:
        printtextanimation("Thanks for playing Prison Break!")
        exit()


title()

start()



