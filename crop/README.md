# gif.py

## Description

For images containing unwanted uniform black/white/transparent/etc. space around the border, the provided function `auto_crop()` will remove this border, so that the bounding box of the image is as tight as possible around the subject. It uses Pillow and NumPy.

## Usage

The following code will crop `image.png`, overwriting `image.png` with the cropped version:
```python
from crop import auto_crop
auto_crop('image.png')
```

Alternatively, the code below will crop `image.png` and save the cropped version to `cropped.png`.
```python
from crop import auto_crop
auto_crop('image.png', 'cropped.png')
```