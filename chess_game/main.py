from figure import Pawn
from board import Board


board = Board()

pawn1 = Pawn('white', [2,2])
pawn2 = Pawn('white', [3,3])

pawn3 = Pawn('black', [6,7])
pawn4 = Pawn('black', [7,6])

board.add_figure(pawn1)
board.add_figure(pawn2)
board.add_figure(pawn3)
board.add_figure(pawn4)

board.move_on_board([2,2], [2,4])
board.move_on_board([3,3], [3,5])

board.move_on_board([6,7], [6,5])
board.move_on_board([7,6], [7,4])