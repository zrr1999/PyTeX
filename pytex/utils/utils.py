import matplotlib
import numpy as np
from pylatex import Matrix, Figure, NoEscape

matplotlib.use('Agg')  # Not to use X server. For TravisCI.


def array(lis, **kwargs):
    return Matrix(np.array(lis), **kwargs)


def plot_show(caption, width=r'0.5\textwidth', *args, **kwargs):
    fig = Figure(position='htbp')
    fig.add_plot(width=NoEscape(width), *args, **kwargs)
    fig.add_caption(NoEscape(caption))
    return fig


def replace(items, replace_dict, mode="str"):
    if mode == "str":
        for i, item in enumerate(items):
            for a, b in replace_dict.items():
                item = item.replace(a, b)
            if type(item) is not NoEscape:
                items[i] = NoEscape(item)
            else:
                items[i] = item
    elif mode == "re":
        for i, item in items:
            for a, b in replace_dict.items():
                item = a.sub(b, item)
            if type(item) is not NoEscape:
                items[i] = NoEscape(item)
            else:
                items[i] = item
    elif mode == "auto":
        raise NotImplementedError("Auto mode is not implemented!")
    else:
        raise NotImplementedError("Other mode is not implemented!")
    return item
