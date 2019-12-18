from loderunnerclient.strategy.turn import turn
from loderunnerclient.strategy.keyboard import keyboard
from loderunnerclient.strategy.stupid import stupid
from loderunnerclient.strategy.optimal_bfs import optimal_bfs
from loderunnerclient.strategy.eyes_possible import eyes_possible
from loderunnerclient.LodeRunnerClient import GameClient
import logging
import sys
import os

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)

def main():
    gcb = GameClient("http://127.0.0.1:8080/codenjoy-contest/board/player/5qh3sshg71palazjercg?code=8398025344020371513&gameName=loderunner")
    strategy = globals()[sys.argv[1]]
    #strategy = eyes_possible
    gcb.run(strategy)

if __name__ == '__main__':
    main()
