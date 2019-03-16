from math import pi


class SetupConfiguration(object):
    def __init__(self, iterations: int = 100, quantity_of_detectors: int = 50, dispersion: int = 90,
                 image_path: str = 'images/Kropka.jpg', is_step_by_step: bool = True, step_size: int = 25):
        """
        :param iterations: how many different positions will be collected
        :param quantity_of_detectors:
        :param dispersion: a space between successive ones detectors
        :param image_path:
        :param is_step_by_step:
        :param step_size:
        """
        super(SetupConfiguration, self).__init__()
        self.iterations = iterations
        self.quantity_of_detectors = quantity_of_detectors
        self.dispersion = dispersion
        self.image_path = image_path
        self.is_step_by_step = is_step_by_step
        self.step_size = step_size

    def set_iterations(self, x: int):
        self.iterations = x

    def set_quantity_of_detectors(self, x: int):
        self.quantity_of_detectors = x

    def set_dispersion(self, x: int):
        """
        :param x: dispersion in degrees
        """
        self.dispersion = x

    def get_dispersion_in_radians(self):
        return self.dispersion / 360 * 2 * pi

    def set_step_size(self, x: int):
        self.step_size = x

    def set_is_step_by_step(self, x: bool):
        self.is_step_by_step = x
