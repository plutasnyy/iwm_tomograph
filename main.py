from core.configuration import Configuration
from core.sinogram import Sinogram
from PIL import Image

image = Image.open('images/{}'.format('CT_ScoutView.jpg'))
conf = Configuration(
    iterations=180,
    quantity_of_detectors=120,
    dispersion=60,
)

sinogram = Sinogram(conf)
for iteration, _ in sinogram.create_sinogram_from_image(image):
    print(iteration)

sinogram.sinogram_to_image()
