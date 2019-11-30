from loderunnerclient.internals.actions import LoderunnerAction
from loderunnerclient.internals.board import Board

def stupid(gcb: Board):
    res = gcb._line_by_line()
    print(res)
    action_id = 0
    return list(LoderunnerAction)[action_id]
