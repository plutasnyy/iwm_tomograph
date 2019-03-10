from core.configuration import Configuration
from core.sinogram import Sinogram
from PIL import Image

image = Image.open('images/{}'.format('Shepp_logan.jpg'))
conf = Configuration(
`
    dispersion=180,
)

sinogram = Sinogram(conf)
for iteration, _ in sinogram.create_sinogram_from_image(image):
    print(iteration)

sinogram.sinogram_to_image()
