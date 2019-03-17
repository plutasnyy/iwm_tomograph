import numpy as np

from copy import copy, deepcopy
from math import pi, cos, sin, sqrt
from IPython.core.display import clear_output

from core.image_processor import ImageProcessor
from core.utils.bresenham import bresenham

from core.configuration.configuration_agregator import ConfigurationAggregator
from core.models.detector import Detector
from core.models.emiter import Emiter

from core.models.point import Point


class Sinogram(object):

    def __init__(self, conf: ConfigurationAggregator) -> None:
        self.image_processor = ImageProcessor()
        self.conf = conf
        self.emiter_degrees = np.linspace(0, 2 * pi, self.conf.iterations)
        self.mask = [-1, 3, -1]
        [self.center, self.radius, self.sinogram, self.image] = [None for _ in range(4)]

    def create_sinogram_from_image(self, image):

        self.radius = int(np.ceil(sqrt(image.size[0] ** 2 + image.size[1] ** 2) / 2 * 1.5))

        wrapped_image = self.image_processor.wrap_image(image, self.radius * 2)
        clear_copy_of_wrapped_image = copy(wrapped_image)

        self.center = Point(wrapped_image.size[0] // 2, wrapped_image.size[1] // 2)
        self.sinogram = np.zeros(shape=(self.conf.quantity_of_detectors, self.conf.iterations), dtype=np.int64)

        iterations_to_update = [0]
        iterations_to_update.extend(i - 1 for i in range(1, self.conf.iterations + 1) if not i % self.conf.step_size)
        iterations_to_update.append(self.conf.iterations-1)

        for iteration, emiter_degree in enumerate(self.emiter_degrees):
            emiter = self._get_emiter(emiter_degree)
            detectors = self._get_detectors(emiter_degree)

            for i, detector in enumerate(detectors):
                points = bresenham(detector, emiter)
                points_in_image = list(filter(self.image_processor.is_point_in_real_image, points))

                self.sinogram[i][iteration] = self.image_processor.get_average_brightness_of_the_line(
                    clear_copy_of_wrapped_image,
                    points_in_image
                )

            if self.conf.is_step_by_step and iteration in iterations_to_update:
                clear_output(wait=True)
                print('Iteration: {}/{}'.format(iteration + 1, self.conf.iterations))
                self.image_processor.print_detector_on_image(emiter, detectors, wrapped_image)
                self.image_processor.print_one_dimension_image(self.sinogram)
                yield iteration

        if self.conf.is_filter:
            for col in range(self.sinogram.shape[1]):
                column = self.sinogram[:, col]
                new_column = list()
                for i in range(len(column)):
                    if 1 <= i <= len(column) - 2:
                        local_sum = 0
                        for j in range(len(self.mask)):
                            local_sum += self.sinogram[i + j - 1, col] * self.mask[j]
                        new_column.append(local_sum)
                    else:
                        new_column.append(self.sinogram[i][col])
                self.sinogram[:, col] = deepcopy(new_column)
            print("Filter")

        print("Normalization")
        self.image_processor.normalize_image(self.sinogram)
        self.image_processor.print_one_dimension_image(self.sinogram)

        return self.sinogram

    def sinogram_to_image(self):
        width = self.radius * 2

        image = np.zeros(shape=(width, width), dtype=np.int64)
        counter = np.zeros(shape=(width, width))

        for iteration, emiter_degree in enumerate(self.emiter_degrees):
            emiter = self._get_emiter(emiter_degree)
            detectors = self._get_detectors(emiter_degree)

            for iw, detector in enumerate(detectors):
                points = bresenham(detector, emiter)
                value = self.sinogram[iw][iteration]
                points_in_image = list(filter(self.image_processor.is_point_in_real_image, points))
                for point in points_in_image:
                    image[point.x, point.y] += value
                    counter[point.x, point.y] += 1

        for x in range(width):
            for y in range(width):
                if counter[x][y] != 0:
                    image[x][y] /= counter[x][y]

        image = self.image_processor.normalize_image(image)
        self.image = np.transpose(self.image_processor.trim_real_image(image))
        self.conf.image = self.image

        ImageProcessor.print_one_dimension_image(self.image)
        return self.image

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
