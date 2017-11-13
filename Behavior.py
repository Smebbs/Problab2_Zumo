class Behavior:

    def __init__(self,bbcon,sensobs):
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.motor_recommendation = None
        self.acive_flag = False
        self.halt_request = False
        self.priority = None
        self.match_degree = None
        #self.weight = self.priority * self.match_degree


    def consider_deactivation(self):

        return

    def consider_activation(self):

        return

    def sense_and_act(self):

        #Bruk sensobs til å lage motor_recommendation

        return

    def update(self):
        if self.acive_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()
        sense = self.sense_and_act()
        self.motor_recommendation = sense[0]
        self.match_degree = sense[1]
        self.halt_request = sense[2]
        self.weight = self.match_degree * self.priority