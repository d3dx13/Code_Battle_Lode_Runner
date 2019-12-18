from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board
import math


def stupid(gcb: Board):
    res = gcb._line_by_line()
    #print(res)
    action_id = 0
    def point_to_list(point_list):
        out = []
        for point in point_list:
            out.append([point.get_x(), point.get_y()])
        return out

    def closest_ladder(ladder_list, robot, enemy_list):
        cls_ladder = [10000000000, -1]
        i = 0
        for enemy in enemy_list:
            for ladder in ladder_list:
                if (math.fabs(enemy[0]-ladder[0]) < math.fabs(robot[0]-ladder[0])) and (math.fabs(robot[0]-ladder[0])<cls_ladder[0]):
                    cls_ladder = ladder
                    i += 1
        return cls_ladder

    def only_on_brick(list, our_brick):
        filtered = []
        for element in list:
            if (element[0]>our_brick[0][0]) and (element[0]>our_brick[len(our_brick)-1][0]):
                filtered.append(element)
        return filtered

    robot = [gcb.get_my_position().get_x(), gcb.get_my_position().get_y()]
    robot_row = robot[1]
    enemy_position = point_to_list(gcb.get_enemy_positions())
    enemy_on_row = []
    # create the list of enemies in row of our character
    for enemy in enemy_position:
        if enemy[0] == robot_row:
            enemy_on_row.append(enemy)

    wall_position = point_to_list(gcb.get_wall_positions())
    wall_on_row = []
    our_flour = []

    # create the list of walls in row of our character
    for wall in wall_position:
        if wall[1] == robot_row:
            wall_on_row.append(wall)
        if wall[1] == (robot_row + 1):
            our_flour.append(wall)

    ladder_position = point_to_list(gcb.get_ladder_positions())
    ladder_on_row = []
    # create the list of enemies in row of our character
    for ladder in ladder_position:
        if ladder[0] == robot_row:
            ladder_on_row.append(ladder)

    # find brick coordinates
    bricks_under = []
    i = 0
    for brick in our_flour:
        i += 1
        bricks_under.append(brick)
        if brick[0] < robot[0]:
            if math.fabs(our_flour[i+1][0]-brick[0]) > 1:
                bricks_under = []
        elif brick[0] > robot[0]:
            if math.fabs(our_flour[i+1][0]-brick[0]) > 1:
                break
    near_ladder = closest_ladder(only_on_brick(ladder_on_row, bricks_under), robot, enemy_on_row)
    nearest_ladder = math.fabs(closest_ladder(only_on_brick(ladder_on_row, bricks_under), robot, enemy_on_row)[0]-robot[0])
    left_hole = math.fabs(bricks_under[0][0]-robot[0])
    right_hole = math.fabs(bricks_under[len(bricks_under)-1][0]-robot[0])

    if nearest_ladder == 0:
        action_id = 3
    elif ((right_hole <= left_hole) and (right_hole < nearest_ladder))or((nearest_ladder < left_hole) and (nearest_ladder < right_hole) and (near_ladder[0] > robot[0])):
        action_id = 1
    elif ((left_hole < right_hole) and (left_hole < nearest_ladder))or((nearest_ladder < left_hole) and (nearest_ladder < right_hole) and (near_ladder[0] < robot[0])):
        action_id = 0
    else:
        action_id = 2
    print(str(left_hole), " ", right_hole, " ", nearest_ladder)

    return list(LoderunnerAction)[action_id]
