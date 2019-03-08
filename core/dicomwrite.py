import dicom, dicom.UID
from dicom.dataset import Dataset, FileDataset
import datetime, time


def write_dicom(filename, pixel_array,name,id,des):
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = 'Secondary Capture Image Storage'
    file_meta.MediaStorageSOPInstanceUID = '1.3.6.1.4.1.9590.100.1.1.111165684411017669021768385720736873780'
    file_meta.ImplementationClassUID = '1.3.6.1.4.1.9590.100.1.0.100.4.0'
    ds = FileDataset(filename, {},file_meta = file_meta,preamble=b"\0" * 128)
    
    # Add the data elements -- not trying to set all required here. Check DICOM standard
    ds.PatientName = name
    ds.PatientID = id
    ds.PatientComments = des

    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 0
    ds.HighBit = 15
    ds.BitsStored = 16
    ds.BitsAllocated = 16
    ds.Columns = pixel_array.shape[0]
    ds.Rows = pixel_array.shape[1]
    if pixel_array.dtype != np.uint16:
        pixel_array = pixel_array.astype(np.uint16)
    ds.PixelData = pixel_array.tostring()
    # Set creation date/time
    ds.ContentDate = str(datetime.date.today()).replace('-','')
    ds.ContentTime = str(time.time())
    ds.save_as(filename)