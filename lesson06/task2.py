class Road:
    def __init__(self, lenght, widght):
        self._lenght = lenght
        self._width = widght

    def road_square(self):
        return self._lenght * self._width


class Asphalt(Road):
    def __init__(self, lenght, widght, mass_per_cm, thin):
        super().__init__(lenght, widght)
        self.mass_per_cm = mass_per_cm
        self.thin = thin

    def asphalt_mass(self):
        return self.road_square() * self.mass_per_cm * self.thin


highway = Asphalt(20, 5000, 25, 5)
print(highway.asphalt_mass())
