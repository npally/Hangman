"""Create a hangman game"""
import random



def letter_check(x):
    global word
    if x in word:
        print(f"Yes, letter {x} is in the word")
    else:
        print("Sorry. That letter is not in the word.")

def word_check():
    global gl, word, blank
    for letter in word:
        if letter in gl:
            print(letter, end=" ")
        else:
            print(blank, end=" ")

fin = open('wordlist.txt', 'r')
words = [line.strip() for line in fin]
word = random.choice(words)
blank = '_'
guesses = 0
letters = len(word)
clue = len(word) * '_'
gl = []

print(f"\nWelcome to Hangman by Kilgore Trout! Coming to you from another dimension.\nYou will have 10 guesses to find the word.\nYour word has {letters} letters.")
print(clue)

while guesses <= 9:
    s = input("\nEnter your letter\n>> ")
    if s in word:
        gl.append(s)
    guesses += 1
    letter_check(s)
    word_check()
    print("\nYou have", 10 - guesses,"guesses left.")

    wchars = set(word)
    wchars = list(wchars)
    wchars.sort()
    wchars = ''.join(wchars)
    gl.sort()

    if wchars == ''.join(gl):
         print("Congratulations. You win!!!")
         raise SystemExit


print('Sorry mate you have run out of guesses. You lose.')
print(f'Your word was {word}')
