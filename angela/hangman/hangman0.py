word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)
temp_word = chosen_word
output = "_" * len(chosen_word)
print(chosen_word)
while True:
    print(output)
    guess = input("Guess a letter: ").lower()
    index = temp_word.find(guess)
    if index >= 0:
        output = output[:index] + guess[0] + output[(index + 1) :]
        temp_word = temp_word[:index] + " " + temp_word[(index + 1) :]

        if output == chosen_word:
            print("The word is:", output)
            print("Correct!")
            break
