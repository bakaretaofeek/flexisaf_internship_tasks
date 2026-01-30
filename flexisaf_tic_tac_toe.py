import random

# Define the game board
def create_board():
    return [" " for _ in range(9)]


def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Check if a player has won

def check_winner(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


# Check if the game is a tie

def check_tie(board):
    return " " not in board



# Storing good moves
ai_memory = {}  # stores good moves


def ai_move(board):
    state = tuple(board)
    empty_positions = [i for i in range(9) if board[i] == " "]

    # If AI has learned a good move, use it
    if state in ai_memory:
        return ai_memory[state]

    # Otherwise pick randomly
    return random.choice(empty_positions)


# Main game loop

def play_game():
    board = create_board()
    current_player = "X"  # User = X, AI = O
    moves_history = []

    while True:
        print_board(board)

        if current_player == "X":
            move = int(input("Choose a position (0-8): "))
            if board[move] != " ":
                print("That spot is taken. Try again.")
                continue
        else:
            move = ai_move(board)
            print("AI chooses:", move)
            moves_history.append((tuple(board), move))

        board[move] = current_player

        # Check win
        if check_winner(board, current_player):
            print_board(board)
            print(current_player, "wins!")

            # AI learns winning moves
            if current_player == "O":
                for state, move in moves_history:
                    ai_memory[state] = move
            break

        # Check tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Call the main game loop

play_game()


