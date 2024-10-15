# Export Colab notebooks as pdf files

## Description

To convert a Jupyter notebook to pdf, `.ipynb > .html > .pdf` is my usual route. Google Colab has issues where it only exports the first page of contents to html. This code uses `jupyter nbconvert` to get a clean pdf output, and it works in Colab. 

## Usage

- Copy the following code into a cell at the end of your notebook.
- Change the file name in the first line to be the name of the notebook. (I couldn't find a convenient way to do this automatically.)
- Run the cell. 
- The pdf should download to `Downloads/`.

```python

NOTEBOOK_NAME = "CHANGE_THIS.ipynb"

#####################################################################################################
!apt-get install -y pandoc > /dev/null 2>&1
!sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic > /dev/null 2>&1
!pip install nbconvert > /dev/null 2>&1

from google.colab import drive, files
drive.mount('/content/drive')
notebook_path = rf'/content/drive/MyDrive/Colab Notebooks/{NOTEBOOK_NAME}'

import os
if os.path.exists(notebook_path):
    !jupyter nbconvert --to pdf "{notebook_path}" > /dev/null 2>&1
    pdf_filename = notebook_path.replace('.ipynb', '.pdf')
    files.download(pdf_filename)
else:
    print("Notebook not found. Please check the path.")
#####################################################################################################
```

## Troubleshooting

It's possible that the notebook is saved somewhere other than `/content/drive/MyDrive/Colab Notebooks/` on Drive.   

If so, change the `notebook_path = rf'/content/drive/MyDrive/Colab Notebooks/{NOTEBOOK_NAME}'` line to use the correct path.