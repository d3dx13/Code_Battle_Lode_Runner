import random
from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board
import keyboard as kb

def keyboard(gcb: Board):
    if kb.is_pressed('a'):
        action_id = 0
    elif kb.is_pressed('d'):
        action_id = 1
    elif kb.is_pressed('w'):
        action_id = 2
    elif kb.is_pressed('s'):
        action_id = 3
    elif kb.is_pressed('e'):
        action_id = 4
    elif kb.is_pressed('q'):
        action_id = 5
    elif kb.is_pressed('k'):
        action_id = 7
    else:
        action_id = 6
    return list(LoderunnerAction)[action_id]
