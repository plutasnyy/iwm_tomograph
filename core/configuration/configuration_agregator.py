from core.configuration.dicom_configuration import DicomConfiguration
from core.configuration.filter_configuration import FilterConfiguration
from core.configuration.setup_configuration import SetupConfiguration


class ConfigurationAggregator(SetupConfiguration, FilterConfiguration, DicomConfiguration):
    def __init__(self, **kwargs):
        """
        SETUP:
        :param iterations: how many different positions will be collected
        :param quantity_of_detectors:
        :param dispersion: a space between successive ones detectors
        :param image_path:
        :param is_step_by_step:
        :param step_size:

        DICOM
        :param name:
        :param id:
        :param destination:
        :param file_name:

        FILTER
        :param is_filter:
        """
        super().__init__()
        allowed_keys = ['iterations', 'quantity_of_detectors', 'dispersion', 'image_path', 'name', 'id', 'destination',
                        'file_name', 'is_filter', 'is_step_by_step', 'step_size']
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)
