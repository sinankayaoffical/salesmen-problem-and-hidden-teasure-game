import random

def hidden_treasure_game():
  """
  A game that uses simple search and binary search to find a hidden treasure.
  """

  # Choose a random location for the treasure
  treasure_location = random.randint(0, 100)

  # Welcome message for the user
  print("Welcome detective! Put on your thinking cap and get ready to crack the case.")
  print("We need to find the hidden treasure, but its location is a secret number between 0 and 100.")
  print("You only have 5 questions to narrow down the search.")

  # Track the number of questions remaining
  remaining_questions = 5

  # Ask the first 3 questions using simple search
  for i in range(3):
    remaining_questions -= 1
    if remaining_questions == 0:
      print(f"Last question! Is the treasure number {treasure_location}?")
    else:
      print(f"{remaining_questions} questions left.")
    
    guess = int(input())

    if guess < treasure_location:
      print("The treasure is hidden in a higher number.")
    elif guess > treasure_location:
      print("The treasure is hidden in a lower number.")
    else:
      print("Congratulations! You found the hidden treasure!")
      return

  # Ask the last 2 questions using binary search
  for i in range(2):
    remaining_questions -= 1
    if remaining_questions == 0:
      print(f"Last question! Is the treasure number {treasure_location}?")
    else:
      print(f"{remaining_questions} questions left.")

    print("Is the treasure hidden in the first half of the remaining search space? (yes/no)")
    answer = input()

    if answer.lower() == "yes":
      treasure_location = (treasure_location + 1) // 2
    else:
      treasure_location = (treasure_location + 100) // 2

  # User didn't find the treasure
  print("Oh no! The treasure remains hidden, but you put up a valiant effort.")
  print("Would you like to try again? (yes/no)")
  answer = input()

  if answer.lower() == "yes":
    hidden_treasure_game()

# Start the game
hidden_treasure_game()
