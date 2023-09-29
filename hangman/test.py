import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(0, len(self.word))]
        self.num_letters = int(len(set(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
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
        # while True:
            guess = input("Guess a letter:")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if self.check_guess(guess):
                    self.list_of_guesses.append(guess)


def play_game(word_list):
    num_lives = 3
    game = Hangman(word_list, num_lives)
    # print("Num_letters: ",game.num_letters)

    while True:
        print("game.num_letters: ",game.num_letters)
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters == 0:  # Check if all letters have been guessed
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()


play_game(['mango','watermelon','orange','kiwi','strawberry'])
