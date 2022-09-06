import numpy as np

def to_latex(matrix, bracket="", decimals = 4):
    bracket_types = {"":'',
                     "(":'p', ")":'p',
                     "[":'b', "]":'b',
                     "{":'B', "}":'B',
                     "|":'v',
                     "||":'V'}

    lines = str(np.round(matrix, decimals)).replace('[', '').replace(']', '').splitlines()

    rv = []
    rv = [r'\begin{' + bracket_types[bracket] + 'matrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{' + bracket_types[bracket] + 'matrix}']

    latex_string =  '\n'.join(rv)
    return latex_string