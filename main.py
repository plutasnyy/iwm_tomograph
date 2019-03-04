from core.configuration import Configuration
from core.sinogram import Sinogram
from PIL import Image

image = Image.open('images/Kropka.jpg')
conf = Configuration(
    iterations=70,
    quantity_of_detectors=10,
    dispersion=40,
)

sinogram = Sinogram(conf)
for iteration, sinogram in sinogram.create_sinogram_from_image(image):
    print(iteration)
