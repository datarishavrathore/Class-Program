import random

choices = ["rock", "paper", "scissors"]


user_score = 0
system_score = 0

for i in range(1, 4):
    system = random.choice(choices)
    user = input("Enter your choice (rock/paper/scissors): ").lower()

    print(f"\nRound {i}✌️ Start ")
    print("Your Choice   :", user)
    print("System Choice :", system)

    if user == system:
        print("Result : Draw")
    elif (user == "rock" and system == "scissors") or \
         (user == "paper" and system == "rock") or \
         (user == "scissors" and system == "paper"):
        print("Result : You Win")
        user_score += 1
    else:
        print("Result : System Wins")
        system_score += 1

print("\n------ Final Score ------")
print("Your Score   :", user_score)
print("System Score :", system_score)


if user_score > system_score:
    print("🎉 You won the game!")
elif system_score > user_score:
    print(" System won the game!")
else:
    print("🤦‍♂️ Game Draw!")