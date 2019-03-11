from core.configuration.configuration_agregator import ConfigurationAggregator
from core.sinogram import Sinogram
from core.image_processor import ImageProcessor
from PIL import Image


images_dict = {
    1: "CT_ScoutView.jpg",
    2: "CT_ScoutView-large.jpg",
    3: "Kolo.jpg",
    4: "Kwadraty2.jpg",
    5: "Kropka.jpg",
    6: "SADDLE_PE.JPG",
    7: "SADDLE_PE-large.JPG",
    8: "Shepp_logan.jpg",
}

image = Image.open('images/{}'.format(images_dict[2])).convert('L')
conf = ConfigurationAggregator(
    iterations=1,
    quantity_of_detectors=100,
    dispersion=180,
)

sinogram = Sinogram(conf)
for iteration, _ in sinogram.create_sinogram_from_image(image):
    print('Iteration: {}'.format(iteration))

sinogram.sinogram_to_image()

print('MSE: {0:0.2f}'.format(ImageProcessor.calculate_medium_squared_error(image, sinogram.image)))
