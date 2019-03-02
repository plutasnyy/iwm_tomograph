from PIL import Image
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np
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
    # TODO debug why, for big quantity of iterations points_in_image is equal to 0 tested for big distraction,
    #  so it is impossible
    def get_average_brightness_of_the_line(clear_copy_of_wrapped_image, points_in_image) -> int:
        sum = 0
        for point in points_in_image:
            r, g, b = clear_copy_of_wrapped_image.getpixel((point.x, point.y))
            sum += int((r + g + b) / 3)
        if len(points_in_image) == 0:
            return 0
        return int(sum / len(points_in_image))

    @staticmethod
    def print_sinogram(sinogram):
        rgb_sinogram = [[(i, i, i) for i in _] for _ in sinogram]
        plt.imshow(rgb_sinogram)
        plt.show()

    def wrap_image(self, image):
        scale = 3
        width, height = image.size[0], image.size[1]
        new_width, new_height = scale * width, scale * height
        new_size = (width * scale, height * scale)
        x_corner_to_paste = (new_width - width) // 2
        y_corner_to_paste = (new_height - height) // 2

        self.real_image_coords = self.get_real_image_cords(x_corner_to_paste, y_corner_to_paste, width, height)

        grey = (210, 210, 210)
        wrapped_image = Image.new("RGB", new_size, color=grey)
        wrapped_image.paste(image, (x_corner_to_paste, y_corner_to_paste))

        return wrapped_image

    def is_point_in_real_image(self, p):
        """
        lb - left bottom corner
         ru - right upper corner
        :param p: point
        :return: True if point is between real_image_coords
        """
        lb, ru = self.real_image_coords[0], self.real_image_coords[3]  #
        return lb.x <= p.x <= ru.x and lb.y <= p.y <= ru.y
