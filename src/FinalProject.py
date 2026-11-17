import json
import time

import pygame


#Important goals:
#TODO: Build the JSON reader and import the community made API.
#TODO: Create a code that reads the API out and formats it.
#TODO: Create a visual index that the program can use to display items with the pygame library.
#TODO: Create logic around modding/arcane restrictions (i.e. warframe mods go to warframes only, warframes must have an orokin reactor
# to have x amount of space, riven mods have a "creation" screen).
#TODO: Damage output logic.

#Advanced goals I might not make it to:
#TODO: Add a build description and commentary section. So the builds have notes one what they're able to do/are doing.
# For examples see the overframe builds and how users have set up their publicly available builds.
#TODO: Save builds feature.
#TODO: Custom icons for each warframe/companion.
#TODO: Add music player.
#TODO: Use a GUI module to make the window re-sizeable.
""" 
RULES: 
1. DO NOT ATTEMPT TO WRITE THIS ALONE. Ask for help when learning JSON and implementing it into the code.
2. Make it functional first, make it pretty/more advanced later.
3. Add comments. Always.
4. Always ask someone else to review the code.
5. Take breaks. Don't stare at the computer for hours on end frying your brain like you did with the last projects.
6. Remember to have fun.
"""

#this is for testing right now
#Darkblue to be easier on the eyes
BGCOLOR = DARKBLUE = (20, 36, 61)
WINWIDTH = 600
WINHEIGHT = 800


def main():
    pygame.init()
    pygame.display.set_caption("BuildBox.py")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (WINHEIGHT,WINWIDTH)
    screen = pygame.display.set_mode(resolution)
    running = True
    focused = True
    #inputrect
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        background = BGCOLOR
        screen.fill(background)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


if __name__ == "__main__":
    main()