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

## This is the hardest one:
class TodoElement:
    ## missing!
    pass

def legitimate_moves( board, player, die1, die2 ):
    """
    Return a list of move sequences that are legitimate.
    Unfortunately, in some cases we have to calculate all
    legitimate move sequences in order to decide if a given 
    move sequence is feasible, because of the maximality
    criterion (the maximum possible distance must be made).
    """
    ## Algorithm: We will set up an empty list of move
    ## sequences in which we will collect the legitimate
    ## sequences.
    
    ## We will also set up a ``todo list'' containing
    ## `TodoElement` instances, containing a move sequence,
    ## a board (situation), and a list of remaining rolls.
    ## The move sequence is a sequence of planned moves,
    ## and the remaining roll is what numbers we still have
    ## based on the roll.  Initially, the todo list will
    ## contain one or two elements, with the move sequence
    ## being empty (no planned moves so far);  if `die1` and
    ## `die2` are different numbers, we will have two elements,
    ## with `remaining-roll` being different depending on the
    ## order of dice;  if the roll is doubles, we have only
    ## one triple, the remaining rolls containing four times the
    ## number rolled.

    ## Then we will go through the todo list, and try to
    ## produce new sequences from each element; if we have
    ## finished a sequence (because there are no remaining
    ## rolls or because no further move is possible), we append
    ## the result to our list of finished sequences;  otherwise,
    ## we create an updated version of the current todo element,
    ## and append the result to the end of our todo list:
    ## we will get there later on.
    
    ## Finally, we could just return the list of finished move
    ## sequences, but we don't: we first have to keep only the
    ## maximal ones, because that's the rule in backgammon.

    finished = []
    if die1 == die2:
        todo = \
            [                   # list of todo elements
                [               # first and only element:
                    TodoElement( board, [die1, die1, die1, die1] )
                ]
            ]                                # end of todo list
    else:
        todo = \
            [                   # list of todo elements
                [               # first element:
                    TodoElement( board, [die1, die2] )
                ],               # end of first element

                [               # second element:
                    TodoElement( board, [die2, die1] )
                ]                # end of second element
            ]                    # end of todo list
    next_todo_index = 0          # our position in the todo list
    while True:                  # only stop if nothing more to do
        if next_todo_index == len( todo ) - 1: # nothing more to do
            break
        else:
            ## missing:
            ## Try to continue `move-sequence` with first element
            ## of `remaining-roll`.
            ## Append result to `finished` if failure or no more
            ## elements in `remaining-roll`;  append result to
            ## `todo` if successful.

            ## Prepare for next todo element:
            next_todo_index += 1
    ## We will choose the maximal ones in a separate function:
    return maximalMoveSequences( finished )

def maximalMoveSequences( moveSequences ):
    ## temporary:
    return moveSequences

