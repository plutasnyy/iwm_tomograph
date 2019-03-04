from copy import copy
from math import pi, cos, sin, sqrt

from core.models.detector import Detector
from core.models.emiter import Emiter

from core.models.point import Point

from PIL import Image
import numpy as np

from core.utils.imageprocessor import ImageProcessor
from core.utils.bresenham import bresenham


class Sinogram(object):

    def __init__(self, quantity_of_detectors: int, iterations: int, dispersion: float) -> None:
        """
        :param quantity_of_detectors:
        :param iterations: how many different positions will be collected
        :param dispersion: a space between successive ones detectors
        """
        self.image_processor = ImageProcessor()
        self.quantity_of_detectors = quantity_of_detectors
        self.iterations = iterations
        self.dispersion = dispersion
        [self.center, self.radius, self.sinogram] = [None for _ in range(3)]

    def create_sinogram_from_image(self, image):

        wrapped_image = self.image_processor.wrap_image(image)
        clear_copy_of_wrapped_image = copy(wrapped_image)

        self.center = Point(wrapped_image.size[0] // 2, wrapped_image.size[1] // 2)
        self.radius = sqrt(image.size[0] ** 2 + image.size[1] ** 2)*1.5

        degree_step = 2 * pi / self.iterations
        self.sinogram = np.zeros(shape=(self.quantity_of_detectors, self.iterations), dtype=np.int64)
        degree_to_place_emiter_in_radians = 0

        for iteration in range(self.iterations):
            if not iteration % 25:
                print(iteration)

            degree_to_place_emiter_in_radians += degree_step
            emiter = self._get_emiter(degree_to_place_emiter_in_radians)
            detectors = self._get_detectors(degree_to_place_emiter_in_radians, self.dispersion)
            # self.image_processor.print_detector_on_image(emiter, detectors, wrapped_image)

            for i, detector in enumerate(detectors):
                points = bresenham(detector, emiter)
                points_in_image = list(filter(self.image_processor.is_point_in_real_image, points))

                # TODO probably we will need to remember angle and average value for every detector
                #  to reverse radon function instead of calculate it second time
                self.sinogram[i][iteration] = self.image_processor.get_average_brightness_of_the_line(
                    clear_copy_of_wrapped_image,
                    points_in_image
                )

        ImageProcessor.print_sinogram(self.sinogram)
        return self.sinogram

    def sinogram_to_image(self):
        degree_step = 2 * pi / self.iterations
        degree_to_place_emiter_in_radians = 0
        width = int(self.radius)

        new_image = np.zeros(shape=(width, width))
        counter = np.zeros(shape=(width, width))
        for i in range(self.iterations):
            degree_to_place_emiter_in_radians += degree_step
            emiter = self._get_emiter(degree_to_place_emiter_in_radians)
            detectors = self._get_detectors(degree_to_place_emiter_in_radians, self.dispersion)
            for iw,detector in enumerate(detectors):
                points = bresenham(detector, emiter)
                value = self.sinogram[iw][i]
                points_in_image = list(filter(self.image_processor.is_point_in_real_image, points))
                for pon in points_in_image:
                        new_image[pon.x, pon.y] += value
                        counter[pon.x, pon.y] += 1
                        if value<0.4:
                            counter[pon.x, pon.y] += 50000
        for i in range(width):
            for t in range(width):
                if counter[i][t]>0:
                    new_image[i][t] = new_image[i][t]/counter[i][t]
        ImageProcessor.print_sinogram(new_image)
        return new_image

    def _get_emiter(self, degree_to_place_emiter: float) -> Emiter:
        x_emiter = int(self.radius * cos(degree_to_place_emiter) + self.center.x)
        y_emiter = int(self.radius * sin(degree_to_place_emiter) + self.center.y)
        return Emiter(x_emiter, y_emiter)

    def _get_detectors(self, degree_to_place_emiter: float, dispersion: float) -> list:
        """
        :param degree_to_place_emiter: in radians 0 - right side
        :param dispersion: in radians - if pi, half of circle will be covered
        """
        detectors = list()
        for i in range(self.quantity_of_detectors):
            x_detector = int(self.radius * cos(degree_to_place_emiter + pi - dispersion / 2 + i * dispersion / (
                        self.quantity_of_detectors - 1)) + self.center.x)
            y_detector = int(self.radius * sin(degree_to_place_emiter + pi - dispersion / 2 + i * dispersion / (
                        self.quantity_of_detectors - 1)) + self.center.y)
            detectors.append(Detector(x_detector, y_detector))
        return detectors
