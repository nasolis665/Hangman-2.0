from random import choice
from variables import *
from word import *
word = choose_word()


def game_command(word, test):

  word_letters = list(word)
  wl=word_letters
  length = len(word_letters)
  num_lives = 6
  disp_let = []
  undscore=["_" for letter in word_letters]
  times_guessed = 0
  print(
    str(test["indent"]) + "\nHello " + str(test["name"]) + " we are playing a game of hang man I'm thinking of a " + str(length) + " letter word and you gotta guess it. \n" + str(test["indent"]))

  while num_lives != 0:
    letter = input(
      str(test["indent"]) + "\nWhat letter do you want to guess? ")
    letter = letter.lower()
    if (letter in undscore) and (letter not in word_letters):
      print(str(test["indent"]) + "\nYou already found this letter! ")
    elif letter in word_letters:
      print(str(test["indent"]) + "\nYou got a letter!")
      indices=[i for i, x in enumerate(word_letters) if x == letter]
      for i in indices:
        undscore[i]=letter
      i = word_letters.index(letter)
      disp_let += word_letters[i]
      undscore[i] = letter
      print("You have these letter's found: " + str(undscore))
      test["letters_found"].append(letter)
      if undscore==word_letters:
        print("You Win!")
        break
    elif letter not in word_letters:
      print("You did not get a letter. ")
      num_lives -= 1
      times_guessed += 1
      print(hangman_states[times_guessed])
      print("You have " + str(num_lives) + " lives.")
  if num_lives == 0:
    print("You lose.")
    print("You found these letters:" + str(test["letters_found"]) + ", the word was " + str(word))