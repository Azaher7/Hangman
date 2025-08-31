import random

def main():
    greeting = greet_user(input("Select your username: "))
    print(greeting)
    word = generate_word(input("Select your difficulty(E|M|H): "))
    hangman(word)


def greet_user(user):
    while True:
        if user.isalpha() and len(user) >= 3 and len(user) <= 8:
            return f"Hello " + user + ", welcome to hangman"
        else:
            user = input("Username must be between 3 and 8 characters and must contain no special characters or digits, Please try again: ")
            if user.isalpha() and len(user) >= 3 and len(user) <= 8:
                return f"Hello " + user + ", welcome to hangman"


def generate_word(difficulty):
    if difficulty.upper() == "E":
        words = ["English", "French", "Spanish", "German", "Arabic", "Cat", "Dog", "Bear", "Lion", "Elephant", "Tiger"]
        selected_word = random.choice(words)
        return selected_word.lower()

    elif difficulty.upper() == "M":
        words = ["Antartica", "Australia", "Africa", "Asia", "Europe", "America"]
        selected_word = random.choice(words)
        return selected_word.lower()

    elif difficulty.upper() == "H":
        words = ["Sphynx", "Espionage", "Witchcraft", "Rhythm", "Jazz", "Canberra", "Johannesburg"]
        selected_word = random.choice(words)
        return selected_word.lower()

    else:
        raise NameError("Invalid difficulty, please select a valid difficulty level(E|M|H) and try again")
        


def hangman(word):
    if word.isalpha() and len(word) >= 3 and len(word) <= 15:
        hangman = [
            r"""
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
            r"""
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
            r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
            r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
            r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
            r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
            r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """,
        ]

        list_word = list(word)
        blank_spaces = ("_") * len(word)
        list_blank_spaces = list(blank_spaces)

        blank_spaces_display = "  ".join(list_blank_spaces)

        incorrect_guess = 1
        correct_guess = 0
        missed_letters = []
        used_letters = []

        print(hangman[incorrect_guess - 1])
        print(blank_spaces_display)

        game = True

        while game:
            guess = input("\nguess a letter\n")
            if len(guess) == 1 and guess.isalpha():
                if guess.lower() in word:
                    if guess.lower() not in used_letters:
                        used_letters.append(guess)
                        print("\nMissed letters: " + " ".join(missed_letters).upper())
                        print(hangman[incorrect_guess - 1])

                        index_replacement = [index for index, character in enumerate(list_word) if guess.lower() == character]
                        for index in index_replacement:
                            correct_guess += 1

                            if correct_guess < len(word):
                                list_blank_spaces[index] = guess
                                string = " ".join(list_blank_spaces)

                            elif correct_guess >= len(word):
                                game = False
                                list_blank_spaces[index] = guess
                                string = " ".join(list_blank_spaces)
                                print("\ncongratulations, you have completed the challenge\n")
                                break

                        print(string)

                    else:
                        print("\nMissed letters: " + " ".join(missed_letters).upper())
                        print(hangman[incorrect_guess - 1])
                        print("\nLetter was already used, please try again\n")
                        print(string)

                elif guess.lower() not in word:
                    if guess.lower() not in missed_letters:
                        missed_letters.append(guess)
                        print("\nMissed letters: " + " ".join(missed_letters).upper())
                        incorrect_guess += 1

                        if incorrect_guess < len(hangman):
                            print(hangman[incorrect_guess - 1])
                            string = " ".join(list_blank_spaces)
                            print(string)

                        elif incorrect_guess >= len(hangman):
                            game = False
                            print(hangman[incorrect_guess - 1])
                            string = " ".join(list_blank_spaces)
                            print(string)
                            print("\nGAME OVER\n")
                            print("The word is " + word)
                            break

                    else:
                        print("\nMissed letters: " + " ".join(missed_letters).upper())
                        print(hangman[incorrect_guess - 1])
                        print("\nLetter was already used, please try again\n")
                        print(string)

            else:
                print("\nMissed letters: " + " ".join(missed_letters).upper())
                print(hangman[incorrect_guess - 1])
                print("\ninvalid guess, please make sure that that your guess is a letter\n")
                print(string)

    else:
        raise ValueError("invalid")


if __name__ == "__main__":
    main()
