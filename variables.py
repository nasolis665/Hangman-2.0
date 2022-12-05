from random import choice
def var():
  tries = 6
  wordlist=('hot', 'got', 'bought', 'fought', 'lot', 'cot')
  word=choice(wordlist)
  word_letters=list(word)
  print(word_letters) ##uncomment if you wanna cheat##
  letters_found=[]
  disp_let=[]