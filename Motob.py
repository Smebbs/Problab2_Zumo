import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("motors"))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("zumo_button"))))

from motors import Motors
from zumo_button import ZumoButton

import time
TURN_90 = 0.22


class Motob:
    def __init__(self, motors):

        self.motors = motors
        self.value = None

    def update(self, recommendation):
        self.operationalize(recommendation)


    def operationalize(self, recommendation):
        # todo: Sette motorsfilene slik at self.persist ikke stopper automatisk etter duration, hvis ikke stopper robotten etter hver command
        if recommendation == 'S':
            self.motors.stop()
        if recommendation == 'N':
            self.motors.set_value([0.25, 0.25])
        if recommendation == 'NE':
            self.motors.set_value([1, -1], TURN_90/2)
        if recommendation == 'E':
            self.motors.set_value([1, -1], TURN_90)
        if recommendation == 'NW':
            self.motors.set_value([-1, 1], TURN_90/2)
        if recommendation == 'W':
            self.motors.set_value([-1, 1], TURN_90)
        if recommendation == 'R':
            self.motors.set_value([-1, -1], TURN_90/2)
        if recommendation == 'B':
            self.motors.set_value([-0.5, -0.5])
            self.motors.set_value([1, -1], TURN_90*2)


if __name__ == "__main__":
    ZumoButton().wait_for_press()
    motor = Motob(Motors())
    motor.operationalize("B")
    """
    motor.operationalize("N")
    time.sleep(1)
    motor.operationalize("S")
    time.sleep(1)
    motor.operationalize("NW")
    time.sleep(1)
    motor.operationalize("W")
    time.sleep(1)
    motor.operationalize("E")
    motor.operationalize("NE")
    time.sleep(1)
    """