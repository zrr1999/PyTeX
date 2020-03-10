import numpy as np
from pylatex import Matrix, Figure, NoEscape, Package, Command
import matplotlib
matplotlib.use('Agg')  # Not to use X server. For TravisCI.


class Core:
    def __init__(self, doc, packages):
        self.big_num = 0
        self.num = 0
        self.doc = doc

        for package in packages:
            if type(package) is list:
                doc.packages.append(Package(*package))
            else:
                doc.packages.append(Package(package))

    def set(self, add_big_num, add_num):
        self.big_num += add_big_num
        self.num += add_num

    def body_append(self, *items):
        if len(items) == 1:
            self.doc.append(items[0])
        else:
            for item in items:
                self.doc.append(item)

    def pre_append(self, *items):
        if len(items) == 1:
            self.doc.preamble.append(items[0])
        else:
            for item in items:
                self.doc.preamble.append(item)

    def define(self, name=r"\untitled", code="Hello World"):
        # self.doc.preamble.append(NoEscape(f"\\def {name} {{{code}}}"))
        self.doc.preamble.append(Command('newcommand', [NoEscape(name), NoEscape(code)]))

    def __add__(self, other):
        self.body_append(other)
        return self


def array(_list, **kwargs):
    return Matrix(np.array(_list), **kwargs)


def plot_show(caption, width=r'0.5\textwidth', *args, **kwargs):
    fig = Figure(position='htbp')
    fig.add_plot(width=NoEscape(width), *args, **kwargs)
    fig.add_caption(NoEscape(caption))
    return fig



