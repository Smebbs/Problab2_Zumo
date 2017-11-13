sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("motors"))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("zumo_button"))))

from motors import Motors
from zumo_button import ZumoButton


class Motob:
	def __init__(self, motors):

		self.motors = motors
		self.value = None

	def update(self, recommendation):
		self.operationalize(recommendation)

	def operationalize(self, recommendation):
		# todo: Sette motorsfilene slik at self.persist ikke stopper automatisk etter duration, hvis ikke stopper robotten etter hver command
		if recommendation == 'Turn_Color':
			self.motors.stop()
			angle = None  # Sett inn value utfra hvilke sensorer som detekterer linjen
			self.motor.set_value(angle)
		if recommendation == 'Turn_Line':
			self.motors.stop()
			angle = None  # Sett inn value utfra hvilke sensorer som detekterer linjen
			self.motor.set_value(angle)
		if recommendation == 'Standard':
			self.motors.stop()
			angle = None  # Sett inn value utfra hvilke sensorer som detekterer linjen
			self.motor.set_value(angle)


ZumoButton().wait_for_press()
motor = Motob(Motors)
motor.operationalize("Turn_Color")
