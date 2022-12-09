from random import choice

test = {
  "num_lives" : 6,
  "letters_found":[],
  "indent" : "------------------",
  "undscore":[],
  "dash":'_',
  "name":input("What is your name? ")
}

hangman_states = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]