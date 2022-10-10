import numpy as np

def linstep(a0, a1, w):
    return (a1 - a0) * w + a0

def smoothstep(a0, a1, w):
    return (a1 - a0) * (3.0 - w * 2.0) * w * w + a0

def interp(arr, xy, smooth=True, tol=1e-9):
    """Interpolate an image/grid of values at arbitrary points

    Arguments:
    - arr: Grid of values to interpolate
    - xy: Array of (x, y) points at which to interpolate 'arr'
    - smooth: Whether to use "smooth" Hermite interpolation (vs. linear)
    - tol: small tolerance value  

    Details:
    - Points in 'xy' should be between (0,0) and (1,1)
    - arr[ 0, 0] corresponds to xy point [0,0]
    - arr[ 0,-1] corresponds to xy point [0,1]
    - arr[-1, 0] corresponds to xy point [1,0]
    - arr[-1,-1] corresponds to xy point [1,1]
    
    Returns: Array of interpolated values
    """
    fun = smoothstep if smooth else linstep
    xy = xy.reshape(-1,2)
    xy = np.clip(xy, tol, 1-tol)
    arr = arr.T
    rows, columns = np.shape(arr)
    x,y = ((xy[:, 0])*(columns - 1)), ((xy[:, 1])*(rows - 1))
    
    x_f, x_i = np.modf(x)
    y_f, y_i = np.modf(y)
    
    x_i = x_i.astype(int)
    y_i = y_i.astype(int)
    
    bottom = fun(arr[x_i,     y_i], arr[x_i + 1,     y_i], x_f)
    top    = fun(arr[x_i, y_i + 1], arr[x_i + 1, y_i + 1], x_f)
    
    left   = fun(arr[x_i,     y_i], arr[x_i,     y_i + 1], y_f)
    right  = fun(arr[x_i + 1, y_i], arr[x_i + 1, y_i + 1], y_f)
    
    vals = 0.5 * fun(left, right, x_f) + 0.5 * fun(bottom, top, y_f)
    return vals