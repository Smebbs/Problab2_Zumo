import Sensob


class Ultra(Sensob):
    def __init__(self, sensors):
        super().__init__(sensors)

    def get_value(self):
        values = []
        for sensor in self.sensors:  # Update og append values
            sensor.update()
            values.append(sensor.getvalue)
        limit = 0.01  # placeholder verdi
        close = 0
        far = 0
        # Logikk for å sjekke om en av avstandene er mindre enn limit, -> Kollisjon inc.
        for value in values:
            if value < limit:
                current_sensor = self.sensors[values.index(value)]
                # Logikk for å bryte av, få motorer til å unngå kollisjon
            if value < close:
                closest = value
            if value > far:
                far = value
                # Bruk verdiene til å skape et overblikk av omgivelsene, gjelder bare ved flere
                #