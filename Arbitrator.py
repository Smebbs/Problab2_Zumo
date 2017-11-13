class Arbitrator:
    def __init__(self):
        self.bbcon = None

    def set_bbcon(self, bbcon):
        self.bbcon = bbcon
        #self.file = self.file = open('log.txt', 'w')
        #self.file.write("Start of log:")

    def choose_action(self):
        behavior_winner = None
        weight_winner = 0
        #self.file.write("-------------------------")
        #self.file.write("All actions and weights:")

        for behavior in self.bbcon.behaviors_active:
            #self.file.write("Behaviour recommendation:", behavior.motor_recommendation, "\tBehaviour weight:",behavior.weight)
            if behavior.weight > weight_winner:
                behavior_winner = behavior
                weight_winner = behavior.weight

        #self.file.write("Behaviour winner:", behavior_winner.motor_recommendation)
        #self.file.write("-------------------------")
        return behavior_winner.motor_recommendation, behavior_winner.halt_request
