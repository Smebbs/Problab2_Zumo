class Motob:

    def __init__(self, motors):

        self.motors = motors
        self.value = None

    def update(self,recommendation):
        self.operationalize(recommendation)

    def operationalize(self,recommendation):

        #logikk for å velge riktig value-vektor
        if recommendation == 'Turn_180_L':
            for motor in self.motors:
                motor.stop()
                motor.backward(dur=0.5)
                motor.left(dur=0.5)
                motor.forward()
                
        if recommendation == 'Turn_180_R':
            for motor in self.motors:
                motor.stop()
                motor.backward(dur=0.5)
                motor.right(dur=0.5)
                motor.forward()
                
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
