import random

# Define game parameters
SIZE = 3  # Grid size (3x3)
EMPTY_TILE = 0 

def generate_board():
  """
  Generates a random board configuration with the empty tile.
  """
  tiles = list(range(1, SIZE * SIZE + 1))
  random.shuffle(tiles)
  tiles[random.randint(0, len(tiles) - 1)] = EMPTY_TILE
  return tiles

def print_board(board):
  """
  Prints the game board in a user-friendly format.
  """
  for i in range(SIZE):
    for j in range(SIZE):
      tile = board[i * SIZE + j]
      print(tile if tile else " ", end=" ")
    print()

def get_empty_tile_position(board):
  """
  Finds the position of the empty tile on the board.
  """
  for i in range(SIZE):
    for j in range(SIZE):
      if board[i * SIZE + j] == EMPTY_TILE:
        return i, j

def is_valid_move(board, move):
  """
  Checks if the requested move is valid (adjacent to empty tile).
  """
  empty_row, empty_col = get_empty_tile_position(board)
  row, col = move
  return (abs(row - empty_row) + abs(col - empty_col)) == 1

def make_move(board, move):
  """
  Swaps the empty tile with the tile in the specified direction.
  """
  if not is_valid_move(board, move):
    return

  empty_row, empty_col = get_empty_tile_position(board)
  row, col = move
  board[empty_row * SIZE + empty_col], board[row * SIZE + col] = board[row * SIZE + col], board[empty_row * SIZE + empty_col]

def is_game_won(board):
  """
  Checks if the board is in the solved state (tiles in order).
  """
  return board == list(range(1, SIZE * SIZE + 1)) + [EMPTY_TILE]

# Main game loop
def main():
  board = generate_board()
  print("Welcome to the Slide Puzzle!")

  while True:
    print_board(board)
    
    # Get user input
    move = input("Enter your move (e.g., 'w', 'a', 's', 'd'): ")

    # Translate input to move direction
    if move == "w":
      move_row, move_col = -1, 0
    elif move == "a":
      move_row, move_col = 0, -1
    elif move == "s":
      move_row, move_col = 1, 0
    elif move == "d":
      move_row, move_col = 0, 1
    else:
      print("Invalid move. Please try again.")
      continue

    make_move(board, (move_row, move_col))

    if is_game_won(board):
      print_board(board)
      print("Congratulations! You solved the puzzle.")
      break

if _name_ == "_main_":
  main()