from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board
from loderunnerclient.internals.point import Point
from time import time
from loderunnerclient.logic.java_decompose_checher import check_moves

number_into_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

"""
Логика такова, что за один ход из одного конкретного места можно: 
1) попасть в другое место
2) остаться на том же самом месте
3) разрушить блок

Набор действий, данный игроку:
{
  GO_LEFT = 'left' - движение влево
  GO_RIGHT = 'right' - движение вправо
  GO_UP = 'up' - движение вверх
  GO_DOWN = 'down' - движение вниз
  DO_NOTHING = 'stop' - ничего не делать
  
  DRILL_RIGHT = 'act,right' - бурить вправо вниз
  DRILL_LEFT = 'act,left' - бурить влево вниз
  
  SUICIDE = 'act(0)' - суицид
}

Вопрос: Могу ли я извлечь физику игры, чтобы знать, как я взаимодействую с игрой?
Замечание: Прописывать логику саомстоятельно достаточно сложно.

"""
def eyes_possible(gcb: Board):
    global cost_map

    TIME = time()

    def _print_cost_map():
        global cost_map
        print_map = {}
        for point in cost_map:
            print_map[point] = int(cost_map[point])
        result = ""
        for y in range(gcb.get_size()[0]):
            for x in range(gcb.get_size()[1]):
                try:
                    result += number_into_char[print_map[(x, y)] % len(number_into_char)]
                except:
                    if (y == 0 or y == gcb.get_size()[0]-1 or x == 0 or x == gcb.get_size()[1]-1):
                        result += '*'
                    else:
                        result += ' '
            result += '\n'
        print(result)
    cost_map = {}  # elem = cost

    hero = (gcb.get_my_position().get_x(), gcb.get_my_position().get_y())
    cost_map[hero] = 59
    for point in gcb.get_gold_positions():
        cost_map[(point.get_x(), point.get_y())] = 1

    check = {}
    check[0] = check_moves(gcb, gcb.get_my_position())
    visited = set()
    visited.add(gcb.get_my_position())
    for iter in range(0, 300):
        check[iter+1] = []
        for point in check[iter]:
            for new_point in check_moves(gcb, point):
                if not (new_point in visited):
                    check[iter+1].append(new_point)
                    visited.add(new_point)
        for point in check[iter]:
            cost_map[(point.get_x(), point.get_y())] = 0

    for point in gcb.get_gold_positions():
        if (cost_map[(point.get_x(), point.get_y())] == 0):
            cost_map[(point.get_x(), point.get_y())] = 9
        else:
            cost_map[(point.get_x(), point.get_y())] = 1


    _print_cost_map()
    print(time() - TIME)
    return LoderunnerAction.DO_NOTHING
