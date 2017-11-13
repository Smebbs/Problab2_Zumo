from Behavior import Behavior
from Cam import Cam
from PIL import Image


class Search_Color(Behavior):
    def __init__(self, bbcon, sensobs):
        super().__init__(bbcon, sensobs)
        self.time = 0

    def consider_activation(self):
        if self.time == 0:
            self.time += 1
            return False
        elif self.time == 1:
            self.time = 0
            return True

    def consider_deactivation(self):
        return True

    def sense_and_act(self):
        image = self.sensobs.get_value()
        loaded = image.load()
        motor_recommendation = 'Turn_Color'
        match_degree = 1
        halt_request = False
        sigma_x = 0
        n_points = 0
        width = self.sensobs.img_width
        height = self.sensobs.img_height
        for x in range(width):
            for y in range(height):
                r, g, b = loaded[x, y]
                # remove red from the pic
                if r < 100 and g > 120 and b < 100:
                    sigma_x += x
                    n_points += 1

        if n_points != 0:
            x = int(sigma_x/n_points)
            print(x)

        return motor_recommendation, match_degree, halt_request


if __name__ == "__main__":
    cam = Cam()
    # Temp:
    cam.update()
    behav = Search_Color("bbcon", cam)
    behav.sense_and_act()