import random
word_list = ["string", "integer", "pull", "push", "markdown", "float", "boolean", "if", "else", "elif"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print("Theme: Python Concepts")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried", guess, "!")
            elif guess not in word:
                print(guess, "Isn't in the word... 😒")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried", guess, "!")
            elif guess != word:
                print(guess, "It's not the word 😂")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Are you a hacker?")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("I'll get you next time Perry the Platypus!!!")
    else:
        print("Haha. YOU LOSE 🤣!!! The word was " + word + ". You're really BAD. Play again 🥱!")

def display_hangman(tries):
    stages = [ """
                         --------
                        |   |
                        |   O
                        |  /|\\
                        |   |
                        |  / \\
                        -
                        """,
                        """                        
                         --------
                        |   |
                        |   O
                        |  /|\\
                        |   |
                        |  / 
                        -
                        """,
                        """                        
                         --------
                        |   |
                        |   O
                        |  /|\\
                        |   |
                        |   
                        -
                        """,
                        """                        
                         --------
                        |   |
                        |   O
                        |  /|
                        |   |
                        |   
                        -
                        """,
                        """                       
                         --------
                        |   |
                        |   O
                        |   |
                        |   |
                        |   
                        -
                        """,
                        """                       
                         --------
                        |   |
                        |   O
                        |  
                        |  
                        |  
                        -
                        """,
                        """                       
                         --------
                        |   |
                        |  
                        |  
                        |   
                        |  
                        -
                        """
    ]
    return stages[tries]
def main():
    word = get_word(word_list)
    play(word)
    while input("If you lost, congrats you hanged a person. If you won then ignore this. Going again? (Y/N)").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()