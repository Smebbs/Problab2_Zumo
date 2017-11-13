class Motob:

    def __init__(self, motors):

        self.motors = motors
        self.value = None

    def update(self,recommendation):
        self.operationalize(recommendation)

    def operationalize(self,recommendation):

        #todo: Sette motorsfilene slik at self.persist ikke stopper automatisk etter duration, hvis ikke stopper robotten etter hver command
        if recommendation == 'Halt':
            for motor in self.motors:
                motor.stop()
                time.sleep(100)
        if recommendation == 'Turn_Color':
            for motor in self.motors:
                motor.stop()
                angle = None # Sett inn value utifra fargekonsentrasjon i bilde eller noe
                motor.set_value(angle)
        if recommendation == 'Turn_Line':
            for motor in self.motors:
                motor.stop()
                angle = None # Sett inn value utfra hvilke sensorer som detekterer linjen
                motor.set_value(angle)
        if recommendation == 'Standard':
            for motor in self.motors:
                motor.forward()
