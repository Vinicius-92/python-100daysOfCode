import random

# Step 3
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(len(chosen_word)):
    display += "_"

# Use a while loop to let the user guess again. The loop should only stop once
#  the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
#  Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

print(display)
