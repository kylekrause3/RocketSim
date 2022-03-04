from turtle import window_height
import pythonGraph, random, math

# CONSTANTS
WINDOW_WIDTH  = 1800
WINDOW_HEIGHT = 800

# Performance Variables

# Simulation Variables

# Terrain
GROUND_HEIGHT = 0
GROUND_WIDTH = 0
WATER_HEIGHT = 0
ground_y_coords = [0]

# Rocket

# Boat (i.e., Landing Pad)


def initialize_simulation(generate_new_scenario):
    initialize_terrain(generate_new_scenario)
    initialize_boat(generate_new_scenario)
    initialize_rocket(generate_new_scenario)
     

def initialize_terrain(generate_new_scenario):
    global GROUND_HEIGHT, GROUND_WIDTH, WATER_HEIGHT

    GROUND_HEIGHT = math.floor(WINDOW_HEIGHT * 0.3)
    GROUND_WIDTH = math.floor(WINDOW_WIDTH * 0.2)
    WATER_HEIGHT = random.randint(50, GROUND_HEIGHT)
    print("Initialize Terrain Successfully Called")


def initialize_boat(generate_new_scenario):
    print("Initialize Boat Successfully Called")


def initialize_rocket(generate_new_scenario):
    print("Initialize Rocket Successfully Called")


def erase_objects():
    pythonGraph.clear_window(pythonGraph.colors.BLACK)
    


def draw_objects():
    draw_terrain()
    draw_boat()
    draw_rocket()
    draw_hud()
  

def draw_terrain():
    # water first, then ground OVER water
    pythonGraph.draw_rectangle(0, WINDOW_HEIGHT - WATER_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, pythonGraph.colors.BLUE, pythonGraph.colors.BLUE)
    pythonGraph.draw_rectangle(0, WINDOW_HEIGHT - GROUND_HEIGHT, GROUND_WIDTH, WINDOW_HEIGHT, pythonGraph.colors.GREEN, pythonGraph.colors.GREEN)
    
   

def draw_boat():
    pass


def draw_rocket():
    pass


def draw_hud():
    pass


def update_objects():
    pass


def update_rocket():
    pass


def update_boat():
    pass


def get_input():
    pass


def is_simulation_over():
    return False


def analyze_results():
    pass
        

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