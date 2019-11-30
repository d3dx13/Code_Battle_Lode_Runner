from loderunnerclient.strategy.turn import turn
from loderunnerclient.strategy.keyboard import keyboard
from loderunnerclient.strategy.stupid import stupid
from loderunnerclient.strategy.optimal_bfs import optimal_bfs
from loderunnerclient.LodeRunnerClient import GameClient
import logging
import sys
import os

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)

def main():
    gcb = GameClient("http://51.136.50.139/codenjoy-contest/board/player/d0fkhzh469jod3m1bwzt?code=3152725939839322376&gameName=loderunner")
    strategy = globals()[sys.argv[1]]
    gcb.run(strategy)

if __name__ == '__main__':
    main()
