import json
from datetime import datetime
from datetime import timedelta
from collections import defaultdict

if __name__ == "__main__":
    pass


class Export:
    expi=None
    gold=None
    mode=None
    time=None

    def __init__(self, xp:str='0', gold:str='0', mode:str='', time:str=''):
        self.expi = int(xp.strip())
        self.gold = int(gold.strip())
        self.mode = mode.strip()
        self.time = datetime.strptime(time.strip(), "%Y-%m-%dT%H:%M:%S.%fZ") if time != '' else None

    def __str__(self):
        return f"{{expi={self.expi}, gold={self.gold}, mode={self.mode}, time={self.time}}}"

class ModeResult:
    xp=0
    gold=0
    seconds=0.0

    def updateXp(self, xp:int):
        self.xp+=xp
    def updateGold(self, gold:int):
        self.gold+=gold
    def updateSeconds(self, delta:timedelta):
        # for debugging mode changes:
        #print(f"adding {delta.total_seconds()} seconds") # for debugging mode changes
        self.seconds+=delta.total_seconds()

    def __str__(self):
        return f"{{xp={self.xp}, gold={self.gold}, seconds={self.seconds}}}"


def getStatsFile () -> str:
    # read file and return contents as str
    with open('raw_data.json', 'r') as f:
        return f.read()

def convertJsonToDict (raw_string:str) -> dict:
    # load json from string
    return json.loads(raw_string)

def extractExportData (raw_dict:dict) -> list:
    # convert json export to list of py-objects
    data = raw_dict['data']
    result = [Export(d['metadata']['experience'],d['metadata']['gold'],d['metadata']['gameMode'],d['createdAt']) for d in data]
    return result

def computeResultDict (exportList:list) -> dict:
    # compute rewards and time played per gamemode
    start=None
    currentMode=None
    last=None
    result=defaultdict(ModeResult)

    for i,expo in enumerate(exportList):
        # init at the beginning of the list
        if i == 0:
            start=expo.time
            currentMode=expo.mode
            last=expo.time
            result[currentMode]=ModeResult()
            result[currentMode].updateXp(expo.expi)
            result[currentMode].updateGold(expo.gold)
            continue
        # add current export to result and finish up
        if i == len(exportList)-1 and currentMode == expo.mode:
            last=expo.time
            result[currentMode].updateSeconds(last - start)
            result[currentMode].updateXp(expo.expi)
            result[currentMode].updateGold(expo.gold)
            continue
            
        # compute total and keep going for same mode
        if currentMode == expo.mode:
            last=expo.time
            result[currentMode].updateXp(expo.expi)
            result[currentMode].updateGold(expo.gold)
            continue
        
        # compute timespan for current mode
        result[currentMode].updateSeconds(last - start)

        # TODO fix single pings and pauses/breaks, playtime not computed correctly
        # since join and leave times arent in data this tool cannot tell...
        # ... if user was playing without reward or went on a break :(
        
        # then start tracking new mode
        start=expo.time
        currentMode=expo.mode
        last=expo.time
        
        # init new dict-pair if needed
        if result[currentMode] is None:
            result[currentMode]=ModeResult()
        # and https://www.youtube.com/watch?v=IAUcHcVnzBM
        result[currentMode].updateXp(expo.expi)
        result[currentMode].updateGold(expo.gold)
            
    return result
