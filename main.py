from core.configuration import Configuration
from core.sinogram import Sinogram
from PIL import Image

image = Image.open('images/{}'.format('Kwadraty2.jpg'))
conf = Configuration(
    iterations=120,
    quantity_of_detectors=120,
    dispersion=180,
)

sinogram = Sinogram(conf)
for iteration, _ in sinogram.create_sinogram_from_image(image):
    print(iteration)

sinogram.sinogram_to_image()
