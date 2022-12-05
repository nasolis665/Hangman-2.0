from random import choice

def game_command():
  num_lives = 6
  word_list=('hot', 'got', 'bought', 'fought', 'lot', 'cot')
  word=choice(word_list)
  word_letters=list(word)
  print(word_letters) ##uncomment if you wanna cheat##
  letters_found=[]
  disp_let=[]
  length=len(word_letters)
  name=input("What is your name? ")
  print(f"Hello {name} we are playing a game of hang man I'm\n thinking of a {length} letter word and you gotta guess it")
  undscore=[]
  dash='_'
  for i in range(len(word)):
    undscore.append(dash)
  while num_lives != 0:
    letter=input("what letter do you want to guess? ")
    letter=letter.lower()
    if (letter in disp_let) and (letter not in word_letters):
      print("You already found this letter!")
    elif letter in word_letters:
      print("You got a letter!")
      i=word_letters.index(letter)
      disp_let += word_letters[i]
      undscore=undscore[:i]+[letter]+undscore[i+1:]
      if letter in word_letters >1:
        pass
      print(f"You have these letter's found: {undscore}")     
      print("letter's wont be in order")
      letters_found.append(letter)
      word_letters.remove(letter)
      length=len(word_letters)
      if length == 0:
        print("You Win!")
        break
    elif letter not in word_letters:
      print("You did not get a letter")
      num_lives -= 1
      print(f"You have {num_lives} lives")
  if num_lives == 0:
    print("You Lose")
    print(f"you found these letters: {letters_found}, the word was {word}")
