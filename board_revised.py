from sys import exit
from random import randint
from Coordinate import Coordinate


class Board():
    BOXES = [[1, 0], [0, 1], [1, 1], [-1, 1],
             [1, -1], [-1, 0], [0, -1], [-1, -1]]

    def __init__(self, rows=10, cols=10, mines=10):
        self.rows = rows
        self.cols = cols
        self.board = [['-'] * self.rows for __ in range(self.cols)]
        self.board_solution = [[0] * self.rows for __ in range(self.cols)]
        self.TEST_BOARD = [[]]
        self.mines = mines
        self.mine_coordinates = []
        self._place_mines()
        self.flag_count = 0
        self._place_mine_clues()
        self.solved = False

    def _place_mines(self):
        mine_count = 0
        while mine_count < self.mines:
            row = randint(0, self.rows - 1)
            col = randint(0, self.cols - 1)
            if self.board_solution[row][col] == 0:
                mine_count += 1
                self.mine_coordinates.append(Coordinate(row, col))
                self.board_solution[row][col] = '*'
        # self.board_solution[0][0] = '*'

    def _place_mine_clues(self):
        for mine_coord in self.mine_coordinates:
            for box in Board.BOXES:
                cell = Coordinate(mine_coord.row + box[0],
                                  mine_coord.col + box[1])
                if self._is_valid_coordinate(cell.row, cell.col) and \
                        not self._is_mine(cell.row, cell.col):
                    self.board_solution[cell.row][cell.col] += 1

    def _print_board(self, board):
        print "   ",
        for index in range(self.cols):
            print str(index + 1) + ' ',
        print
        for row in range(self.rows):
            print '{:2}'.format(str(row + 1)) + '[',
            for i in range(self.cols):
                if i == self.cols - 1:
                    print str(board[row][i]) + ' ]'
                else:
                    print str(board[row][i]) + ' ',
        print

    def _is_mine(self, row, col):
        if self.board_solution[row][col] == '*':
            return True
        else:
            return False

    def _take_action(self, row, col, action):
        if self._is_mine(row, col) and action == 'step':
            print "Game Over"
        elif not self._is_mine(row, col) and action == 'step':
            self._clear_and_check_adjacent(row, col)
        elif action == 'flag':
            self.board[row][col] = '+'
            self.flag_count += 1
        elif action == 'remove':
            if self.board[row][col] == '+':
                self.board[row][col] = '-'
                self.flag_count -= 1

    def _is_solved(self):
        for mine in self.mine_coordinates:
            if self.board[mine.row][mine.col] != '+':
                return False
        return True
        print "Correct Solution"

    def _is_valid_coordinate(self, row, col):
        if (0 <= row < self.rows) and (0 <= col < self.cols):
            return True
        return False

    def _clear_and_check_adjacent(self, row, col):
        '''
        Stepped into cell at row, col and it was not a mine.
        If cell > 0, reveal number on board.
        if cell == 0, no mines are adjacent to cell. Reveal all adjacent cell
            if revealed cell == 0, reveal all adjacent cells
        '''
        if self.board_solution[row][col] > 0:
            self._reveal_cell(row, col)
        elif self.board_solution[row][col] == 0:
            self._reveal_adjacent_cells(row, col)

    def _reveal_cell(self, row, col):
        self.board[row][col] = self.board_solution[row][col]

    def _reveal_adjacent_cells(self, row, col):
        # clear all adjacent cells. if adjcent cell is clear
        self._reveal_cell(row, col)
        for box in Board.BOXES:
            cell = Coordinate(row + box[0], col + box[1])
            if self._is_valid_coordinate(cell.row, cell.col) and \
                    self.board[cell.row][cell.col] == '-':
                self._reveal_cell(cell.row, cell.col)
                if self.board_solution[cell.row][cell.col] == 0:
                    self._reveal_adjacent_cells(cell.row, cell.col)


class Engine():
    def __init__(self):
        self.new_game = Board(mines=2)

    def play(self):
        while not self.new_game.solved:
            self.new_game._print_board(self.new_game.board_solution)
            self.new_game._print_board(self.new_game.board)
            row = input("Row: ")
            col = input("Col: ")
            action = raw_input("Step, Flag or Remove: ")
            # print "Column Row Action"
            # print "Action: Step, Flag or Remove"
            # string_input = raw_input(">: ").split()
            # row, col, action = string_input

            if not self.new_game._is_valid_coordinate(row - 1, col - 1):
                print "invalid coordinates"
                continue
            else:
                self.new_game._take_action(row - 1, col - 1, action)
            if self.new_game._is_solved():
                print "You win!!!"
                exit(1)


test_game = Engine()
test_game.play()

# game = Board()
# while not game.solved:
#     game._print_board(game.board_solution)
#     game._print_board(game.board)
#     row = input("Row: ")
#     col = input("Col: ")
#     action = raw_input("Step, Flag or Remove: ")
#     game._take_action(row, col, action)
#     game._is_solved()

'''
# UX
    # Accepting Input
    # Producing Output
# Number Indicators Implementation
# Game Logic
# main file that initializes the game
'''
# print "Row:"
# row = raw_input("> ")
# print "Column:"
# col = raw_input("> ")
# print "Step or Mine"
# action = raw_input("> ")
