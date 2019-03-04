from math import pi

from core.sinogram import Sinogram
from PIL import Image

image = Image.open('images/Kwadraty2.JPG')
sinogram = Sinogram(
    quantity_of_detectors=100,
    iterations=150,
    dispersion=pi/5)
sinogram.create_sinogram_from_image(image)
sinogram.sinogram_to_image()
