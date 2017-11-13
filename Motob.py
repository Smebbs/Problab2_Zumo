class Motob:

    def __init__(self, motors):

        self.motors = motors
        self.value = None

    def update(self,recommendation):
        self.operationalize(recommendation)

    def operationalize(self,recommendation):
        #logikk for å velge riktig value-vektor
        value_new = None

        self.value = value_new
        self.motors.set_value(self.value)
