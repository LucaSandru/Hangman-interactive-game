import random
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

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
list_word1 = ['goal', 'cure', 'idea', 'wrong', 'correct', 'mouse', 'bat', 'eyes', 'cake', 'wrap', 'rat', 'lying', 'fact', 'moon', 'sun', 'city', 'town', 'school', 'plane', 'problem', 'solve' , 'car', 'apple', 'absurd','alright', 'basket', 'book', 'puzzle', 'height', 'hair', 'house', 'magic', 'fixable', 'jelly', 'fish', 'work', 'joke', 'juice', 'lucky', 'bad', 'club', 'ball', 'bill', 'quiz',  'wave', ]
list_word2 = ['dialog', 'basketball', 'baseball', 'chemistry', 'phisical', 'football', 'faculty', 'bachelor', 'airplane', 'antigel', 'ghost', 'zodiac', 'zombie', 'jogging', 'voodoo','axiom', 'bikini', 'goalkeeper', 'blitz', 'axiom', 'develop', 'giraffe', 'trivial', 'nightclub', 'cycle', 'hydrogen', 'curacao', 'duplex', 'equip', 'galaxy', 'haiku', 'jackpot', 'successfull', 'jigsaw', 'matrix', 'nightclub', 'oxygen', 'injury', 'queue',  'rhythm', 'strength', 'subway', 'transplant', 'vodka', 'zigzag']
list_word3 = ['numbskull', 'kilogram', 'buckaroo', 'supermarket', 'kiosk', 'wellspring', 'pshaw', 'analogysm', 'jawbreaker', 'schnapps', 'pneumonia', 'voyeurism', 'unknown', 'thumbscrew', 'tombstone', 'stonehange', 'fluffiness', 'razzmatazz', 'apologiesing', 'pancake', 'terminology', 'astrophisical', 'kilobyte', 'plancton', 'xenophobic', 'perseverence', 'presumption', 'quite', 'foxglove', 'megahertz', 'buffalo', 'cryptocurrency', 'pinneapple', 'fishhook', 'zigzagging', 'fjord', 'fuchsia', 'arrogance', 'jiujitsu', 'knapsack', 'pixel', 'headache', 'syndrome', 'anticonceptionnal', 'zigzagging']
x = input("Choose a difficulty: \n1.Easy\n2.Medium\n3.Hard\n")
if x == '1':
    chosen_word = random.choice(list_word1)
elif x == '2':
    chosen_word = random.choice(list_word2)
else: chosen_word = random.choice(list_word3)
print(logo)
display = []
for i in range(len(chosen_word)):
    display.append("_")
lives = 6
ok = 1
tried = ""
print(" ".join(display))
while ("_" in display and ok == 1):
    guess = input("Choose a letter: ")
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        tried += guess
        tried +=" "
        print(f"Already used letters: {tried}")
        print(stages[lives])
        if lives == 0:
            print(f"You died! The word was '{chosen_word}'")
            ok = 0
            break
    print(" ".join(display))
if ok == 1:
    print("Gongratulations! You won!")
