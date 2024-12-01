## State
!! WARNING !!
This tool works, but:
Since the current Data-State from crpg-site doesn't contain lastSpawn- or serverLeave-times this tool is only accurate when analysing 'block-data'.
I am working on PRs to fix that and integrate this toll into the CRPG website when i can.

## About this
CRPG now has a 'Stats'-Tab.
It sadly has no direct calculation or export to quantify the rewards for your time spend.
Therefore i wrote this thingy.

## Setting it up
Install [python](https://www.python.org/)
Clone the repo
through idle: open main.py and press f5
though cli: python .\main.py  (when opened temrinal in project folder)

## How-To-Use
1. Go to [https://c-rpg.eu/](https://c-rpg.eu/)
2. Go to 'Stats'-Tab on the 'Characters'-Page
3. Press F12
4. Go to 'Network'-Tab in the Console
5. (optinal) Clear it for better overview
6. Select the Timespan you want to export on the 'Stats'-Tab
7. Click on the 'GET' response and navigate to its' 'Response'-Tab:
   ![grafik](https://github.com/user-attachments/assets/c326a3bf-7fcb-4f49-9b5f-acac38283995)
9. Rightclick onto 'data' and click on 'Copy all'
10. Replace the contents of the 'raw_data.json' in the project with your clipboard-contents (select all and ctrl+v or rightclick->paste)
11. Run the 'main' python file -> DONE
