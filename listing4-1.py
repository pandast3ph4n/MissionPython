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
        ["The airlock", 13, 5, True, False],
        ["The engineering lab", 13, 13, False, False],
        ["Poodle Misson Control", 9, 13, False, True],
        ["The viewing gallery", 9, 15, False, False],
        ["The crew bathroom", 5, 5, False, False],
        ["The airlock entery bay", 7, 11, True, True],
        ["Left elbow room", 9, 7, True, False],
        ["Right elbow room", 7, 13, True, True],
        ["The science lab", 13, 13, False, True],
        ["The greenhouse", 13, 13, True, False],
        [PLAYER_NAME + "'s sleeping qaurters", 9, 11,  False, False],
        ["West corridor", 15, 5, True, True],
        ["The briefing room",7, 13,False, True]
        ["The crew's community room", 11, 13, True, False]
        ["Main Misson Control", 14, 14, False, False]
        ["The sick bay", 12, 7, True, False]
        ["West corridor", 9, 7, True, False]
        ["Utilities control room", 9, 9, False, True]
        ["Systems engneering bay", 9, 11, False, False]
        ["Security portal to Misson Control", 7, 7, True, False]
        [FREIND1_NAME + "'s sleeping qaurters", 9, 11, True, True],
        [FREIND2_NAME + "'s sleeping qaurters", 9, 11, True, True],
        ["The pipeworks", 13, 11, True, False]
        ["The chief scientist's office", 9, 7, True, True]
        ["the robot workshop", 9, 11, True, False]
        ]


assert len(GAME_MAP)-1 == MAP_SIZE, "Map size and GAME_MAP don't match"

["The dusty planet surface", 13, 13, True, True]

def get floor_type():
    if  current_room in outdoor_rooms:
        return 2
    else:
        return 0

def generate_map():

