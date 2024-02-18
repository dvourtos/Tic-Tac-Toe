"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Initialize variables to count X's and O's
    x_count = 0
    o_count = 0
    empty_count = 0

    #Check each element of the inner list.
    for l in board :
        for element in l :
            if element == X :
                x_count += 1
            elif element == O :
                o_count += 1
            elif element == EMPTY :
                empty_count += 1
    
    #If the board is empty (initial state) return X
    if empty_count == 9 :
        return X
    #Return which player's move is.
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #Initialize an empty set.
    act = set()

    #For each value of the inner list check which are not EMPTY
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            try :
                if board[i][j] == EMPTY :
                    act.add((i,j))
            except IndexError:
                pass
    return act

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #Deep Copy the given board
    board_copy = copy.deepcopy(board)

    #Take all of the available actions from the given board.
    a = actions(board)

    #If action cannot be made raise an Exception
    if action not in a :
        raise Exception("Action cannot be made.")
    
    #Find the player to play
    player_to_play = player(board)
    i,j = action

    #Store in the board copy the proper value
    board_copy[i][j] = X if player_to_play == X else O

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #Using the utility function check if there is a winner or not.
    r = utility(board)
    if r == 1:
        return X
    elif r == -1 :
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #If there is a winner then game is over
    if winner(board) is not None :
        return True
    
    #Check if the board is fully filled
    for row in board :
        if EMPTY in row :
            return False

    #If there is no winner and the board is fully filled, the game is over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #Check Rows.
    for row in board :
        if row.count(X) == 3 :
            return 1
        elif row.count(O) == 3 :
            return -1
        
    #Check Columns.
    for col in range(len(board)) :
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY :
            if board[0][col] == X: 
                return 1
            elif board[0][col] == O:
                return -1
    
    #Check Diagonals.
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0]!=EMPTY) or (board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY) :
        if board[1][1] == X:
            return 1
        elif board[1][1] == O:
            return -1
    return 0

def maxvalue(board) :
    v = -100000000
    if terminal(board) :
        return utility(board),None
    for action in actions(board) :
        min_value,bestMove = minvalue(result(board,action))
        if min_value > v :
            v = min_value
            bestMove = action 
    return v, bestMove

def minvalue(board) :
    v = 1000000000
    if terminal(board) :
        return utility(board), None
    for action in actions(board) :
        max_value,bestMove = maxvalue(result(board,action))
        if max_value < v :
            v = max_value
            bestMove = action
    return v, bestMove

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #If the board is in terminal state return None
    if terminal(board) :
        return None

    #Check wich player is to play. If its the maximizing player call the maxvalue function. Otherwise call the minvalue.
    next_player = player(board)
    if next_player == X :
        _, bestMove = maxvalue(board)
        return bestMove
    else :
        _,bestMove = minvalue(board)
        return bestMove
