#Dette er det Fjerde Kapitelet i boken

["The airlock", 13, 5, True, False]

import time, random, math

WIDTH = 800
HEIGHT = 800

PLAYER_NAME = "Chelby"
FREIND1_NAME = "Any"
FREIND2_NAME = "Bob"
current_room = 31

top_left_x = 100
top_left_y = 150
DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

MAP_WIDTH = 5
MAP_HEIGHT =10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [ ["Room 0 - where unsed objects are kept", 0, 0, False, False] ]

outdoor_rooms = range(1, 26)
for planetsecorts in range (1, 26):
    GAME_MAP.append( ["The dusty planet surface", 13, 13, True, True] )

GAME_MAP += [
        #["room name", height, width, top exit?, right exit?]
        ["The airlock" 13, 5, True, False],
        ["The engineering lab", 13, 13, False, False],
        ["Poodle Misson Control", 9, 13, False, True],
        ["The viewing gallery", 9, 15, False, False],
