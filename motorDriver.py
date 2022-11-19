import RPi.GPIO as GPIO

RIGHT_MOTOR_ENABLE_PIN = 22
RIGHT_MOTOR_DATA_ONE = 27
RIGHT_MOTOR_DATA_TWO = 17
LEFT_MOTOR_ENABLE_PIN = 13
LEFT_MOTOR_DATA_ONE = 26
LEFT_MOTOR_DATA_TWO = 19
PWM_FREQUENCY = 1000
INITIAL_PWM_DUTY_CYCLE = 100


def set_right_mode():
    """Set mode to Right"""
    GPIO.output(LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(LEFT_MOTOR_DATA_TWO, False)
    GPIO.output(RIGHT_MOTOR_DATA_ONE, False)
    GPIO.output(RIGHT_MOTOR_DATA_TWO, True)


def set_left_mode():
    """Set mode to Left"""
    GPIO.output(LEFT_MOTOR_DATA_ONE, False)
    GPIO.output(LEFT_MOTOR_DATA_TWO, True)
    GPIO.output(RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(RIGHT_MOTOR_DATA_TWO, False)


def set_reverse_mode():
    """Set mode to Reverse"""
    GPIO.output(RIGHT_MOTOR_DATA_ONE, False)
    GPIO.output(RIGHT_MOTOR_DATA_TWO, True)
    GPIO.output(LEFT_MOTOR_DATA_ONE, False)
    GPIO.output(LEFT_MOTOR_DATA_TWO, True)


def set_forward_mode():
    """Set mode to Forward"""
    GPIO.output(RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(RIGHT_MOTOR_DATA_TWO, False)
    GPIO.output(LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(LEFT_MOTOR_DATA_TWO, False)


def set_idle_mode():
    """Set mode to Idle"""
    set_right_motor_to_idle()
    set_left_motor_to_idle()


def set_right_motor_to_idle():
    """Sets the RIGHT motor to Idle state"""
    GPIO.output(RIGHT_MOTOR_DATA_ONE, True)
    GPIO.output(RIGHT_MOTOR_DATA_TWO, True)


def set_left_motor_to_idle():
    """Sets the LEFT motor to Idle state"""
    GPIO.output(LEFT_MOTOR_DATA_ONE, True)
    GPIO.output(LEFT_MOTOR_DATA_TWO, True)


def set_gpio_pins():
    """Sets the GPIO pins for the two motors"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RIGHT_MOTOR_DATA_ONE, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_DATA_TWO, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_DATA_ONE, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_DATA_TWO, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_ENABLE_PIN, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_ENABLE_PIN, GPIO.OUT)

