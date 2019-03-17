class FilterConfiguration(object):
    def __init__(self, is_filter: bool = True):
        """
        :param is_filter:
        """
        super(FilterConfiguration, self).__init__()
        self.is_filter = is_filter

    def set_filter(self, x: bool):
        self.is_filter = x
