from random import choice
from variables import *

def game_command():
  word=choice(["word_list"])
  word_letters=list(word)
  length=len(word_letters)
  num_lives=6
  print({["indent"]}+ "\n Hello "+ {["name"]} +" we are playing a game of hang man \n I'm thinking of a" + length + "letter word and you gotta guess it. \n" + {["indent"]})
  
  for i in range(len(["word"])):
    ["undscore"].append(["dash"])
  while ["num_lives"] != 0:
    letter=input("What letter do you want to guess? ")
    letter=letter.lower()
    if (letter in ["disp_let"]) and (letter not in word_letters):
      print("You already found this letter!")
    elif letter in ["word_letters"]:
      print("You got a letter!")
      i=["word_letters"].index(["letter"])
      disp_let=[]
      disp_let += word_letters[i]
      ["undscore"][i]=letter
      # if letter in word_letters >1:
        # pass
      print("You have these letter's found:"+ ["undscore"])     
      print("Letter's wont be in order")
      ["letters_found"].append(letter)
      word_letters.remove(letter)
      length=len(word_letters)
      if length == 0:
        print("You Win!")
        break
    elif letter not in word_letters:
      print("You did not get a letter")  
      num_lives -= 1
      print("You have"+ ["num_lives"]+"lives")
  if num_lives == 0:
    print("You Lose")
    print("You found these letters:"+ {["letters_found"]}+", the word was"+ {word})
