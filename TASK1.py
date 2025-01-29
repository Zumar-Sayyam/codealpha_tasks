import random
def hangman():
    words = ["python", "hangman", "programming", "developer", "software", "engineer", "debugging"]
    word = random.choice(words)
    guessed_word = ["_" for _ in word]
    guessed_letters = set()
    attempts_left = 7
    print("Welcome to Hangman!")

    while attempts_left > 0 and "_" in guessed_word:
        print("\n" + " ".join(guessed_word))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_left -= 1

    if "_" not in guessed_word:
        print(f"\nCongratulations! You've guessed the word: {''.join(guessed_word)}")
    else:
        print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    hangman()

