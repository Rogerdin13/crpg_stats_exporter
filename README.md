## About this
STATUS: WIP

CRPG now has a 'Stats'-Tab.
It sadly has no direct calculation or export to quantify the rewards for your time spend.
Therefore i wrote this thingy.

!! WARNING !!
Since currently this tool cannot cross-reference server join times or compute pauses in playing it currently only works on data, that is played in one sitting

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
