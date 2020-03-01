import board_class
from board_class import Board
from board_class import InitializedBoard
import vertical_draw as draw

## Represent the opponents (and their checkers etc.) with
## numbers, because we represent everything with numbers.
RED = Board.RED
BLACK = Board.BLACK

## We have to decide in which direction each opponent will proceed.
RED_HOME = Board.RED_HOME

def new_board():
    return InitializedBoard()

def ask_player_and_move( board, next_player, die1, die2 ):
    ## missing:
    pass

def opponent( player ):
    return board_class.opponent( player )

def game_over( board ):
    return board.game_over()

def draw_board( board ):
    draw.draw_board( board )

def is_move_possible( board, player, fromPoint, toPoint ):
    """
    Checks if a given move is legitimate
    (only makes sure that there is no checker waiting on the bar
    (unless the move is from the bar), and that the target point 
    contains `player`'s checkers, no checker or exactly one of
    opponent's checkers.
    """
    if not board.has_checker( player, fromPoint ):
        return False
    if board.has_checkers_on_bar( player ):
        if not fromPoint == Board.BAR:
            return False
    
    ## temporary:
    return True

