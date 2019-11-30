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
    gcb = GameClient(settings["connect"]["address"]["@data"], settings["connect"]["player-id"]["@data"], settings["connect"]["code"]["@data"])
    strategy = globals()[sys.argv[1]]
    gcb.run(strategy)

if __name__ == '__main__':
    main()
