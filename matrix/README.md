# matrix.py

## Description

This code converts a 2D array into a LaTeX matrix. The bracket type and decimal precision can be specified.  

See the example below for how to display a formatted matrix within a Jupyter notebook.


## Example

```python
import numpy as np
import matrix

np.random.seed(0)
A = np.random.rand(2,3)

# Generate LaTeX string for matrix enclosed in [square brackets]
# displaying at most 3 decimal places for each number
A_string = matrix.to_latex(A,"[", 3)

print(A_string)
```

The above prints the following string: 

`\begin{bmatrix}`  
`  0.549 & 0.715 & 0.603\\`  
`  0.545 & 0.424 & 0.646\\`  
`\end{bmatrix}`  


Furthermore, to display the result immediately within a Jupyter notebook, use the following code:

```python
from IPython.display import display, Latex
display(Latex(A_string))
```

This displays the following:

$$
\begin{bmatrix}
  0.549 & 0.715 & 0.603\\
  0.545 & 0.424 & 0.646\\
\end{bmatrix}
$$