from src.analyser import *


def extractDataFromFile()->dict:
    rawFileString = getStatsFile()
    jsonDict = convertJsonToDict(rawFileString)
    convertedDict = extractExportData(jsonDict)
    resultsDict = computeResultDict(convertedDict)
    return resultsDict

def printResults(results:dict)->str:
    for key, value in results.items():
        print(key)
        print(f"\t{value.xp} XP")
        print(f"\t{value.gold} Gold")
        print(f"\t{value.seconds} Seconds")
        print(f"\t{value.xp/value.seconds} XP/s")
        print(f"\t{value.gold/value.seconds} Gold/s")

if __name__ == "__main__":
    resultsDict = extractDataFromFile()
    printResults(resultsDict)
    pass

