# Hangman Game

This is a simple implementation of the classic Hangman game in Python.

## How to Play

1. You'll be presented with a hidden word, and your goal is to guess the letters in the word.

2. You have a limited number of lives (default is 5) to guess the word. Each incorrect guess results in losing a life.

3. Enter a letter as your guess. If the letter is in the word, it will be revealed. If not, you'll lose a life.

4. Keep guessing letters until you either guess the word correctly or run out of lives.

## Getting Started

To play the Hangman game, follow these steps:

- Clone this repository to your local machine:

```bash
git clone https://github.com/drst07/hangman.git
```

- Navigate to the project directory:

```bash
cd hangman
```

- Run the game:

```bash
python hangman.py
```

- Follow the on-screen instructions to make your guesses.

## Customization

You can customize the game by modifying the word list in the play_game() method:

```bash
play_game(['mango','watermelon','orange','kiwi','strawberry'])
```

Feel free to add your own words to make the game more interesting.

