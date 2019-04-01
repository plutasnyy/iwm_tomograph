# iwm_tomograph

### Installation
```
conda create -n iwm python=3.6 anaconda
conda activate iwm
``` 

##### Add widgets
With pip:
```
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension
```

With conda:
```
conda install -c conda-forge ipywidgets
```

### Steps

Load an image

![](docs/1.png)

Place the image in bigger image. Calculate positions of and emiter and detectors, calculate lines between devices using bresnhman algorithm.

![](docs/2.png)

Create singoram column using average value of every line. Move devices and repeat for every degree.

![](docs/3.png)

Construct image from averages of lines using sinogram.

![](docs/4.png)
 
 ### GUI
 
![](docs/9.png)