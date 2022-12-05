from random import choice

def game_command():
  tries = 6
  wordlist=('hot', 'got', 'bought', 'fought', 'lot', 'cot')
  word=choice(wordlist)
  word_letters=list(word)
  print(word_letters) ##uncomment if you wanna cheat##
  letters_found=[]
  disp_let=[]
  while tries != 0:
    letter=input("what letter do you want to guess?")
    letter=letter.lower()
    if letter in disp_let:
      print("You already found this letter!")
    elif letter in word_letters:  
      print("You got a letter!")
      index=word_letters.index(letter)
      disp_let += word_letters[index]
      print(f"You have these letter's found: {disp_let}")     
      print("letter's wont be in order")
      letters_found.append(letter)
      word_letters.remove(letter)
      length=len(word_letters)
      if length == 0:
        print("You Win!")
        break
    elif letter not in word_letters:
      print("You did not get a letter")
      tries -= 1
      print(f"You have {tries} lives")
  if tries == 0:
    print("You Lose")
    print(f"you found these letters: {letters_found}, the word was   {word}")
