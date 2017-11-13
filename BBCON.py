import time



class BBCON_:

    def __init__(self, behaviors, sensobs, motobs, arbitrator):

        self.behaviors_all = behaviors #Alle behaviors
        self.behaviors_active = [] #Aktive behaviors for syklusen
        self.sensobs_all = sensobs #Alle sensobs
        self.sensobs_active = [] #Aktive sensobs for syklusen
        self.motobs = motobs #Motobs tilknyttet bbcon
        self.arbitrator = arbitrator #Arbitrator tilknyttet bbcon
        self.time = 0 #Variabel for tid, økes += 1 ved hver syklus, halter ved time = 50
        self.future_collision = False # Betegner hvorvidt ultralydsensor har oppdaget et objekt lang unna

    # Add og Remove metoder for behavior og sensob
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
        
        #Update sensobs og behavior
        for sensob in self.sensobs_active:
            sensob.update()

        for behavior in self.behaviors_active:
            behavior.update()
        
        #Arbitrator velger action, returnerer aksjon + halt_flag
        recommendation,halt = self.arbitrator.choose_action
        
        #Eneste true halt_flag forekommer ved time = 50
        if halt: 
            self.motobs.update('Halt')
        
        #Oppdater motorer
        self.motobs.update(recommendation)
        
        #La en syklus gå
        time.sleep(0.5) 
        
        #Reset sensobs, klar for ny syklus
        for sensob in self.sensobs_active:
            sensob.reset()

