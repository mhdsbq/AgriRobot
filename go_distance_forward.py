import dualMotorLib
import Rpi.GPIO as GPIO

DIAMETER_OF_WHEEL = 11 #cm
NUMBER_OF_STEPS_FOR_A_FULL_ROTATION = 200
STEP_PIN_LEFT = 26
STEP_PIN_RIGHT = 21
DIR_PIN_LEFT = 19
DIR_PIN_RIGHT = 20

STEP_DELAY = 0.05 #seconds

def go_distance_forward(distance):
    """" Move the robot forward a given distance in cm"""
    circumference_of_wheel = DIAMETER_OF_WHEEL * 3.14159265359
    number_of_steps = distance * NUMBER_OF_STEPS_FOR_A_FULL_ROTATION / circumference_of_wheel

    dual_motor = dualMotorLib.DualMotor( STEP_PIN_LEFT, STEP_PIN_RIGHT, DIR_PIN_LEFT, DIR_PIN_RIGHT )
    dual_motor.motors_go(clockwise=False, steps=number_of_steps, stepdelay=STEP_DELAY, verbose=False, initdelay=0)

    # GPIO.cleanup()
