# Remove transparency from a folder of PNG files

## Description

This script edits PNG files to remove transparency and replace it with solid white or black.


## Usage

Usage is: `py opacify.py [src] [color=color] [dest=dest]`

- `src` = Source folder containing pngs (and, optionally, any other files)
- `color` (defaults to white) = color to fill in the transparent pixels: 'white'/'w' or 'black'/'b'
- `dest` (defaults to same as `src`) = Folder to place resulting files, i.e. without overwriting `src` folder

## Examples

- Remove transparency from all files in 'fig/'. Use white replacement color.
```
py opacify.py fig
```

- Remove transparency from all files in 'fig/', place resulting files in 'opaque/'. Use white replacement color.
```
py opacify.py fig dest=opaque
```

- Remove transparency from all files in 'fig/', place resulting files in 'opaque/'. Use black replacement color.
```
py opacify.py fig dest=opaque color=black
```

## Requirements

`pillow` must be installed, i.e. using:

```
pip install pillow
```