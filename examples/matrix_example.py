import numpy as np
import matrix

np.random.seed(0)
A = np.random.rand(2,3)

# Generate LaTeX string for matrix enclosed in [square brackets]
# displaying at most 3 decimal places for each number
A_string = matrix.to_latex(A,"[", 3)

print(A_string)



## Display in notebook:

# from IPython.display import display, Latex
# display(Latex(A_string))