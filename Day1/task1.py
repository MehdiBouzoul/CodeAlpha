import random
L = ["dog", "cat", "codealpha", "juice", "joboffer"]

word = random.choice(L)
guess = 0
guessed_letters = list()
while guess < 6 and len(guessed_letters) != len(word):
  for letter in word:
    if letter in guessed_letters:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print("Guess a letter : ")
  guessed_letter = input()
  if guessed_letter in word:
    guessed_letters += guessed_letter
  guess +=1
  
if  len(guessed_letters) == len(word):
  print("You guessed the word with", guess, "guesses!")
else:
  print("You ran out of guesses. The word was", word)
