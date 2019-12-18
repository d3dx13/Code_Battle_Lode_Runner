from loderunnerclient.strategy.turn import turn
from loderunnerclient.strategy.keyboard import keyboard
from loderunnerclient.strategy.stupid import stupid
from loderunnerclient.LodeRunnerClient import GameClient
import logging
import sys
import os

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)

def main():
    gcb = GameClient("http://127.0.0.1:8080/codenjoy-contest/board/player/ef1ibc24wwoq4sui2c77?code=3448429991401935482&gameName=loderunner")
    strategy = globals()[sys.argv[1]]
    #strategy = stupid
    gcb.run(strategy)

if __name__ == '__main__':
    main()
