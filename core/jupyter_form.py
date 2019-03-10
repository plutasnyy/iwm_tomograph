from IPython.core.display import clear_output

from core.utils.fileselector import gui_get_file_name
import ipywidgets as widgets
from ipywidgets import Layout, Box, Label, interactive

def get_form(conf):

    iterations = widgets.IntSlider(
        value=conf.iterations,
        min=10,
        max=500,
        step=10,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
    )

    quantity_of_detectors = widgets.IntSlider(
        value=conf.quantity_of_detectors,
        min=10,
        max=1000,
        step=10,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
    )

    dispersion = widgets.IntSlider(
        value=conf.dispersion,
        min=1,
        max=360,
        step=1,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
    )

    process_button = widgets.Button(
        description='Process',
        disabled=False,
        tooltip='Click me',
        icon='fa-arrow-right'
    )

    select_image_button = widgets.Button(
        description='Select Image',
        disabled=False,
        tooltip='Click me',
        icon='fa-image'
    )

    def process(_):
        print(conf.image_path)

    def select_image(_):
        conf.image_path = gui_get_file_name()

    process_button.on_click(process)
    select_image_button.on_click(select_image)

    form_item_layout = Layout(
        display='flex',
        flex_flow='row',
        justify_content='space-between',
    )

    form_items = [
        Box([Label(value='Iterations'), interactive(conf.set_iterations, x=iterations)], layout=form_item_layout),
        Box([Label(value='Quantity of detectors'),
             interactive(conf.set_quantity_of_detectors, x=quantity_of_detectors)], layout=form_item_layout),
        Box([Label(value='Dispersion (in degrees)'), interactive(conf.set_dispersion, x=dispersion)],
            layout=form_item_layout),
        Box([select_image_button, process_button], layout=form_item_layout)
    ]

    form = Box(form_items, layout=Layout(
        display='flex',
        flex_flow='column',
        align_items='stretch',
        width='50%'
    ))

    return form
	