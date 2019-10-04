import random

print("Welcome to Shwivl's Guessing Game!")
a = random.randint(0,100)


while True:
  print("")
  userGuess = int(input("Enter your guessed no. b/w 0-100: "))
  if userGuess < a:
    print("")
    print("Higher")

  elif userGuess > a:
    print("")
    print("Lower")

  else:
    print("")
    print("You guessed correctly!")
    print(" ")
    print('Would you like to play again? Type "y" or "n."')
    playagain = str(input(''))
    print(" ")
    if playagain == str('y'):
      continue
    elif playagain == str('n'):
      break
    else:
      print("Invalid input. Assuming n, closing program.\n")
      break

