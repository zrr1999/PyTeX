import matplotlib

from pylatex import Document, Section, Figure, NoEscape

import matplotlib.pyplot as plt  # noqa


def main(core, width,  *args, **kwargs):
    doc = core.doc
    with doc.create(Figure(position='htbp')) as plot:
        plot.add_plot(width=NoEscape(width), *args, **kwargs)
        plot.add_caption('I am a caption.')

    doc.generate_pdf(clean_tex=False)


if __name__ == '__main__':
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [15, 2, 7, 1, 5, 6, 9]

    plt.plot(x, y)

    main('matplotlib_ex-dpi', r'1\textwidth', dpi=300)
    main('matplotlib_ex-facecolor', r'0.5\textwidth', facecolor='b')
