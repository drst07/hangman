import random

word_list = ['mango','watermelon','orange','kiwi','strawberry']

print(word_list)

word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess_in_word_list = list(filter(lambda x: guess.lower() in x, word_list))
    if len(guess_in_word_list )!=0:
        print( f'Good guess! {guess} is in the word.')
    else:
        print("Sorry, {guess} is not in the word. Try again.")
        ask_for_input()
    

def ask_for_input():
        while True:  
            guess = input("Enter a single letter: ")
            if len(guess)==1 and  guess.isalpha():
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        check_guess(guess)

ask_for_input()

            
       
   