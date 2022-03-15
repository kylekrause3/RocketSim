from turtle import window_height 
from PIL import Image
import pythonGraph, random, math, rocket_ai_template, ga_helper

# CONSTANTS
WINDOW_WIDTH  = 1800
WINDOW_HEIGHT = 800

# Performance Variables
highscore = 0.0
frames = 0
frames_internal = 0
fuel_consumed = 0
crashes = 0
landings = 0

# Simulation Variables
turns_before_new = 5
currentrun = 0


# Terrain
ground_height = 0
ground_width = 0
water_height = 0
water_height_init = 0
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
rocket_gravity = 0

# Boat (i.e., Landing Pad)
boatx = 0
boatx_init = 0
boaty = 0

boatvel = 0
boatvel_init = 0
boatwidth = 0  # boat is wider than it is tall
boatheight = 0  # "


def initialize_simulation(generate_new_scenario):
    global highscore
    if generate_new_scenario:
        highscore = 0.0

    initialize_terrain(generate_new_scenario)
    initialize_boat(generate_new_scenario)
    initialize_rocket(generate_new_scenario)
     

def initialize_terrain(generate_new_scenario):
    global ground_height, ground_width, water_height, ground_y_coords, water_height_init
    ground_height = math.floor(WINDOW_HEIGHT * 0.3)
    ground_width = math.floor(WINDOW_WIDTH * 0.2)
    if generate_new_scenario:
        water_height_init = random.randint(50, ground_height)
    water_height = water_height_init

    ground_y_coords = [ground_height, water_height]


def initialize_rocket(generate_new_scenario):
    global rocketx, rockety, rocketvelx, rocketvely, rocketwidth, rocketheight, rocket_isboosting, rocket_gravity
    rocketwidth = 54
    rocketheight = 54
    rocketx = (ground_width / 2) - rocketwidth / 2
    rockety = WINDOW_HEIGHT - ground_height - rocketheight
    rocketvelx = 0.0
    rocketvely = 0.0

    rocket_isboosting = True
    rocket_gravity = 0.4


def initialize_boat(generate_new_scenario):
    global boatx, boatx_init, boaty,  boaty_init, boatvel, boatvel_init, boatheight, boatwidth

    boatheight = 48
    boatwidth = boatheight * 3
    if(generate_new_scenario == True):
        boatx_init = random.randint(ground_width, WINDOW_WIDTH - boatwidth)
        boatvel_init = random.randint(-3, 3)

    boatx = boatx_init
    boaty = WINDOW_HEIGHT - water_height - boatheight
    boatvel = boatvel_init


def erase_objects():
    pythonGraph.clear_window(pythonGraph.colors.BLACK)
    

def draw_objects():
    global frames, frames_internal
    frames += 1
    frames_internal += 1
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

    circle_radius = 5
    if rocket_thrusters[0] > 0.0:
        pythonGraph.draw_circle((rocketx + rocketwidth / 2) + rocketwidth / 8, rockety + rocketheight, circle_radius, pythonGraph.colors.YELLOW, True)
    if rocket_thrusters[1] > 0.0:
        pythonGraph.draw_circle(rocketx + rocketwidth / 2, rockety + rocketheight, circle_radius, pythonGraph.colors.YELLOW, True)
    if rocket_thrusters[2] > 0.0:
        pythonGraph.draw_circle((rocketx + rocketwidth / 2) - rocketwidth / 8, rockety + rocketheight, circle_radius, pythonGraph.colors.YELLOW, True)


def draw_boat():
    global boatx, boaty, boatwidth, boatheight
    pythonGraph.draw_image('boat.png', boatx, boaty, boatwidth, boatheight)


def update_objects():
    update_rocket()
    update_boat()


def update_rocket():
    global rocketx, rockety, rocketvelx, rocketvely, rocket_isboosting, rocket_thrusters, rocket_gravity, fuel_consumed, frames_internal

    if rocket_isboosting:
        for i in range(3):
            rocket_thrusters[i] = 0.0
        if not rockety < WINDOW_HEIGHT * .33:
            rocket_thrusters[1] = rocket_gravity + 0.3
        else:
            rocket_thrusters[1] = rocket_gravity / 2
            rocket_thrusters[2] = .25
        if rocketx >= ground_width:
            fuel_consumed = 0
            frames_internal = 0
            rocket_isboosting = False

    rocketvely = rocketvely - rocket_thrusters[1] + rocket_gravity
    rocketvelx += -1 * rocket_thrusters[0] + rocket_thrusters[2]

    rocketx += rocketvelx
    rockety += rocketvely

    if rocketvelx != 0:
        rocketvelx *= 0.985 # would do a delta time but that'd be too much for this simple of a project

    for i in range(3):
        fuel_consumed += rocket_thrusters[i]


def update_boat():
    global boatx, boatvel
    boatx += boatvel
    if boatx <= ground_width or boatx + boatwidth >= WINDOW_WIDTH:
        boatvel *= -1


def get_input():
    global boatvel, rocket_thrusters
    # run_autopilot(run_number, rocket_x, rocket_y, rocket_vx, rocket_vy, rocket_width, boat_x, boat_y, boat_width, gravity)
    for i in range(3):
        rocket_thrusters[i] = 0.0
    if not rocket_isboosting:
        ai_decision = rocket_ai_template.run_autopilot(currentrun, rocketx, rockety, rocketvelx, rocketvely, rocketwidth, boatx, boaty, boatwidth, rocket_gravity)
        for i in range(len(rocket_thrusters)):
            rocket_thrusters[i] = ai_decision[i]

    '''
    for i in range(3):
        rocket_thrusters[i] = 0.0

    if not rocket_isboosting:
        if pythonGraph.key_down('left'):
            rocket_thrusters[0] = 0.5
        if pythonGraph.key_down('up'):
            rocket_thrusters[1] = rocket_gravity + (rocket_gravity * 1.5)
        if pythonGraph.key_down('right'):
            rocket_thrusters[2] = 0.5'''


def draw_hud():
    # draw_text(text, x, y, color, font_size)
    font_size = 20
    line_spacing = 1
    pythonGraph.draw_text("High Score: " + str(highscore), 0, font_size, pythonGraph.colors.WHITE, font_size)
    pythonGraph.draw_text("Frames: " + str(frames), 0, font_size * 2 + line_spacing, pythonGraph.colors.WHITE, font_size)
    pythonGraph.draw_text("Fuel Consumed: " + str(math.floor(10 * fuel_consumed) / 10), 0, font_size * 3 + line_spacing, pythonGraph.colors.WHITE, font_size)
    pythonGraph.draw_text("x Velocity: " + str(math.floor(-10 * rocketvelx) / 10.0), 0, font_size * 4 + line_spacing, pythonGraph.colors.WHITE, font_size)
    pythonGraph.draw_text("y Velocity: " + str(math.floor(-10 * rocketvely) / 10.0), 0, font_size * 5 + line_spacing, pythonGraph.colors.WHITE, font_size)
    pythonGraph.draw_text("Crashes: " + str(crashes) + " Landings: " + str(landings), 0, font_size * 6 + line_spacing, pythonGraph.colors.WHITE, font_size)


def is_simulation_over():
    if not rocket_isboosting:
        if rocketx <= 0 or rocketx + rocketwidth >= WINDOW_WIDTH:
            return True
        if rocketx <= ground_width:
            if rockety >= WINDOW_HEIGHT - ground_height - rocketheight:
                return True
        if rockety >= WINDOW_HEIGHT - water_height - rocketheight:
            return True
    return False


def analyze_results():
    global landings, crashes, highscore
    score = 0
    rocketx_right = rocketx + rocketwidth
    boatx_right = boatx + boatwidth

    if rocketx >= boatx and rocketx_right <= boatx_right:
        score = 1000 - fuel_consumed - (frames_internal / 4) - (rocketvely * 4)
        landings += 1
    else:
        score = 0 - fuel_consumed - (frames_internal / 4) - (rocketvely * 4)
        crashes += 1

    if score > highscore:
        highscore = math.ceil(score)




def main():
    global currentrun
    pythonGraph.open_window(WINDOW_WIDTH, WINDOW_HEIGHT)
    pythonGraph.set_window_title("Rocket Sim")

    initialize_simulation(True)

    while pythonGraph.window_not_closed():
        if not is_simulation_over():
            erase_objects()
            draw_objects()
            get_input()
            update_objects()
        else:
            analyze_results()
            currentrun += 1
            if currentrun >= turns_before_new:
                currentrun = 0
                initialize_simulation(True)
            else:
                initialize_simulation(False)
        
        pythonGraph.update_window()


if __name__ == '__main__':
    main()

