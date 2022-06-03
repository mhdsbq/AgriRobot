import sys
import time
import RPi.GPIO as GPIO

class StopMotorInterrupt(Exception):
    """ Stop the motor """
    pass

class DualMotor(object):
    def __init__(self, step_left_pin, step_right_pin,dir_left_pin, dir_right_pin) -> None:

        self.step_left_pin = step_left_pin
        self.step_right_pin = step_right_pin

        self.dir_left_pin = dir_left_pin
        self.dir_right_pin = dir_right_pin

        self.stop_motor = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def motor_stop(self):
        """stop motor intercept"""
        self.stop_motor = True

    def motors_go(self, clockwise=True, steps=200, stepdelay=.005, verbose=False, initdelay=0):
        """ motor_go,  moves stepper motor based on 5 inputs
         (1) clockwise, type=bool default=False
         help="Turn stepper counterclockwise"
         (2) steps, type=int, default=200, help=Number of steps sequence's
         to execute. Default is one revolution , 200 in Full mode.
         (3) stepdelay, type=float, default=0.05, help=Time to wait
         (in seconds) between steps.
         (4) verbose, type=bool  type=bool default=False
         help="Write pin actions",
         (5) initdelay, type=float, default=0S, help= Intial delay after
         GPIO pins initialized but before motor is moved.
        """
        self.stop_motor = False
        # setup GPIO
        GPIO.setup(self.step_left_pin, GPIO.OUT)
        GPIO.setup(self.step_right_pin, GPIO.OUT)
        GPIO.setup(self.dir_left_pin, GPIO.OUT)
        GPIO.setup(self.dir_right_pin, GPIO.OUT)
        GPIO.output(self.dir_right_pin, clockwise)
        GPIO.output(self.dir_left_pin, clockwise)

        try:
            for i in range(steps):
                if self.stop_motor:
                    raise StopMotorInterrupt
                else:
                    GPIO.output(self.step_left_pin, True)
                    GPIO.output(self.step_right_pin, True)
                    time.sleep(stepdelay)
                    GPIO.output(self.step_left_pin, False)
                    GPIO.output(self.step_right_pin, False)
                    time.sleep(stepdelay)
                    if verbose:
                        print(f"Steps count {i+1}")
        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib:")
        except StopMotorInterrupt:
            print("Stop Motor Interrupt : RpiMotorLib: ")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")            
        
        else:
            # print report status
            if verbose:
                print("\nRpiMotorLib, Motor Run finished, Details:.\n")
                print(f"Clockwise = {clockwise}")
                print(f"Number of steps = {steps}")
                print(f"Step Delay = {stepdelay}")
                print(f"Intial delay = {initdelay}")
                print(f"Size of turn in degrees = {degree_calc(steps)}")

    

def degree_calc(steps):
    """
    Calculate the size of turn based on steptype and steps
    """
    degree = 360 / 200 * steps
    return degree