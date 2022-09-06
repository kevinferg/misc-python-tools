
def to_latex(a, bracket=""):
    bracket_types = {"":"",
                     "(":"p", ")":"p",
                     "[":"b", "]":"b",
                     "{":"B", "}":"B",
                     "|":"v",
                     "||":"V"}
    


    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    latex_string =  '\n'.join(rv)
    return latex_string