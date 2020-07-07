# For randomly choosing a word;
import random 
# For error handling;
import sys
# Adding words;
from words import word_list


# sample word_list
# word_list = ['apple', 'banana', 'cat', 'dog', 'elephant', 'frog'] 

# Welcome message
print('~~~~~~~~~~~~~~~~~~~')
print("Let's play hangman!")
print('~~~~~~~~~~~~~~~~~~~')
print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """)


def get_word():
    # Better Implementation
    return random.choice(word_list).upper()


def play(word):

    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(word_completion)
    print("\n")

    while not guessed and tries > 0:

        guess = input("Please guess a letter or word: ").upper()

        # if the user's guess is a letter and is from alphabets;
        if len(guess) == 1 and guess.isalpha():

            if guess in guessed_letters:
                print("You already guessed the letter", guess  +".")

            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)

            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)

                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess

                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        # if the user's guess is a word and is equal to random's word's length;
        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessed_words:
                print("You already guessed the word", guess)

            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                word_completion = word


        else:
            print("Not a valid guess.")

        
        print('---------------')
        print(word_completion)
        print('---------------')
        print("\n")
        print("You have", tries, "guesses left.")
        print("\n")


    if guessed:
        print("CONGRATULATIONS! You guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was", word + ". Maybe next time!")




def main():
    # getting a random word from `get_word` function;
    word = get_word()

    # Starting the game;
    play(word)


    while input("\nPlay Again? (Y/N): ").upper() == "Y":
        # loop for infinite game play;
        word = get_word()
        play(word)
    print('~~~~~~~~~')
    print("THE END!")
    print('~~~~~~~~~')


if __name__ == "__main__":
    main()