from pylatex import Matrix, Figure, NoEscape
import numpy as np
import matplotlib

matplotlib.use('Agg')  # Not to use X server. For TravisCI.


def array(_list, **kwargs):
    return Matrix(np.array(_list), **kwargs)


def plot_show(caption, width=r'0.5\textwidth', *args, **kwargs):
    fig = Figure(position='htbp')
    fig.add_plot(width=NoEscape(width), *args, **kwargs)
    fig.add_caption(NoEscape(caption))
    return fig
