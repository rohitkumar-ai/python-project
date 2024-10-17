class ChessPiece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup()

    def setup(self):
        for i in range(8):
            self.board[1][i] = ChessPiece("P", "white")
            self.board[6][i] = ChessPiece("P", "black")

    def display(self):
        for row in self.board:
            print(" ".join([piece.name if piece else "." for piece in row]))

def main():
    board = Board()
    turn = "white"

    while True:
        board.display()
        print(f"{turn}'s turn.")
        src_row = int(input("Enter source row (0-7): "))
        src_col = int(input("Enter source column (0-7): "))
        dest_row = int(input("Enter destination row (0-7): "))
        dest_col = int(input("Enter destination column (0-7): "))

        # Simplified move: only allow moving pawns forward
        if turn == "white" and board.board[src_row][src_col] and board.board[src_row][src_col].color == "white":
            if dest_row == src_row + 1 and dest_col == src_col and not board.board[dest_row][dest_col]:
                board.board[dest_row][dest_col] = board.board[src_row][src_col]
                board.board[src_row][src_col] = None
                turn = "black"
            else:
                print("Invalid move!")
        elif turn == "black" and board.board[src_row][src_col] and board.board[src_row][src_col].color == "black":
            if dest_row == src_row - 1 and dest_col == src_col and not board.board[dest_row][dest_col]:
                board.board[dest_row][dest_col] = board.board[src_row][src_col]
                board.board[src_row][src_col] = None
                turn = "white"
            else:
                print("Invalid move!")

if __name__ == "__main__":
    main()
