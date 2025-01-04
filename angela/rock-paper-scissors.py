beat_by = [1, 2, 0]
labels = ["ROCK", "PAPER", "SCISSORS"]

user_choice = int(
    input(
        """
What do you choose?
0 = Rock
1 = Paper
2 = Scissors
: """
    )
)
if user_choice == "":
    exit
computer_choice = random.randint(0, 2)
print(f"YOU: {labels[user_choice]} vs COMPUTER: {labels[computer_choice]}")
if user_choice == computer_choice:
    print("Draw!")
elif beat_by[user_choice] == computer_choice:
    print("You lose!")
else:
    print("You win!")
print("")
