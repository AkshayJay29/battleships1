import random

# Define ship size (all ships will be of size 1)
SHIP_SIZE = 1

# Board size
BOARD_SIZE = 5

def create_board():
  """Creates a board filled with empty spaces ('~')."""
  board = []
  for _ in range(BOARD_SIZE):
    board.append(['~'] * BOARD_SIZE)
  return board

def place_ships(board):
  """Randomly places ships (size 1) on the board."""
  for _ in range(SHIP_SIZE):
    ship_row = random.randint(0, BOARD_SIZE - 1)
    ship_col = random.randint(0, BOARD_SIZE - 1)
    while board[ship_row][ship_col] != '~':
      ship_row = random.randint(0, BOARD_SIZE - 1)
      ship_col = random.randint(0, BOARD_SIZE - 1)
    board[ship_row][ship_col] = 'S'

def print_board(board):
  """Prints the board in a user-friendly format."""
  for row in board:
    print(' '.join(row))

def get_player_guess():
  """Gets user input for guess coordinates."""
  while True:
    try:
      row = int(input("Enter a row number (1-5): ")) - 1
      col = int(input("Enter a column number (1-5): ")) - 1
      if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        return row, col
      else:
        print("Invalid coordinates. Please try again.")
    except ValueError:
      print("Invalid input. Please enter integers.")

def play_game():
  """Main game loop."""
  player_board = create_board()
  computer_board = create_board()

  place_ships(player_board)
  place_ships(computer_board)

  player_ships = SHIP_SIZE
  computer_ships = SHIP_SIZE

  while player_ships > 0 and computer_ships > 0:
    print("\nYour board:")
    print_board(player_board)

    print("\nComputer's board:")
    print_board(['~'] * BOARD_SIZE for _ in range(BOARD_SIZE))  # Hide computer ships

    # Player turn
    row, col = get_player_guess()
    if computer_board[row][col] == 'S':
      print("HIT!")
      computer_board[row][col] = 'X'
      computer_ships -= 1
    else:
      print("MISS!")
      player_board[row][col] = 'X'

    # Computer turn (random guess)
    computer_row = random.randint(0, BOARD_SIZE - 1)
    computer_col = random.randint(0, BOARD_SIZE - 1)
    while player_board[computer_row][computer_col] == 'X':
      computer_row = random.randint(0, BOARD_SIZE - 1)
      computer_col = random.randint(0, BOARD_SIZE - 1)
    if player_board[computer_row][computer_col] == 'S':
      print("\nComputer hits your ship!")
      player_board[computer_row][computer_col] = 'X'
      player_ships -= 1

  # Print final boards
  print("\nYour board:")
  print_board(player_board)
  print("\nComputer's board:")
  print_board(computer_board)

  if player_ships > 0:
    print("You win!")
  else:
    print("You lose!")

def main():
  """Welcome message and main menu."""
  print("Welcome to Battleship!")
  while True:
    print("\nMenu:")
    print("1. Instructions")
    print("2. Play Game")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
      print("\nHow to Play:")
      print("  * You and the computer have a 5x5 board.")
      print("  * You both have 1 ship to sink.")
      print("  * Ships are randomly placed on the boards.")
      print("  * On your turn, guess a row and column to fire at.")
