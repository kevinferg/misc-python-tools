import numpy as np
from PIL import Image

def auto_crop(input_file, output_file=None):
    if output_file is None:
        output_file = input_file
    image = Image.open(input_file)
    A = np.array(image)
    rows = A.shape[0]
    cols = A.shape[1]

    # Crop left and right sides
    for i in range(cols):
        if len(np.unique(A[:,i])) > 1:
            A = A[:,i:]
            cols = A.shape[1]
            break
    for i in range(cols-1,0,-1):
        if len(np.unique(A[:,i])) > 1:
            A = A[:,:i]
            rows = A.shape[0]
            break
    # Trim top and bottom sides
    for i in range(rows):
        if len(np.unique(A[i,:])) > 1:
            A = A[i:,:]
            rows = A.shape[0]
            break
    for i in range(rows-1,0,-1):
        if len(np.unique(A[i,:])) > 1:
            A = A[:i,:]
            break

    image = Image.fromarray(A)
    image.save(output_file) 