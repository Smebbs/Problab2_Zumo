from Sensob import Sensob
import os
from PIL import Image


class Cam(Sensob):
    def __init__(self, img_width=128, img_height=96, img_rot=0):
                super().__init__("Camera")
                self.img_width=img_width
                self.img_height=img_height
                self.img_rot=img_rot

    def get_image(self):
        os.system('raspistill -t 1 -o image.png -w "' + str(self.img_width) + '" -h "' + str(self.img_height) + '" -rot "' + str(self.img_rot) + '"')
        return Image.open('image.png').convert('RGB')


    def update(self):
        image = self.get_image()
        self.value = image
