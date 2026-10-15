from figure import Pawn
from board import Board


board = Board()

pawn1 = Pawn('white', [2,3])
pawn2 = Pawn('black', [2,4])
pawn3 = Pawn('black', [3,4])

board.add_figure(pawn1)
board.add_figure(pawn2)
board.add_figure(pawn3)

print(board.figures)

board.move_on_board([2,3], [3, 4])

print(board.figures)