print("\t\t\t\t\t***** Rock,Paper,Scissor GAME *****")


import random

list = ["r", "p", "s"]
total_chances = int(input("How many rounds you want to play:\n"))
computer = 0
user = 0
n = 1
print("(Here 'r' stands for Rock, 'p' stands for paper, 's' stands for scissor)\n")

while (n <= total_chances):
    comp = random.choice(list)
    your = input("Enter you choice(r/p/s):\n")
    if your == comp:
        print("Your choice is similar to computer, so no one win \ntry again!!\n")
    elif your == "p" and comp == "r":
        user = user + 1
        print(f"Computer's choice is {comp} and your's {your}")
        print(f"you win and points are \nyour => {user} \t\t\t computer => {computer}\n")
    elif your == "s" and comp == "r":
        computer = computer + 1
        print(f"Computer's choice is {comp} and your's {your}")
        print(f"Computer win and points are \nyour => {user} \t\t\t computer => {computer}\n")
    elif your == "r" and comp == "p":
        computer = computer + 1
        print(f"Computer's choice is {comp} and your's {your}")
        print(f"Computer win and points are \nyour => {user} \t\t\t computer => {computer}\n")
    elif your == "s" and comp == "p":
        user = user + 1
        print(f"Computer's choice is {comp} and your's {your}")
        print(f"You win and points are \nyour => {user} \t\t\t computer => {computer}\n")
    elif your == "p" and comp == "s":
        computer = computer + 1
        print(f"Computer's choice is {comp} and your's {your}")
        print(f"Computer win and points are \nyour => {user} \t\t\t computer => {computer}\n")
    elif your == "r" and comp == "s":
        user = user + 1
        print(f"Computer's choice is {comp} and your's {your}")
        print(f"You win and points are \nyour => {user} \t\t\t computer => {computer}\n")
    else:
        print("Wrong input \nTry again !!\n")

    print(total_chances - n, "chances are left\n")
    n = n + 1

print("\nFinal result is: \n")

if user > computer:
    print(f"Congrats!! you Won!! 🥳 🎉 and final scores are: \nyour score ==> {user} \t\t\t computer' score ==> {computer}\\n")
elif computer > user:
    print(f"Sorry!! But you lose!! 😞😞 \nand final scores are: \nyour score ==> {user} \t\t\t computer's score ==> {computer} \nBut don't loose your hurt just play again !!\n\n")
else:
     print("Your points are equal to computer's point\nyour score ==>", user, "\t\t\t computer's score ==>",computer, "\n\n")

ext=input("Press Enter to exit")
