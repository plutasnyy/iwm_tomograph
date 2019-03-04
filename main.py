from math import pi

from core.sinogram import Sinogram
from PIL import Image

image = Image.open('images/SADDLE_PE-large.JPG')
sinogram = Sinogram(
    quantity_of_detectors=100,
    iterations=200,
    dispersion=pi/2)
sinogram.create_sinogram_from_image(image)
