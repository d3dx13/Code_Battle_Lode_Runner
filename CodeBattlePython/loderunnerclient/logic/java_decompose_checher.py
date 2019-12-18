from loderunnerclient.internals.element import Element
from loderunnerclient.internals.point import Point
from loderunnerclient.internals.board import Board


def is_possible_move(board: Board, current: Point, new: Point):
    x = current.get_x()
    y = current.get_y()
    if board.is_barrier_at(x, y):
        return False
    nx = new.get_x()
    ny = new.get_y()
    if (abs(nx - x) + abs(ny - y)) > 1:
        return False

    if board.is_barrier_at(nx, ny):
        return False
    if (ny - y == -1) and (not board.has_ladder_at(x, y)):
        return False

    yd = y + 1
    if (
            (ny - y != 1) and
            (not board.is_barrier_at(x, yd)) and
            (not board.has_ladder_at(x, yd)) and
            (not board.has_ladder_at(x, y)) and
            (not board.has_pipe_at(x, y))
    ):
        return False
    return True

def check_moves(board: Board, current: Point):
    moves = {(1, 0),(0, 1),(-1, 0),(0, -1)}
    available_moves = []
    for move in moves:
        new = Point(current.get_x() + move[0], current.get_y() + move[1])
        if is_possible_move(board, current, new):
            available_moves.append(new)
    return available_moves