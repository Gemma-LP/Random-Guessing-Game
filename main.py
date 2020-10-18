import random

number = random.randint(1,50)
print("I am thinking of a number between 1 and 50. You have 6 chances to guess the correct numer.")
tries = 0

while tries <6:
  guess = int(input("Take a guess: "))
  tries = tries + 1
  if guess < number:
    print("Your guess is too low.")
  if guess > number:
    print("Your guess is too high.")
  if guess == number:
    print("Well done! You guessed the correct number!")
    break
else:
  print("Oops, you ran out of guesses. Better luck next time!")