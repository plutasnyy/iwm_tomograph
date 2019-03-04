from copy import copy

from IPython.core.display import clear_output
from math import pi, cos, sin, sqrt

from core.configuration import Configuration
from core.models.detector import Detector
from core.models.emiter import Emiter

from core.models.point import Point

import numpy as np

from core.utils.imageprocessor import ImageProcessor
from core.utils.bresenham import bresenham


class Sinogram(object):
    BIG_VALUE = 10 ** 5

    def __init__(self, conf: Configuration) -> None:
        self.image_processor = ImageProcessor()
        self.conf = conf
        self.emiter_degrees = np.linspace(0, 2 * pi, self.conf.iterations)
        [self.center, self.radius, self.sinogram] = [None for _ in range(3)]

    def create_sinogram_from_image(self, image):

        self.radius = int(np.ceil(sqrt(image.size[0] ** 2 + image.size[1] ** 2) / 2))

        wrapped_image = self.image_processor.wrap_image(image, self.radius*2)
        clear_copy_of_wrapped_image = copy(wrapped_image)

        self.center = Point(wrapped_image.size[0] // 2, wrapped_image.size[1] // 2)
        self.sinogram = np.zeros(shape=(self.conf.quantity_of_detectors, self.conf.iterations), dtype=np.int64)

        for iteration, emiter_degree in enumerate(self.emiter_degrees):
            if not iteration % 25:
                clear_output(wait="true")
                yield iteration, self.sinogram

            emiter = self._get_emiter(emiter_degree)
            detectors = self._get_detectors(emiter_degree)

            for i, detector in enumerate(detectors):
                points = bresenham(detector, emiter)
                points_in_image = list(filter(self.image_processor.is_point_in_real_image, points))

                self.sinogram[i][iteration] = self.image_processor.get_average_brightness_of_the_line(
                    clear_copy_of_wrapped_image,
                    points_in_image
                )

        clear_output(wait="true")
        ImageProcessor.print_one_dimension_image(self.sinogram)
        return self.sinogram

    def sinogram_to_image(self):
        width = self.radius * 2

        result_image = np.zeros(shape=(width, width), dtype=int)
        counter = np.ones(shape=(width, width))

        for iteration, emiter_degree in enumerate(self.emiter_degrees):
            emiter = self._get_emiter(emiter_degree)
            detectors = self._get_detectors(emiter_degree)

            for iw, detector in enumerate(detectors):
                points = bresenham(detector, emiter)
                value = self.sinogram[iw][iteration]
                points_in_image = list(filter(self.image_processor.is_point_in_real_image, points))
                for point in points_in_image:
                    result_image[point.x, point.y] += value
                    counter[point.x, point.y] += 1
                    if value <= 2:
                        counter[point.x, point.y] = self.BIG_VALUE

        for x in range(width):
            for y in range(width):
                if counter[x][y] != 0:
                    result_image[x][y] = int(result_image[x][y] / counter[x][y])

        ImageProcessor.print_one_dimension_image(result_image)

        return result_image

    def _get_emiter(self, degree_to_place_emiter: float) -> Emiter:
        x_emiter = int(self.radius * cos(degree_to_place_emiter) + self.center.x)
        y_emiter = int(self.radius * sin(degree_to_place_emiter) + self.center.y)
        return Emiter(x_emiter, y_emiter)

    def _get_detectors(self, degree_to_place_emiter: float) -> list:
        """
        :param degree_to_place_emiter: in radians 0 - right side
        """
        detectors = list()
        dispersion = self.conf.get_dispersion_in_radians()
        for i in range(self.conf.quantity_of_detectors):
            x_detector = int(self.radius * cos(degree_to_place_emiter + pi - dispersion / 2 + i * dispersion / (
                    self.conf.quantity_of_detectors - 1)) + self.center.x)
            y_detector = int(self.radius * sin(degree_to_place_emiter + pi - dispersion / 2 + i * dispersion / (
                    self.conf.quantity_of_detectors - 1)) + self.center.y)
            detectors.append(Detector(x_detector, y_detector))
        return detectors
