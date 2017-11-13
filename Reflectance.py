import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("Sensob"))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("reflectance_sensors"))))


from Sensob import Sensob
from reflectance_sensors import ReflectanceSensors


class Reflectance(Sensob):
	def __init__(self):
		super().__init__("Reflectance")
		self.reflect = ReflectanceSensors()

	def get_sensor_current_value(self):
		value = self.reflect.update()
		return value

	def update(self):
		self.value = self.get_sensor_current_value()

	def get_value(self):
		return self.value