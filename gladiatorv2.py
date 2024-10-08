import random
import time 

dice=[1,2,3,4,5,6,7,8,9,10]

diff = "easy"
lev_violence = 1
gender= "male"

print("loading disk")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("loading done")
time.sleep(1)
print("welcome to swords and flipp flopps")
time.sleep(1)
print("please select difficulty: easy, normal, hard.")

while True:
    a1 = input("Enter difficulty: ")
    if a1 == "easy":
        diff = "easy" 
        print("you have selected easy")
        break 
    elif a1 == "normal":
        diff = "normal" 
        print("you have selected normal")
        break
    elif a1 == "hard":
        diff = "hard"
        print("you have selected hard")
        break
    else:
        print("Invalid option, please select again.")

a2 = input("if you want more info on what changes with the difficulty type 1, if not hit enter: ")

if a2 == "1":
    print("The difficulty changes the stats given to the NPC, increases the chances of you succeeding and lowers theirs.\nLowers the judgment of the public and king.")
else:
    print("Please select level of voilenc 1 if your under the age of 18 and 2 if your over the age of 18")

while True:
    a3=int(input())
    if a3==1:
        lev_violence = 1
        break
    elif a3==2:
        lev_violence = 2
        break
    else:
        print("invalid option, try again")
time.sleep(1)
print("precessing")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("chracter creation screen")
time.sleep(1)
print("please select gender, male ore female")
