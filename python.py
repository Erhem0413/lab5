import random

class Puzzle:
    """
    Represents a single-class puzzle game.
    """

    def __init__(self, size):
        """
        Initializes the game with a scrambled list of numbers.
        """
        self.size = size
        self.tiles = list(range(1, size * size + 1))
        random.shuffle(self.tiles)
        self.empty_tile_index = self.tiles.index(0)  # Position of the empty tile

    def print_board(self):
        """
        Prints the current state of the puzzle board.
        """
        for i in range(self.size):
            for j in range(self.size):
                tile = self.tiles[i * self.size + j]
                print(tile if tile else " ", end=" ")
            print()

    def is_valid_move(self, move):
        """
        Checks if the requested move (up, down, left, right) is valid.
        """
        empty_row, empty_col = divmod(self.empty_tile_index, self.size)
        row, col = move
        return (abs(row - empty_row) + abs(col - empty_col)) == 1

    def make_move(self, move):
        """
        Swaps the empty tile with the tile in the specified direction (if valid).
        """
        if not self.is_valid_move(move):
            return

        empty_row, empty_col = divmod(self.empty_tile_index, self.size)
        row, col = move
        new_empty_tile_index = empty_row * self.size + col
        self.tiles[empty_tile_index], self.tiles[new_empty_tile_index] = self.tiles[new_empty_tile_index], self.tiles[empty_tile_index]
        self.empty_tile_index = new_empty_tile_index

    def is_solved(self):
        """
        Checks if the puzzle is solved (tiles in order).
        """
        return self.tiles == list(range(1, self.size * size + 1)) + [0]

# Example usage
puzzle = Puzzle(3)  # Size of the puzzle (3x3)

while not puzzle.is_solved():
    puzzle.print_board()
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

    puzzle.make_move(move)

puzzle.print_board()
print("Congratulations! You solved the puzzle.")