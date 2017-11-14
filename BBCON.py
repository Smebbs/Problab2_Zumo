import time
from Cam import Cam
from Reflectance import Reflectance
from Ultra import Ultra
from Arbitrator import Arbitrator
from Behavior_Avoid_Line import Avoid_Line
from Behavior_Drive_Around import Drive_Around
from Behavior_Kollisjon import Kollisjon
from Behavior_Search_Color import Search_Color
from Motob import Motob
from Motors import Motors
from zumo_button import ZumoButton
from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors


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
        recommendation,halt = self.arbitrator.choose_action()
        print(recommendation, halt)
        
        #Eneste true halt_flag forekommer ved time = 50
        if halt: 
            self.motobs.update('Halt')
        
        #Oppdater motorer
        self.motobs.update(recommendation)
        
        #La en syklus gå
        time.sleep(0.2)
        
        #Reset sensobs, klar for ny syklus
        for sensob in self.sensobs_active:
            sensob.reset()


if __name__ == "__main__":
    ZumoButton().wait_for_press()
    cam = Cam()
    ref = Reflectance()
    ultra_sensor = Ultrasonic()
    ult = Ultra(ultra_sensor)
    mot = Motors()
    mob = Motob(mot)
    arb = Arbitrator()
    bsc = Search_Color(cam)
    bsc.priority = 2
    bav = Avoid_Line(ref)
    bav.priority = 3
    bda = Drive_Around()
    bda.priority = 1
    bak = Kollisjon(ult)
    bak.priority = 3

    bbcon = BBCON_([bsc, bav, bda, bak], [cam, ref, ult], mob, arb)
    bda.add_bbcon(bbcon)
    for beh in bbcon.behaviors_all:
        bbcon.activate_behavior(beh)
    for seh in bbcon.sensobs_all:
        bbcon.activate_sensob(seh)
    arb.set_bbcon(bbcon)


    time.sleep(2)
    for i in range(50):
        bbcon.run_one_timestep()
