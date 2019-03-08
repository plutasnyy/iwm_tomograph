from math import pi


class Configuration(object):
    def __init__(self, iterations: int = 100, quantity_of_detectors: int = 50, dispersion: int = 90,
                 image_path: str = 'images/Kropka.jpg',name: str = 'Kamil Plucisnki', id: str = '132307', des: str = 'none',filename: str = 'test.dcm'):
        """
        :param quantity_of_detectors:
        :param iterations: how many different positions will be collected
        :param dispersion: a space between successive ones detectors
        """
        self.iterations = iterations
        self.quantity_of_detectors = quantity_of_detectors
        self.dispersion = dispersion
        self.image_path = image_path
        self.name = name
        self.id = id
        self.des = des
        self.filename = filename

    def set_iterations(self, x: int):
        self.iterations = x

    def set_quantity_of_detectors(self, x: int):
        self.quantity_of_detectors = x

    def set_dispersion(self, x: int):
        """
        :param x: dispersion in degrees
        """
        self.dispersion = x

    def set_name(self, x: str):
        self.name = x
		
    def set_id(self,x: str):
        self.id = x
		
    def set_des(self,x: str):
        self.des = x
	
    def set_filename(self,x: str):
        self.filename = x
		
    def get_dispersion_in_radians(self):
        return self.dispersion / 360 * 2 * pi
