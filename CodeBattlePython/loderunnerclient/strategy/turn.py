import random

from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board

def turn(gcb: Board):
    action_id = random.randint(0, len(LoderunnerAction)-1)
    return list(LoderunnerAction)[action_id]
