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
    9: "Shepp_logan_small.jpg",
}

image = Image.open('images/{}'.format(images_dict[4])).convert('L')
conf = ConfigurationAggregator(
    iterations=400,
    quantity_of_detectors=200,
    dispersion=140,
    is_step_by_step=False,
    is_filter=False,
)


sinogram = Sinogram(conf)
for _ in sinogram.create_sinogram_from_image(image):
    pass
    # print('Iteration: {}'.format(iteration))

sinogram.sinogram_to_image()

print('{x} {y:0.2f}'.format(x=0, y=ImageProcessor.calculate_medium_squared_error(image, sinogram.image)))
