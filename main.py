from core.configuration import Configuration
from core.sinogram import Sinogram
from PIL import Image

image = Image.open('images/Shepp_logan.jpg')
conf = Configuration(
    iterations=360,
    quantity_of_detectors=100,
    dispersion=12,
)

sinogram = Sinogram(conf)
for iteration, _ in sinogram.create_sinogram_from_image(image):
    print(iteration)

sinogram.sinogram_to_image()
