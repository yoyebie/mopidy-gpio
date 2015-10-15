import logging
import time

import RPi.GPIO as GPIO

logger = logging.getLogger(__name__)

class GPIOManager():

    def __init__(self, frontend, pins):

        self.frontend = frontend

        self.correctlyLoaded = False

        # Play Led
        self.led_pin = pins['playpin']

        try:
            # GPIO Mode
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.led_pin, GPIO.OUT)

            self.correctlyLoaded = True

        except RuntimeError:
            logger.error("MOPIDY_GPIO: Not enough permission " +
                         "to use GPIO. GPIO input will not work")

    def set_led(self, led_state):
        if self.correctlyLoaded:
            GPIO.output(self.led_pin, led_state)
