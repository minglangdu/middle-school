'''
Project 6 : Tic Tac Toe (Base Student Code)

This program contains a partly complete Tic Tac Toe game.

In Phase 1, students need to create ttt_board (the 2-d list that
represents the tic-tac-toe game board) and write the print_board,
check_win, and check_draw functions to get the game working. For
now, these are all written as stubs.

In Phase 2, students will update those functions and the ttt_board
data structure to use a 4x4 tic-tac-toe board instead of a 3x3.

'''

"""
Minglang Du 7-C6
"""

import copy   # We will use the copy module's deepcopy function to 
              # make deep list copies w/ sub-lists (for searching  
              # decision trees of possible moves).
              
import random   # We will use the random module's randomrange()
                # function to randomize AI moves and make it less
                # predictable when it could make multiple moves
                # of equal strength.

'''
ttt_board is the 2-d list that holds the Tic Tac Toe board info.

*** PHASE 1: Create a 2-dimensional list representing a 3x3 tic tac
toe board. There should be three sublists, each corresponding to a
different row on the board; each should be coded before its matching
comment. Each element in that sublist should be a string consisting
of a blank space, representing an empty square on the board.

*** PHASE 2: Students will update this data structure to make
it represent a 4x4 tic tac toe board.
'''
ttt_board = [
          [' ',' ',' '],
          [' ',' ',' '],
          [' ',' ',' ']
    ]

user_char = 'X'
ai_char = 'O'

'''
print_board(bd) prints the game board bd with borders.

*** PHASE 1: Print the tic-tac-toe board with appropriate borders and
headings. See the sample program to see what this should look like.
  
*** PHASE 2: Students will update this function to make it work with
a 4x4 tic-tac-toe board.
'''
def print_board(bd):
    n = len(bd[0]) # for convenience
    h = " " # construct header string
    for i in range(97, 97 + n):
        h += "  " + chr(i) + "   "
    print(h) # print header string
    no = " " # no underscore string
    yes = " " # yes underscore string
    for i in range(n):
        no += " " * 5
        yes += "_" * 5
        if (i < n - 1):
            no += "|"
            yes += "|" # construct filler strings
    for y in range(n): # construct rest of strings
        print(no)
        s = str(y + 1) # construct string showing row
        for x in range(n):
            s += "  " + bd[y][x] + "  " 
            if (x < n - 1):
                s += "|"
        print(s)
        if (y < n - 1):
            print(yes) # print underscore string unless it is the last string
        else:
            print(no)

'''
check_win(bd, ch) should return True if the given char ch appears
in three (Phase 1) or four (Phase 2) consecutive spaces across a
row, column, or diagonal of board bd. Else, it should return False.

A return value of True indicates that the player with that char won.

*** PHASE 1: Students will write this function for a 3x3 board. 
*** PHASE 2: Students will update this function to make it work with
             a 4x4 board.
'''
def check_win(bd, ch):
    n = len(bd[0]) # to be compatible with all sizes of boards
    # check vertical wins
    for x in range(n):
        flag = True # flag is used to check if all three work in a row
        for y in range(n):
            if bd[y][x] != ch:
                flag = False
                break
        if (flag):
            return True
    # check horizontal wins
    for y in range(n):
        flag = True
        for x in range(n):
            if bd[y][x] != ch:
                flag = False
                break
        if (flag):
            return True
    # check first diagonal
    flag = True
    for x in range(n): # there is only one diagonal
        # so there is only one loop
        if bd[x][x] != ch:
            flag = False
            break
    if (flag):
        return True
    # check the second diagonal
    flag = True
    for x in range(n):
        if bd[x][n - x - 1] != ch:
            flag = False
            break
    return flag

'''
check_draw(bd) should return True if the board bd is completely 
filled and no more moves are possible (it's a draw). Else, it should
return False.

*** PHASE 1: Students will write this function for a 3x3 board.
*** PHASE 2: Students will update this function to make it work with
             a 4x4 board.
'''
def check_draw(bd):
    n = len(bd[0])
    flag = True # check if there are empty spaces
    for i in range(n):
        for j in range(n):
            if bd[i][j] == ' ':
                flag = False
                break
    return flag


'''
run_game() prints the intro messages and then runs a loop that 
alternates the AI and user turns.

*** WARNING! Students MUST NOT modify this function, but they should
study how it works.
'''
def run_game():
    global user_char, ai_char
    print('Welcome to the Tic Tac Toe game.')
    print('The AI has the character O. You have the character X.')
    print('You go first. Good luck!\n')
    print_board(ttt_board)
    
    # Loop to keep making AI moves and prompting user for moves:
    while True:
                
        # User Turn
        
        # get_user_move() will prompt the user for a move, this
        # will be saved into user_move, and the row and column
        # of that move will be identified and saved:
        user_move = get_user_move()
        user_row = user_move[0]
        user_col = user_move[1]
        
        # play_move() applies that user move to the board, and then
        # print_board() prints the resulting board position:
        play_move(ttt_board, user_char, user_row, user_col)
        print('\n You have made your move: \n') 
        print_board(ttt_board)
        print()
        
        # Now, we check to see if the move resulted in a win for the
        # user or a draw, and if so, we end the game:
        if check_win(ttt_board, user_char):  # Check if user won
            print('\n⚞♬♪♫  Congratulations!!! You won Tic Tac,'
                  'Toe!!!  ♪♬♫⚟\n')
            break
        elif check_draw(ttt_board):  # Check if it's a draw        
            print('\nIt\'s a draw!! Game over.')
            break
        
        # AI Turn
        
        # get_ai_move() will calculate the AI's move (with the help
        # of the minimax function). The resulting move will be saved
        # into ai_move, and the row and column of that move will be
        # identified and saved:
        print('\n Please wait while the AI calculates its move...\n')
        ai_move = get_ai_move()
        ai_row = ai_move[1]
        ai_col = ai_move[2]
        
        # play_move() applies that AI move to the board, and then
        # print_board() prints the resulting board position:
        play_move(ttt_board, ai_char, ai_row, ai_col)
        print('\n The AI has made its move: \n') 
        print_board(ttt_board)
        print()
        
        # Now, we check to see if the move resulted in a win for the
        # AI or a draw, and if so, we end the game:
        if check_win(ttt_board, ai_char):  # Check if AI won
            print('\nThe AI has won!! You have lost!! Game Over.')
            break
        elif check_draw(ttt_board):  # Check if it's a draw
            print('\nIt\'s a draw!! Game over.')
            break
  
  
'''
play_move(bd, char, row, col) attempts to place the given char at 
the location on board bd given by row and col. If the space is not 
empty, prompt the user for a new space and run play_move() again.

*** WARNING! Students MUST NOT modify this function, but they should
study how it works.
'''
def play_move(bd, char, row, col):
    if bd[row][col] is ' ':  # If the location is empty,
        bd[row][col] = char  # apply the move to that spot.
    else:  # Else, user must have chosen a non-empty space
        print('Space is not empty! Choose again.')
        move_loc = get_user_move() # Get a new move...
        move_row = move_loc[0]
        move_col = move_loc[1]
        play_move(bd, char, move_row, move_col) #...and try again

'''
get_user_move() prompts the user for a move in A1 column/row format.
It then converts that input into an integer row and column and
returns it as a two-element list.

*** WARNING! Students MUST NOT modify this function, but they should
study how it works.
'''
def get_user_move():
    global ttt_board
    loc = input('Enter the location of your move (e.g., B3): ')
    while True:
        # Try the user input to see if its format is valid:
        try:
            # Try to convert the user input string to integer values
            # for the column and row:
            col = ord(loc[0].lower()) - 97  
            row = int(loc[1]) - 1
        except:
            # The user input format was not valid, so try again:
            loc = input('Invalid input format. '
                        + 'Choose again (e.g., B3): ')
            continue
        # Make sure the row and column selected by user are within
        # the board's dimensions:
        if row > len(ttt_board)-1 or col > len(ttt_board[0])-1 \
            or row < 0 or col < 0:
            loc = input('Row or column out of bounds. '
                        + 'Choose again (e.g., B3): ')
            continue
        break
    # Return the row and column inputted by the user as a list:
    return [row, col]

'''
get_ai_move() is a helper function that sets the parameters and makes
the initial call to minimax(), which runs the minimax algorithm
to get the AI's best move. 

*** WARNING! Students MUST NOT modify this function, but they should
it along with minimax() below if they are interested in basic AI.
'''
def get_ai_move():
    # We use an AI search depth of 9. The search depth represents how
    # many moves ahead the AI will look. 9 is more than is needed for
    # a 3x3 board if the AI doesn't go first, but students will
    # upgrade this to a 4x4 board in Phase 2. An AI that looks more
    # moves ahead is harder to beat, but higher search depths have
    # exponentially more branches to search, so search depth must be
    # weighed against how long the AI takes to move.
    return minimax(ttt_board, 9, True, -2, 2)

'''
minimax() uses the Minimax Algorithm with Alpha-Beta Pruning
to find the best possible move for the AI.

position = current position of the game board
player = the player char, either X or O (AI or user)
depth = current search depth (search stops once depth reaches 0)
alpha = score of best AI move found so far
beta = score of best user move found so far

*** WARNING! Students MUST NOT modify this function, but they may
study how it works if they are interested. This is a relatively basic
AI algorithm, but for this level, it is advanced, and students are 
not expected to understand it. An attempt was made to explain it 
with comments for advanced/curious students. The video at

    https://www.youtube.com/watch?v=l-hh51ncgDI

also explains this algorithm well.
'''
def minimax(position, depth, is_ai_player, alpha, beta):
    
    # Assign a score to each win, lose, and draw condition for the
    # AI so that it can make numerical comparisons to evaluate the
    # strength of moves. If a move would lead to a victory, for
    # example, it would have a higher score (1) than a move that
    # would lead to a draw (0) or a loss (-1). The AI will maximize
    # its score to try to achieve victory or at least avoid defeat.
    
    if check_win(position, ai_char):
        # If check_win returned True for ai_char and triggered this
        # branch, that means the AI won in this scenario. A score of
        # 1 indicates an AI victory, so we return that and a token
        # row and col (these don't matter since the previous move is
        # what led to victory, so it's the previous move that
        # contains the correct row and col data)
        return [1, 0, 0] 
    
    elif check_win(position, user_char):
        # If check_win returned True for user_char and triggered this
        # branch, that means the user won in this scenario. A score
        # of -1 indicates a user victory, so we return that and a
        # token row and col.
        return [-1, 0, 0]
    
    elif check_draw(position) or depth == 0:
        # Next, either it is a draw, or we have reached the maximum  
        # search depth without a winner. So, we just return a neutral
        # score of 0 with a token row and column:
        return [0, 0, 0]
    
    # Compile each available move (empty spaces) for the given board 
    # and save the moves as row/column lists in a list called moves.
    # Randomize the order in which the moves are inserted so the AI
    # does not search through them in a predictable pattern.
    moves = []
    row_range = len(ttt_board)
    col_range = len(ttt_board[0])
    for row in range(row_range):
        for col in range(col_range):
            if position[row][col] is ' ': # Space is empty, so...
                # it's a possible move. Insert it into the AI's moves
                # list at a random location:
                moves.insert(random.randrange(len(moves)+1),
                             [row, col])

    
    # Simulate the game, searching several steps ahead to find the
    # best possible move for the AI.
    #
    # For each possible AI move, the AI also needs to simulate the
    # best move the player could make. This way the AI can avoid
    # moves that would create a pathway to victory for the user.
    
    # AI hasn't tried any moves in this branch yet, so the best 
    # move starts off empty.
    best_move = None  
    
    # If the current player is the AI (the maximizing player), try
    # to maximize the game score.
    if is_ai_player:
        
        # First, max_score starts off as lower (-2) than the worst
        # possible score (-1, for a loss). We do this to ensure that
        # the AI still treats the next move as a possible move even
        # if it results in a loss for the AI. (This prevents the AI
        # from failing to produce a move and crashing the program.)
        max_score = -2   
        
        # Loop through possible AI moves in the current board 
        # position, trying and evaluating each, while avoiding
        # unnecessary search branches ("pruning" them):
        for possible_move in moves:
            
            # Get the row and column of the next available AI move.
            row = possible_move[0]  
            col = possible_move[1]
            
            # Create a copy of the current board position to try
            # possible moves on it:
            new_position = copy.deepcopy(position)
            
            # Try the move on the copy of the board position:
            play_move(new_position, ai_char, row, col)
            
            # Recursively find the best possible move of the user 
            # after the move the AI just tried. We set the third 
            # argument, is_ai_player, to False, since it is the 
            # user making the next move:
            move = minimax(new_position, depth-1, False, alpha, beta)
            
            # Get the score associated with that best move:
            score = move[0]
            
            # If the score is higher than the current best score in
            # this search path, it is the new best score and thus
            # the best move for the AI (in this path).
            if score > max_score:  
                max_score = score
                best_move_row = row   # Save the row and column 
                best_move_col = col   # of the move.
                
            # Alpha-Beta Pruning section
            # (not essential for finding a move, but speeds up the
            # algorithm by avoiding wasteful search paths)
            
            # Track the current highest score among ALL the moves AI
            # can possibly make:
            alpha = max(max_score, alpha)
            
            # If the user's current best score (beta) is already
            # better than the AI's best score (alpha) that would
            # result from this board position, we won't search any 
            # further moves from this position; we will just guess
            # that the user is rational and smart enough to not
            # take a path that worsens his odds of victory (if he
            # does anyway, we can deal with it then). This choice
            # "prunes" the rest of this branch of the decision tree,
            # avoiding wasteful searches.
            if beta <= alpha:
                break
        
        # Return AI's best move as a list of score, row, and column:
        return [max_score, best_move_row, best_move_col]
    
    else:
        # Else, it's the user player. Simulate the user's move.
        
        # The user is trying to maximize his chances of winning, i.e.
        # he is trying to minimize the AI's chances of winning. So,
        # we simulate him finding the minimum possible AI score in
        # this search branch.
        
        # Start the user's min_score at 2, which is even worse than
        # the worst-case scenario for him (a score of 1 indicates an
        # AI victory). We do this to ensure that the simulated user
        # chooses at least one move, even if that move results in a
        # loss. This prevents the simulated user from failing to
        # produce a move and crashing the program.
        min_score = 2
        
        # Loop through possible user moves in the current board 
        # position, trying and evaluating each, while avoiding
        # unnecessary search branches ("pruning" them):
        for possible_move in moves:
            
            # Get the row and column of the next available user move.
            row = possible_move[0]
            col = possible_move[1]
            
            # Create a copy of the current board position to try
            # possible moves on it:
            new_position = copy.deepcopy(position)
            
            # Try the move on the copy of the board position:
            play_move(new_position, user_char, row, col)
            
            # Recursively get the best possible move of the AI after
            # the move the simulated user just tried. We set the
            # third argument, is_ai_player, to True, since it is the
            # AI making the next move:
            move = minimax(new_position, depth-1, True, alpha, beta)
            score = move[0]
            
            # If the score of the current move is lower than the
            # current lowest score in this position, that move is
            # the current best move for the user in this position.
            if score < min_score:
                min_score = score
                best_move_row = row
                best_move_col = col
            
            # Alpha-Beta Pruning section
            # (not essential to find a move, but it speeds up the
            # algorithm by eliminating wasteful search branches)
            
            # Compare the best user score for this branch to the best
            # user score for all searched branches. If this branch's
            # score is better, it becomes the new best overall user
            # score (beta): 
            beta = min(min_score, beta)
            
            # If the beta (the user's current best score) that would 
            # result from this position is already lower than alpha  
            # (the AI's current best score), no need to search this
            # branch further. We can rightly assume that the AI would
            # make the move that corresponds to it having a better 
            # score rather than the one that leads to the user having 
            # a better score. In other words, let's not waste the 
            # simulated user's time searching a path that the AI
            # definitely won't take:
            if beta <= alpha:
                break
            
        # Return the user's best move as a list of the move's score,
        # row, and column:
        return [min_score, best_move_row, best_move_col]
    
    # End of minimax function

# Start the game:
run_game()