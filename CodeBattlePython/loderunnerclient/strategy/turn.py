import random

from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board

def turn(gcb: Board):
    if gcb.has_ladder_at(gcb.get_my_position().get_x(), gcb.get_my_position().get_y()):
        action_id = random.randint(0, len(LoderunnerAction)-2)
    else:
        action_id = random.randint(0, len(LoderunnerAction) - 7)
    return list(LoderunnerAction)[action_id]
