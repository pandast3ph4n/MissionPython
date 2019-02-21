#Dette er det Tredde Kapitelet i boken
room_map = [ [1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]
           ]
print(room_map)

for y in range(7):
    print(room_map[y])


for y in range(7):
    for x in range(5):
        print(room_map[y][x], end="")
    print()

WIDTH = 800 # window size
HEIGHT = 800

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar]

room_height = 7
room_width = 5

def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw,
                (top_left_x + (x*30),
                top_left_y + (y*30) - image_to_draw.get_height()))
