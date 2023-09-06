# Quick-Hair-Guide-Tool
NOTE: This is an early version of the tool (ver.0.0.1). 

This tool is used to quickly create a hair guide from the hair geometry.

TO INSTALL THE TOOL:
1. Install the file and put it in the Maya script folder: C:\<users>\Documents\maya\<version>\scripts
2. Open Maya and copy-paste this code snipped into the script editor:

import importlib

from quickHairGuideGen import quickHairGuide

importlib.reload(quickHairGuide)

3. Run the script, or, add the script to Maya shelf by going to script editor and press: File> Save script to Shelf.

HOW TO:
NOTE: Make sure that your hair geo does not have any start, or end caps.
1. Select Single Edge:
   i. Select one vertical edge of your hair geo and press the Select Edge Loop button.
   
2. Create Guide:
   i. Press the Create button to create a hair guide from the edge loop detected earlier.
   
3. Match all Curve Direction:
   i. Select all the guides generated and press the Display button to view all the guide's CVs.
   ii. If any unmatched guide's CV is found, select the guide and press the Reverse button.
   
5. Rename and Group the Hair:
   NOTE: For the serial number i.e. 1, 2, 3, ..., n to appear in the name, type '{num}' into the name. eg. hairStrand{num}_crv.
   i. Enter the name pattern of the guide in the name text field.
   ii.   Enter the group name of the guides into the group text field.
   iii. Press the Rename and Group button. 
