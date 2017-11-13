class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        behavior_winner = None
        weight_winner = 0
        for behavior in self.bbcon.behaviors_active:
            if behavior.weight > weight_winner:
                behavior_winner = behavior
                weight_winner = behavior.weight