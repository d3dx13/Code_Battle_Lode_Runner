from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board
import queue
number_into_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def optimal_bfs(gcb: Board):
    global x_max, y_max, map, cost_map, task_list, hero
    y_max = 0
    x_max = 0
    def parse_map():
        global x_max, y_max, map, cost_map
        map_copy = gcb._line_by_line().split('\n')
        map = {}
        x_max = len(map_copy[0])
        y_max = len(map_copy[1])
        for y in range(y_max):
            for x in range(x_max):
                map[(x, y)] = map_copy[y][x]
    def print_cost_map():
        global x_max, y_max, map, cost_map
        print_map = {}
        for point in cost_map:
            print_map[point] = int(10.0*(cost_map[point][0]-1) / cost_map[point][1] + 0.5)
        result = ""
        for y in range(y_max):
            for x in range(x_max):
                try:
                    result += number_into_char[print_map[(x, y)] % len(number_into_char)]
                except:
                    if (y == 0 or y == y_max-1 or x == 0 or x == x_max-1):
                        result += '*'
                    else:
                        result += ' '
            result += '\n'
        print(result)

    def calc_next_ceil():
        global map, cost_map, task_list
        point = task_list.get()
        point = list(point)
        if (map[(point[0], point[1])] in {' ', '◄', '►'} and map[(point[0], point[1]+1)] in {'H', '#', '☼', ')', '(','U','Э','Є'}):
            if (map[(point[0]-1, point[1])] in {' ', 'H', '~', '$', '&', '@'} and not ((point[0]-1, point[1]) in cost_map.keys())):
                new_cost = list(cost_map[(point[0], point[1])])
                new_cost[1] += 1
                if (map[(point[0] - 1, point[1])] == '$'):
                    new_cost[0] = 1
                if (map[(point[0] - 1, point[1])] == '&'):
                    new_cost[0] = 5
                if (map[(point[0] - 1, point[1])] == '@'):
                    new_cost[0] = 10
                cost_map[(point[0]-1, point[1])] = new_cost
                task_list.put((point[0]-1, point[1]))
            if (map[(point[0]+1, point[1])] in {' ', 'H', '~', '$', '&', '@'} and not ((point[0]+1, point[1]) in cost_map.keys())):
                new_cost = list(cost_map[(point[0], point[1])])
                new_cost[1] += 1
                if (map[(point[0] +1, point[1])] == '$'):
                    new_cost[0] = 1
                if (map[(point[0] +1, point[1])] == '&'):
                    new_cost[0] = 5
                if (map[(point[0] +1, point[1])] == '@'):
                    new_cost[0] = 10
                cost_map[(point[0]+1, point[1])] = new_cost
                task_list.put((point[0]+1, point[1]))
        if (map[(point[0], point[1])] in {' ', ']', '['} and map[(point[0], point[1] + 1)] in {' ', '$', '&', '@'}):
            if (not ((point[0], point[1]+1) in cost_map.keys())):
                new_cost = list(cost_map[(point[0], point[1])])
                new_cost[1] += 1
                if (map[(point[0], point[1]+1)] == '$'):
                    new_cost[0] = 1
                if (map[(point[0], point[1]+1)] == '&'):
                    new_cost[0] = 5
                if (map[(point[0], point[1]+1)] == '@'):
                    new_cost[0] = 10
                cost_map[(point[0], point[1]+1)] = new_cost
                task_list.put((point[0], point[1]+1))
        if (map[(point[0], point[1])] in {'Y', 'H'}):
            if (map[(point[0], point[1]+1)] in {' ', 'Y', 'H', '~', '$', '&', '@'} and not ((point[0], point[1]+1) in cost_map.keys())):
                new_cost = list(cost_map[(point[0], point[1])])
                new_cost[1] += 1
                if (map[(point[0], point[1]+1)] == '$'):
                    new_cost[0] = 1
                if (map[(point[0], point[1]+1)] == '&'):
                    new_cost[0] = 5
                if (map[(point[0], point[1]+1)] == '@'):
                    new_cost[0] = 10
                cost_map[(point[0], point[1]+1)] = new_cost
                task_list.put((point[0], point[1]+1))
            if (map[(point[0], point[1]-1)] in {' ', 'Y', 'H', '~', '$', '&', '@'} and not ((point[0], point[1]-1) in cost_map.keys())):
                new_cost = list(cost_map[(point[0], point[1])])
                new_cost[1] += 1
                if (map[(point[0], point[1]-1)] == '$'):
                    new_cost[0] = 1
                if (map[(point[0], point[1]-1)] == '&'):
                    new_cost[0] = 5
                if (map[(point[0], point[1]-1)] == '@'):
                    new_cost[0] = 10
                cost_map[(point[0], point[1]-1)] = new_cost
                task_list.put((point[0], point[1]-1))

    task_list = queue.Queue()
    parse_map()
    cost_map = {} # elem = [cost, time]

    hero = (gcb.get_my_position().get_x(), gcb.get_my_position().get_y())
    cost_map[hero] = [1, 1]
    task_list.put(hero)
    while (not task_list.empty()):
        calc_next_ceil()

    print_cost_map()
    return list(LoderunnerAction)[6]
