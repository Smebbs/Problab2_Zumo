import time

class BBCON_:
    def __init__(self, behaviors, sensobs, motobs, arbitrator):

        self.behaviors_all = behaviors
        self.behaviors_active = []
        self.sensobs_all = sensobs
        self.sensobs_active = []
        self.motobs = motobs
        self.arbitrator = arbitrator
        self.future_collision = False

    def add_behavior(self, behavior):
        self.behaviors_all.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs_all.append(sensob)

    def activate_behavior(self, behavior):
        if behavior in self.behaviors_all:
            self.behaviors_active.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.behaviors_active:
            self.behaviors_active.remove(behavior)
    
    def activate_sensob(self, sensob):
        if sensob in self.sensobs_all:
            self.sensobs_active.append(sensob)

    def deactivate_sensob(self, sensob):
        if sensob in self.sensobs_active:
            self.sensobs_active.remove(sensob)

    def run_one_timestep(self):

        for sensob in self.sensobs_active:
            sensob.update()

        for behavior in self.behaviors_active:
            behavior.update()

        recommendation,halt = self.arbitrator.choose_action
        if halt:
            #Stopp roboten, end run
            return

        self.motobs.update(recommendation)

        time.sleep(0.5)

        for sensob in self.sensobs_active:
            sensob.reset()

