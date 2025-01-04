import random
from hangman.words import word_list
from hangman.art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(f"Pssst, the solution is {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"


correct_letters = []
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
    print(f"You lives remaining: {lives}")
    print("")

    # for letter in chosen_word:
    #     if len(guess) > 0 and letter == guess[0]:
    #         display += letter
    #         correct_letters.append(letter)
    #     elif letter in correct_letters:
    #         display += letter
    #     else:
    #         display += "_"

    #     if display == chosen_word:
    #         print("You win")
    #         game_over = True
    # print(display)

# print("\n********************")
# print("The word is:", chosen_word)
# print("Correct!")
# print("********************")
