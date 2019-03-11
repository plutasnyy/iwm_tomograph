import ipywidgets as widgets
from ipywidgets import Layout, Box, Label, interactive

from core.configuration.configuration_agregator import ConfigurationAggregator


def get_dicom_form(conf: ConfigurationAggregator):
    name = widgets.Text(
        value=conf.name,
        placeholder='Type something',
        description='String:',
        disabled=False
    )

    id = widgets.Text(
        value=conf.id,
        placeholder='Type something',
        description='String:',
        disabled=False
    )

    destination = widgets.Text(
        value=conf.destination,
        placeholder='Type something',
        description='String:',
        disabled=False
    )

    file_name = widgets.Text(
        value=conf.file_name,
        placeholder='Type something',
        description='String:',
        disabled=False
    )

    process_button = widgets.Button(
        description='Save',
        disabled=False,
        tooltip='Click me',
        icon='fa-arrow-right'
    )
    form_item_layout = Layout(
        display='flex',
        flex_flow='row',
        justify_content='space-between',
    )

    form_items = [
        Box([Label(value='Name'), interactive(conf.set_name, x=name)], layout=form_item_layout),
        Box([Label(value='ID'), interactive(conf.set_id, x=id)], layout=form_item_layout),
        Box([Label(value='Description'), interactive(conf.set_destination, x=destination)], layout=form_item_layout),
        Box([process_button], layout=form_item_layout)
    ]

    form = Box(form_items, layout=Layout(
        display='flex',
        flex_flow='column',
        align_items='stretch',
        width='50%'
    ))

    return form
