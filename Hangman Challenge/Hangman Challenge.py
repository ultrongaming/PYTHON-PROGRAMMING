import random

# List of words for the game
WORDS = ["python", "java", "kotlin", "javascript", "hangman", "programming"]

# Function to display the current state of the game
def display_game_state(word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

# Function to run the hangman game
def play_hangman():
    word = random.choice(WORDS)  # Select a random word
    guessed_letters = set()      # Letters guessed by the player
    incorrect_guesses = 0
    max_incorrect_guesses = 6    # Maximum number of incorrect guesses allowed

    print("Welcome to Hangman!")
    
    while True:
        display_game_state(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")

        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word '{word}'. You win!")
            break

        # Check if the player has reached the maximum number of incorrect guesses
        if incorrect_guesses >= max_incorrect_guesses:
            print(f"Game Over! The word was '{word}'. Better luck next time!")
            break

# Start the game
play_hangman()