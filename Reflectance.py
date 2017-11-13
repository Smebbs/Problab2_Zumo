import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("Sensob"))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("reflectance_sensors"))))


from Sensob import Sensob
from basic_robot import reflectance_sensors


class Reflectance(Sensob):
	def __init__(self, sensors):
		super.__init__(self, sensors)
		self.reflect = reflectance_sensors.ReflectanceSensors()

	def get_sensor_current_value(self):
		return self.reflect.update()

	def update(self):
		return mean(self.get_color_reading())

	def get_value(self):
		return self.value


def mean(array):
	return sum(array) / float(len(array))


sensor = Reflectance
while True:
	print(sensor.update())