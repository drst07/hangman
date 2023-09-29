import random

class Hangman:
    """
    Represents a Hangman game.

    Args:
        word_list (list): A list of words to choose from for the game.
        num_lives (int, optional): The number of lives (chances) the player has. Default is 5.

    Attributes:
        word_list (list): A list of words for the game.
        word (str): The selected word to guess.
        word_guessed (list): A list representing the current state of the word being guessed.
        num_letters (int): The number of unique letters in the selected word.
        num_lives (int): The number of lives (chances) the player has.
        list_of_guesses (list): A list to keep track of guessed letters.

    Methods:
        check_guess(guess): Checks if a guessed letter is correct and updates the game state.
        ask_for_input(): Prompts the player to enter a letter guess.

    """
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(0, len(self.word))]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check if a guessed letter is correct and update the game state.

        Args:
            guess (str): The letter guessed by the player.

        Returns:
            bool: True if the guessed letter is in the word, False otherwise.
        """
        print(self.word, self.num_letters)
        if guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(0, len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1  # Update the number of letters left to guess
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

        return guess.lower() in self.word

    def ask_for_input(self):
            """
            Prompt the player to enter a letter guess.
            """
            guess = input("Guess a letter:")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if self.check_guess(guess):
                    self.list_of_guesses.append(guess)



def play_game(word_list):
    """
    Play a game of Hangman.

    Args:
        word_list (list): A list of words to choose from for the game.
    """
    num_lives = 3
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters == 0:  # Check if all letters have been guessed
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()


play_game(['mango','watermelon','orange','kiwi','strawberry'])
