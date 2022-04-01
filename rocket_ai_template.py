# ---------------------------------------------------------------------
# PEX 3 Rocket AI
# Author:  YOUR NAME GOES HERE
# Course: CS110Z, Spring 2020
# ---------------------------------------------------------------------
import pythonGraph, random, ga_helper

# --------------------------------------------------------------
# This line starts the genetic algorithm
# Parameters (in order)
#   1.  Number of "AIs" that can survive each generation
#   2.  Number of children AIs that can be produced
#   3.  Max horizontal velocity
#   4.  Max vertical velocity
# --------------------------------------------------------------
#pex3_helper.initialize_genetic_algorithm(4, 2, 10.0, 10.0)

# --------------------------------------------------------------
# This line sets the AI you want to submit to the competition
# When you are done with the PEX, uncomment this line and
# replace the parameters with the values of your "best" AI
# --------------------------------------------------------------
#pex3_helper.use_ai_configuration(HORIZONTAL_THRUST_AMOUNT, VERITCAL_THRUST_AMOUNT, MAX_HORIZONTAL_SPEED, MAX_VERTICAL_SPEED)


# --------------------------------------------------------------
# Returns the Name of the Student
# --------------------------------------------------------------
def get_student_name():
    return "your_name_goes_here"


# --------------------------------------------------------------
# Runs the AI
# --------------------------------------------------------------
def run_autopilot(run_number, rocket_x, rocket_y, rocket_vx, rocket_vy, rocket_width, boat_x, boat_y, boat_width, gravity):
    # This tuple tells your simulation which thrusters to fire
    # The first number is the left thruster, the second is the right, and the third is up
    max_vy_down = gravity * 3
    max_vy_up = gravity * 1.5

    thrust_up = 0
    thrust_right = 0
    thrust_left = 0

    if rocket_vy >= max_vy_down:
        thrust_up = gravity + (gravity * 1.5)

    return (0.0, 0.0, 0.0)


'''
    for i in range(3):
        rocket_thrusters[i] = 0.0

    if not rocket_isboosting:
        if pythonGraph.key_down('left'):
            rocket_thrusters[0] = 0.5
        if pythonGraph.key_down('up'):
            rocket_thrusters[1] = rocket_gravity + (rocket_gravity * 1.5)
        if pythonGraph.key_down('right'):
            rocket_thrusters[2] = 0.5
'''
