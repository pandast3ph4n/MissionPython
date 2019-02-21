#Dette er det Første Kapitelet i boken
WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 350


def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550, 300))



def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 10
    elif keyboard.left:
        player_x -= 10
    elif keyboard.up:
        player_y -= 10
    elif keyboard.down:
        player_y += 10

clock.schedule_interval(game_loop, 0.03)

take_off_checklist = ["Put on suit",
                      "seal hatch",
                      "Check cabin pressure",
                      "fasten seatbelt"]

take_off_checklist.append("Tell Mission Control checks are complete")
take_off_checklist.remove("seal hatch")
take_off_checklist.insert(1, "seal hatch")
take_off_checklist[3] = "Take A Selfie"
take_off_checklist[3] = "Fasten Seatbelt"
del take_off_checklist[2]

spacewalk_checklist = [  "Put On Suit" ,
                        "Check Oxygen",
                        "Seal Helmet",
                        "Test Radio",
                        "Open airlock"]

skills_list = take_off_checklist + spacewalk_checklist
pr_list = ["Taking a Selfie",
            "Delivering lectures",
            "Doing TV inerviews",
            "Meeting the public"]

skills_list += pr_list
print(skills_list)

#Making Map
room_map = [ [1, 0, 0, 0, 0],
             [0, 0, 0, 2, 0],
             [0, 0, 0, 0, 0],
             [0, 3, 0, 0, 0],
             [0, 0, 0, 0, 4]
            ]
print(room_map[3][1])
room_map[0][0] = 5
print(room_map)