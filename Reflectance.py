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
		value = self.reflect.update()

	def update(self):
		self.value = self.get_color_reading()

	def get_value(self):
		return self.value