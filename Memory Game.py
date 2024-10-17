import random

def create_board():
    numbers = list(range(1, 9)) * 2  # Create pairs
    random.shuffle(numbers)
    return numbers

def display_board(board, revealed):
    for i in range(len(board)):
        if revealed[i]:
            print(board[i], end=" ")
        else:
            print("?", end=" ")
    print()

def main():
    board = create_board()
    revealed = [False] * len(board)
    attempts = 0

    while not all(revealed):
        display_board(board, revealed)
        choice1 = int(input("Choose the first card (0-15): "))
        choice2 = int(input("Choose the second card (0-15): "))
        attempts += 1

        if board[choice1] == board[choice2]:
            revealed[choice1] = revealed[choice2] = True
            print("Match found!")
        else:
            print("Try again.")

    print(f"You found all pairs in {attempts} attempts!")

if __name__ == "__main__":
    main()
