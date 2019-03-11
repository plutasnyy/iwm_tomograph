class FilterConfiguration(object):
    def __init__(self, gamma: float = 0.4, gauss: float = 0.6, is_filter: bool = True):
        """
        :param gamma:
        :param gauss:
        :param is_filter:
        """
        super(FilterConfiguration, self).__init__()
        self.is_filter = is_filter
        self.gamma = gamma
        self.gauss = gauss

    def set_gamma(self, x: float):
        self.gamma = x

    def set_gauss(self, x: float):
        self.gauss = x

    def set_filter(self, x: bool):
        self.is_filter = x
