#Tic-Tac-Toe
#Plays the game of tic-tac-toe against a human opponent

#global constants
X = "X"
O = "O"
LOW = 0
HIGH = 8
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
WAYS_TO_WIN = ((0, 1, 2),
               (3, 4, 5),
               (6, 7, 8),
               (0, 3, 6),
               (1, 4, 7),
               (2, 5, 8),
               (0, 4, 8),
               (2, 4, 6))

def print_welcome(title):
    """Display the welcome message"""
    title = "welcome to " + title
    print("\t\t" + title.title() + "\n")
    
def print_instructions():
    """Display the game instructions"""
    print(
        """
        You will make your move known by entering a number, 0 - 8. The number
        will correspond to the board position as illustrated:
        
                        0 | 1 | 2
                       ---|---|---
                        3 | 4 | 5
                       ---|---|---
                        6 | 7 | 8
                        
        """)
    
def ask_yes_no(question):
    """Ask a yes or no question return value as 'y' or 'n.'"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_num(question, low, high):
    """Ask for a number within the range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def assign_pieces():
    """Determine if the user or the computer goes first."""
    go_first = ask_yes_no("Do you want the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move.")
        human = X
        computer = O
    else:
        print("\nOk, I will go first.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Create a new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")
    
def legal_moves(board):
    """Creates a list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Determine the game winner."""
    for pattern in WAYS_TO_WIN:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != EMPTY:
            the_winner = board[pattern[0]]
            return the_winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """Get human move"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_num("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied. Choose another.\n")
    print("Fine...")
    return move
def computer_move(board, computer, human):
    """Make computer move"""
    #Make a copy to work since function will be changing list
    board = board[:]
    #the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I will take square number: ", end="")

    #if computer can win take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move undo it
        board[move] = EMPTY

        #if human can win, block
        for move in legal_moves(board):
            board[move] = human
            if winner(board) == human:
                print(move)
                return move
            #done checking this move, undo it
            board[move] = EMPTY

            #since no one can win on the next move, pick next best open square
            for move in BEST_MOVES:
                if move in legal_moves(board):
                    print(move)
                    return move

def next_turn(turn):
    """Switch turns"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Congratulate the winner"""
    if the_winner != TIE:
        print(the_winner, " won!\n")
    else:
        print("It's a tie!\n")
def main():
    print_welcome("tic-tac-toe")
    print_instructions()
    computer, human = assign_pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
            display_board(board)
            turn = next_turn(turn)
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
            display_board(board)
            turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
        

#start
main()
input("\n\nPress the enter key to exit.")
            

    
