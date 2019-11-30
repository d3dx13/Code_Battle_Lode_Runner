from loderunnerclient.strategy.turn import turn
from loderunnerclient.strategy.keyboard import keyboard
from loderunnerclient.LodeRunnerClient import GameClient
import logging
import sys
import os
import xmltodict

with open(os.path.dirname(os.path.abspath(__file__))+'/settings.xml') as fd:
    settings = xmltodict.parse(fd.read())

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)

def main():
    gcb = GameClient("http://codebattle-spb-2019.francecentral.cloudapp.azure.com/codenjoy-contest/board/player/5oap4pgcmb361163t32z?code=1323028855795138413&gameName=loderunner")
    strategy = globals()[sys.argv[1]]
    gcb.run(strategy)

if __name__ == '__main__':
    main()
