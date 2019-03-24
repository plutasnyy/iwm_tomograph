from core.configuration.configuration_agregator import ConfigurationAggregator
from core.utils.file_selector import gui_get_file_name
import ipywidgets as widgets
from ipywidgets import Layout, Box, Label, interactive


def get_setup_form(conf: ConfigurationAggregator):
    iterations = widgets.IntSlider(
        value=conf.iterations,
        min=1,
        max=500,
        step=10,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        description=' ',
    )

    quantity_of_detectors = widgets.IntSlider(
        value=conf.quantity_of_detectors,
        min=2,
        max=1000,
        step=10,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        description=' ',
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
        description=' ',
    )

    step_size = widgets.IntSlider(
        value=conf.step_size,
        min=1,
        max=500,
        step=1,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        description=' ',
    )

    select_image_button = widgets.Button(
        description='Select Image',
        disabled=False,
        tooltip='Click me',
        icon='fa-image'
    )

    is_step_by_step = widgets.RadioButtons(
        options=[True, False],
        value=conf.is_step_by_step,
        disabled=False,
        description=' ',
    )

    is_filter = widgets.RadioButtons(
        options=[True, False],
        value=conf.is_filter,
        description=' ',
        disabled=False
    )

    def select_image(_):
        conf.image_path = gui_get_file_name()

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
        Box([Label(value='Step by step'), interactive(conf.set_is_step_by_step, x=is_step_by_step)],
            layout=form_item_layout),
        Box([Label(value='Step size'), interactive(conf.set_step_size, x=step_size)],
            layout=form_item_layout),
        Box([Label(value='Filter'), interactive(conf.set_filter, x=is_filter)],
            layout=form_item_layout),
        Box([select_image_button], layout=form_item_layout)
    ]

    form = Box(form_items, layout=Layout(
        display='flex',
        flex_flow='column',
        align_items='stretch',
        width='50%'
    ))

    return form
