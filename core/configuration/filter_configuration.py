class FilterConfiguration(object):
    def __init__(self, gamma: float = 0.4, gauss: float = 0.6):
        """
        :param gamma:
        :param gauss:
        """
        super(FilterConfiguration, self).__init__()
        self.gamma = gamma
        self.gauss = gauss

    def set_gamma(self, x: float):
        self.gamma = x

    def set_gauss(self, x: float):
        self.gauss = x
