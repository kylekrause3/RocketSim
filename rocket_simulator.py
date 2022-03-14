from turtle import window_height 
from PIL import Image
import pythonGraph, random, math

# CONSTANTS
WINDOW_WIDTH  = 1800
WINDOW_HEIGHT = 800

# Performance Variables

# Simulation Variables

# Terrain
ground_height = 0
ground_width = 0
water_height = 0
ground_y_coords = [0]

# Rocket
rocketx = 0
rockety = 0
rocketvelx = 0
rocketvely = 0
rocketheight = 0
rocketwidth = 0

rocket_isboosting = True
rocket_thrusters = [0.0, 0.0, 0.0]
rocket_gravity = 0.98

# Boat (i.e., Landing Pad)
boatx = 0
boatx_init = 0
boaty = 0
boaty_init = 0
boatvel = 0
boatvel_init = 0
boatwidth = 0  # boat is wider than it is tall
boatheight = 0  # "


def initialize_simulation(generate_new_scenario):
    initialize_terrain(generate_new_scenario)
    initialize_boat(generate_new_scenario)
    initialize_rocket(generate_new_scenario)
     

def initialize_terrain(generate_new_scenario):
    global ground_height, ground_width, water_height

    ground_height = math.floor(WINDOW_HEIGHT * 0.3)
    ground_width = math.floor(WINDOW_WIDTH * 0.2)
    water_height = random.randint(50, ground_height)
    print("Initialize Terrain Successfully Called")


def initialize_rocket(generate_new_scenario):
    global rocketx, rockety, rocketvelx, rocketvely, rocketwidth, rocketheight, rocket_isboosting
    rocketwidth = 54
    rocketheight = 54
    rocketx = (ground_width / 2) - rocketwidth / 2
    rockety = WINDOW_HEIGHT - ground_height - rocketheight
    rocketvelx = 0.0
    rocketvely = 0.0

    rocket_isboosting = True


def initialize_boat(generate_new_scenario):
    global boatx, boatx_init, boaty,  boaty_init, boatvel, boatvel_init, boatheight, boatwidth

    boatheight = 48
    boatwidth = boatheight * 3
    if(generate_new_scenario == True):
        boatx_init = random.randint(ground_width, WINDOW_WIDTH - boatwidth)
        boaty_init = WINDOW_HEIGHT - water_height - boatheight
        boatvel_init = random.randint(-3, 3)

    boatx = boatx_init
    boaty = boaty_init
    boatvel = boatvel_init



def erase_objects():
    pythonGraph.clear_window(pythonGraph.colors.BLACK)
    


def draw_objects():
    draw_terrain()
    draw_boat()
    draw_rocket()
    draw_hud()
  

def draw_terrain():
    # water first, then ground OVER water
    pythonGraph.draw_rectangle(0, WINDOW_HEIGHT - water_height, WINDOW_WIDTH, WINDOW_HEIGHT, pythonGraph.colors.BLUE, pythonGraph.colors.BLUE)
    pythonGraph.draw_rectangle(0, WINDOW_HEIGHT - ground_height, ground_width, WINDOW_HEIGHT, pythonGraph.colors.GREEN, pythonGraph.colors.GREEN)
    

def draw_rocket():
    global rocketx, rockety, rocketwidth, rocketheight, rocketvelx, rocketvely, rocket_thrusters
    pythonGraph.draw_image('rocket.png', rocketx, rockety, rocketwidth, rocketheight)

    # draw_circle(x, y, radius, color, filled, width)aw_circle(x, y, radius, color, filled, width)draw_circle(x, y, radius, color, filled, width)
    if rocket_thrusters[0]:
        # draw something on left
        pass
    if rocket_thrusters[1]:
        # draw something in center
        pass
    if rocket_thrusters[2]:
        # draw something on right
        pass

    '''2.  If the left thruster is firing:
        - Draw something on the left side of the rocket
    3.  If the right thruster is firing:
        - Draw something on the right side of the rocket
    4.  If the bottom thruster is firing:
        - Draw something on the bottom of the rocket'''


def draw_boat():
    global boatx, boaty, boatwidth, boatheight
    pythonGraph.draw_image('boat.png', boatx, boaty, boatwidth, boatheight)


def draw_hud():
    pass


def update_objects():
    update_rocket()
    update_boat()


def update_rocket():
    global rocketx, rockety, rocketvelx, rocketvely, rocket_isboosting, rocket_thrusters, rocket_gravity

    if rocket_isboosting:
        for i in range(3):
            rocket_thrusters[i] = 0.0
        if not rockety < WINDOW_HEIGHT * .5:
            rocket_thrusters[1] = 0.35
        else:
            rocket_thrusters[2] = 0.25
        if rocketx >= ground_width:
            rocket_isboosting = False

    rocketvely -= rocket_thrusters[1] + rocket_gravity
    rocketvelx += rocket_thrusters[0] + rocket_thrusters[2]

    rocketx += rocketvelx
    rockety += rocketvely


def update_boat():
    global boatx, boatvel
    boatx += boatvel
    if boatx <= ground_width or boatx + boatwidth >= WINDOW_WIDTH:
        boatvel *= -1



def get_input():
    pass


def is_simulation_over():
    return False


def analyze_results():
    pass


def main():
    pythonGraph.open_window(WINDOW_WIDTH, WINDOW_HEIGHT)
    pythonGraph.set_window_title("Rocket Sim")

    initialize_simulation(True)

    while pythonGraph.window_not_closed():
        if is_simulation_over() == False:
            erase_objects()
            draw_objects()
            get_input()
            update_objects()
        else:
            analyze_results()
            initialize_simulation(False)
        
        pythonGraph.update_window()


if __name__ == '__main__':
    main()

