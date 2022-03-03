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


# --------------------------------------------------------------
# Initializes the Simulation
# --------------------------------------------------------------
def initialize_simulation(generate_new_scenario):
    initialize_terrain(generate_new_scenario)
    initialize_boat(generate_new_scenario)
    initialize_rocket(generate_new_scenario)
     

# --------------------------------------------------------------
# Initializes the Terrain
# --------------------------------------------------------------
def initialize_terrain(generate_new_scenario):
    global GROUND_HEIGHT, GROUND_WIDTH, WATER_HEIGHT

    GROUND_HEIGHT = random.randint(250, 350)
    GROUND_WIDTH = random.randint(75, 100)
    WATER_HEIGHT = GROUND_HEIGHT - 50
    print("Initialize Terrain Successfully Called")


# --------------------------------------------------------------
# Initializes the Boat
# --------------------------------------------------------------
def initialize_boat(generate_new_scenario):
    print("Initialize Boat Successfully Called")


# --------------------------------------------------------------
# Initializes the Rocket
# --------------------------------------------------------------
def initialize_rocket(generate_new_scenario):
    print("Initialize Rocket Successfully Called")


# --------------------------------------------------------------
# Draws all of the in game objects
# --------------------------------------------------------------
def erase_objects():
    pass


# --------------------------------------------------------------
# Draws all of the in game objects
# --------------------------------------------------------------
def draw_objects():
    pass
  

# --------------------------------------------------------------
# Draws the Terrain
# --------------------------------------------------------------
def draw_terrain():
    pass
   

# --------------------------------------------------------------
# Draws the Boat
# --------------------------------------------------------------
def draw_boat():
    pass


# --------------------------------------------------------------
# Draws the Rocket (and Thrusters)
# --------------------------------------------------------------
def draw_rocket():
    pass


# --------------------------------------------------------------
# Draws the On Screen Text
# --------------------------------------------------------------
def draw_hud():
    pass


# --------------------------------------------------------------
# Updates all animated objects
# --------------------------------------------------------------
def update_objects():
    pass


# --------------------------------------------------------------
# Updates the Rocket
# --------------------------------------------------------------
def update_rocket():
    pass


# --------------------------------------------------------------
# Updates the Landing Pad / Boat
# --------------------------------------------------------------
def update_boat():
    pass


# --------------------------------------------------------------
# Checks for Manual (or eventually) AI Input
# --------------------------------------------------------------
def get_input():
    pass


# --------------------------------------------------------------
# Detects if the Rocket has hit the ground or a boundry
# --------------------------------------------------------------
def is_simulation_over():
    return False


# --------------------------------------------------------------
# Analyzes the Results of the Simulation
# --------------------------------------------------------------
def analyze_results():
    pass
        
        
# -----------------------------------------------------
# "Main Program"
# -----------------------------------------------------
pythonGraph.open_window(WINDOW_WIDTH, WINDOW_HEIGHT)
pythonGraph.set_window_title("Rocket Sim")  

# Initializes the Simulation At Least Once
initialize_simulation(True)
    
# Main "Game Loop"
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