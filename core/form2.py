from IPython.core.display import clear_output

from core.utils.fileselector import gui_get_file_name
import ipywidgets as widgets
from ipywidgets import Layout, Box, Label, interactive,Text




def get_form2(conf):

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
	
	des = widgets.Text(
        value=conf.des,
		placeholder='Type something',
		description='String:',
		disabled=False
    )
	
	filename = widgets.Text(
        value=conf.filename,
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
        Box([Label(value='Name'), Text(conf.set_name, x=name)], layout=form_item_layout),
        Box([Label(value='ID'),Text(conf.set_id, x=id)], layout=form_item_layout),
        Box([Label(value='Description'), Text(conf.set_des, x=des)],layout=form_item_layout),
		Box([process_button], layout=form_item_layout)
    ]
	
	form = Box(form_items, layout=Layout(
        display='flex',
        flex_flow='column',
        align_items='stretch',
        width='50%'
    ))
	
	return form