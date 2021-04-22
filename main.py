from Player.Player import RandomComputerPlayer
from Player.Player import HumanPlayer

from Board.Board import TerminalBoard
from pathlib import Path


board_data = [0,0,0,0,0,0,0,0,0]
#board_data = ['X','O','X','X','O',0,0,0,'O']
board = TerminalBoard(board_data)

board.play()
