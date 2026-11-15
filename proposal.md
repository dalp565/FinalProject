# FinalProject

## Repository
Link: <https://github.com/dalp565/FinalProject.git>

## Description
I want to do research into programs that store data, more specifically building programs akin to inventory HUDS in video games. For the project I will use a problem I currently face in Warframe: understanding the modding system and buildcrafting. I will be working with player made public APIs and then taking the information they have on items and mods to create builds with certain types of effectiveness: "nuke" builds that remove enemies within seconds, survival builds, and enemy type specific builds that use a specific damage type to it's most effective degree.

## Features
- Feature 1
	- Inputs data from a public API resource that is player made.
      - Digital Extremes does not have a public facing open API that can be drawn from so I will be working with a player made resource instead: https://wiki.warframe.com/w/Mod/List_of_Mods
- Feature 2
	- View/Select available Mods/Arcanes.
      - Mods and Arcanes enchance warframes, weapons, companions, etc.
      - This feature should be able to display the modifications these items provide and make them selectable. (i.e. Focusing in on the item itself like a TCG card.)
- Feature 3 
	- Show the end effect of the modification combination.
      - Report on the end result in terms of additional weapon effectiveness. 

## Challenges
- Learn how to use Python to quesry an API resource to obtain data and read it.
- Understand how to properly use the data returned by the API and how to work with JSON data. (Study JSON and it's uses as well.)
- Design logic that can properly report on how modifications interact with each other to increase stats/weapon effectiveness and enforce restrictions.

## Outcomes
Ideal Outcome:
- Be able to output a final testable evaluation of a modification combination's effectiveness in terms of damage increase and costs associated with it. (Resources to build, damage output, damage types etc.)

Minimal Viable Outcome:
- Ability to read the data from the Warframe API and have the ability to view the modifications.
- Ability to select modifications and list them with their combined effectiveness.
- Output that information in a user readable format for their consumption.

## Milestones

- Week 1 - Understanding the Basics
  1. Read Warframe API modification information from the web site into Python. Research and study the JSON library.
  2. Build up the skill to view this information so we know what information is available per modification.

- Week 2 - Visualization.
  1. Create an interface to view the modifications and select them that is clean. This should be a window built with the pygame library.
  2. Create a rule set that controls what modifications can be selected and what other restrictions that are in play.

- Week 3 - Refinement (Final)
  1. Implement logic to calculate the improvements that a modification combination will result in.
  2. Report on the combination in a formated way that will list the selected modifications, improvement provided by each modifications, cost and then a summary at the end that reports the final improvement provided and overall cost.