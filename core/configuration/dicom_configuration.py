class DicomConfiguration(object):
    def __init__(self, name: str = 'Kamil Plucisnki', id: str = '132307',
                 destination: str = 'none', file_name: str = 'test'):
        """
        :param name:
        :param id:
        :param destination:
        :param file_name:
        """
        super(DicomConfiguration, self).__init__()
        self.name = name
        self.id = id
        self.destination = destination
        self.file_name = file_name
        self.image = None

    def set_name(self, x: str):
        self.name = x

    def set_id(self, x: str):
        self.id = x

    def set_destination(self, x: str):
        self.destination = x

    def set_file_name(self, x: str):
        self.file_name = x
