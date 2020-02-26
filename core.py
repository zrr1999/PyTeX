import numpy as np
from pylatex import Matrix, Figure, NoEscape
import matplotlib
matplotlib.use('Agg')  # Not to use X server. For TravisCI.


class Core:
    def __init__(self, doc):
        self.big_num = 0
        self.num = 0
        self.doc = doc


def array(_list, **kwargs):
    return Matrix(np.array(_list), **kwargs)


def plot_show(caption, width=r'0.5\textwidth', *args, **kwargs):
    fig = Figure(position='htbp')
    fig.add_plot(width=NoEscape(width), *args, **kwargs)
    fig.add_caption(NoEscape(caption))
    return fig

