from nose.tools import assert_equal
from game import Room
from board import Board


def test_Board_constructor():
    new_board = Board()
    assert_equal(new_board.rows, 10)
    assert_equal(new_board.cols, 10)
    assert_equal(new_board.mines, 10)
    assert_equal(len(new_board.mine_coordinates), 10)


def test_place_mines(self):
    new_board = Board(rows=2, col=2, mines=0)
    new_board.mines = 1
    new_board.board_solution = [[0, 0], [0, '*']]


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
