from PyQt5.QtWidgets import QFileDialog


def gui_get_file_name(dir=None):
    """Select a file via a dialog and return the file name."""
    if dir is None: dir = './'
    file_path = QFileDialog.getOpenFileName(None, "Select data file...", dir, filter="All files (*);; SM Files (*.sm)")
    return file_path[0]
