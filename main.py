import random
print("------------Lets play HANGMAN-------------")
print("Total Lives=6")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["apple", "baboon", "camel","mango","tiger","watch","xerox","quit",'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus','neptune',"air","sun","moon","riddle","america","break","smoke","orange","international","network","human"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives=6



display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


  
    print("\n")
    if guess not in chosen_word:
      print("Oopss!!!")
      lives-=1
      if lives==0:
        end_of_game=True
        print("You lose")
          
          
   
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(stages[lives])   
    print(f"lives left = {lives}")