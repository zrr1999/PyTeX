from pylatex.base_classes import Environment, Options, Command
from pylatex.package import Package
from pylatex import Document, Section
from pylatex.utils import NoEscape


class Tasks(Environment):
    """A class to wrap LaTeX's tasks environment."""
    def __init__(self, enumeration_symbol=None, *, options=None, **kwargs):
        self._enumeration_symbol = enumeration_symbol

        if enumeration_symbol is not None:
            self.packages.add(Package("tasks"))

            if options is not None:
                options = Options(options)
            else:
                options = Options()

        super().__init__(options=options, **kwargs)

    def add_task(self, s):
        self.append(Command('task'))
        self.append(s)


def choice(describe, *items, line_num=4):
    """

    :param describe: The describe of this problem.
    :param items: Choice items.
    :param line_num: The number of items in one line.
    :return: LaTex code.
    """
    co = Tasks()
    co.append(f"({line_num})")
    for item in items:
        co.add_task(NoEscape(item))
    return NoEscape(describe+co.dumps())
