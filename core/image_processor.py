import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Circle
from scipy.ndimage import gaussian_filter

from core.models.point import Point


class ImageProcessor(object):

    def __init__(self):
        self.real_image_coords = None

    @staticmethod
    def print_detector_on_image(emiter, detectors, image):
        fig, ax = plt.subplots(1)
        ax.set_aspect('equal')
        ax.imshow(image)
        circle = Circle((int(emiter.x), int(emiter.y)), 3, color='red')
        ax.add_patch(circle)
        for detector in detectors:
            circle = Circle((detector.x, detector.y), 3, color='green')
            line_cords = [[emiter.x, detector.x], [emiter.y, detector.y]]
            ax.add_patch(circle)
            plt.plot(*line_cords, linewidth=0.5, color='#95d4ed')
        plt.show()

    @staticmethod
    def get_real_image_cords(x: int, y: int, width: int, height: int) -> list:
        return [
            Point(x, y),
            Point(x + width - 1, y),
            Point(x, y + height - 1),
            Point(x + width - 1, y + height - 1),
        ]

    @staticmethod
    def get_average_brightness_of_the_line(clear_copy_of_wrapped_image, points_in_image) -> int:
        if len(points_in_image) == 0:
            return 0
        sum = 0
        for point in points_in_image:
            r, g, b = clear_copy_of_wrapped_image.getpixel((point.x, point.y))
            sum += int((r + g + b) / 3)
        return int(sum / len(points_in_image))

    @staticmethod
    def print_one_dimension_image(sinogram) -> None:
        rgb_sinogram = [[(i, i, i) for i in _] for _ in sinogram]
        plt.imshow(rgb_sinogram)
        plt.show()

    @staticmethod
    def normalize_image(image):
        max = np.amax(image)
        for i in range(len(image)):
            for j in range(len(image[i])):
                if max != 0:
                    x = int(round(image[i][j] / max * 255))
                    image[i][j] = x if x > 0 else 0
        return image.astype(np.uint8)

    @staticmethod
    def calculate_medium_squared_error(base_image, result_image):
        return ((base_image - np.transpose(result_image)) ** 2).mean()

    def wrap_image(self, image, size):
        width, height = image.size[0], image.size[1]
        x_corner_to_paste = (size - width) // 2
        y_corner_to_paste = (size - height) // 2

        self.real_image_coords = self.get_real_image_cords(x_corner_to_paste, y_corner_to_paste, width, height)

        grey = (120, 120, 120)
        wrapped_image = Image.new("RGB", (size, size), color=grey)
        wrapped_image.paste(image, (x_corner_to_paste, y_corner_to_paste))

        return wrapped_image

    def is_point_in_real_image(self, p: Point) -> bool:
        """
        lb - left bottom corner
        ru - right upper corner
        :param p: point
        :return: True if point is between real_image_coords
        """
        lb, ru = self.real_image_coords[0], self.real_image_coords[3]  #
        return lb.x <= p.x <= ru.x and lb.y <= p.y <= ru.y

    def trim_real_image(self, image):
        lb, ru = self.real_image_coords[0], self.real_image_coords[3]  #
        return image[lb.y:ru.y + 1, lb.x:ru.x + 1]
