from random import choice
from variables import *
from word import *

word=choose_word()
def game_command(word, test):  
  
  word_letters=list(word)
  length=len(word_letters) 
  num_lives=6
  disp_let=[]
  times_guessed=0
  print(str(test["indent"]) + "\nHello "+ str(test["name"]) +" we are playing a game of hang man I'm thinking of a " + str(length) + " letter word and you gotta guess it. \n" + str(test["indent"]))
  
  for i in range(len(word)):
    test["undscore"].append(str(test["dash"]))
  while num_lives != 0:
    letter=input(str(test["indent"]) +"\nWhat letter do you want to guess? ")
    letter=letter.lower()
    if (letter in disp_let) and (letter not in word_letters):
      print(str(test["indent"]) +"\nYou already found this letter! ")
    elif letter in word_letters:
      print(str(test["indent"]) +"\nYou got a letter!")
      i=word_letters.index(letter)
      disp_let += word_letters[i]
      test["undscore"][i]=letter
      
      # if letter in word_letters >1:
        # pass
      print("You have these letter's found: "+ str(test["undscore"]))     
      print("Letter's won't be in order. ")
      test["letters_found"].append(letter)
      word_letters.remove(letter)
      length=len(word_letters)
      if length == 0:  
        print("You Win!")
        break
    elif letter not in word_letters:
      print("You did not get a letter. ")  
      num_lives -= 1
      times_guessed+=1
      print(hangman_states[times_guessed])
      print("You have "+ str(num_lives)+" lives.")
  if num_lives == 0:
    print("You lose.")
    print("You found these letters:"+ str(test["letters_found"])+", the word was "+ str(word))