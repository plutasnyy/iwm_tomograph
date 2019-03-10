from configuration.dicom_configuration import DicomConfiguration
from configuration.filter_configuration import FilterConfiguration
from configuration.setup_configuration import SetupConfiguration


class ConfigurationAggregator(SetupConfiguration, FilterConfiguration, DicomConfiguration):
    def __init__(self, **kwargs):
        """
        :param iterations: how many different positions will be collected
        :param quantity_of_detectors:
        :param dispersion: a space between successive ones detectors
        :param image_path:
        :param name:
        :param id:
        :param destination:
        :param file_name:
        :param gamma:
        :param gauss:
        """
        super().__init__()
        allowed_keys = ['iterations', 'quantity_of_detectors', 'dispersion', 'image_path', 'name', 'id', 'destination',
                        'file_name', 'gauss', 'gamma']
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)


conf = ConfigurationAggregator(gauss=0.3)
print(conf.image_path)
print(conf.gauss)
