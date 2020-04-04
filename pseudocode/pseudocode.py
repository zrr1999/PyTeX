import re
from pylatex.base_classes import Environment, Options, Command
from pylatex.package import Package
from pylatex.utils import NoEscape


class Function(Environment):
    packages = [Package("algpseudocode")]

    def __init__(self, name, args="", enumeration_symbol=None, *, options=None, **kwargs):
        self._enumeration_symbol = enumeration_symbol

        if enumeration_symbol is not None:

            if options is not None:
                options = Options(options)
            else:
                options = Options()

        super().__init__(options=options, **kwargs)
        self.name = name
        self.args = args

    def dumps(self):
        """Represent the function as a string in LaTeX syntax.

        Returns
        -------
        str
            A LaTeX string representing the function.
        """

        content = self.dumps_content()
        if not content.strip() and self.omit_if_empty:
            return ''

        string = ''

        begin = Command('Function', arguments=(self.name, self.args))
        string += begin.dumps() + self.content_separator
        string += content + self.content_separator
        string += Command('EndFunction').dumps()

        return string

    def add_state(self, s):
        self.append(Command('State', s))  # *(2)占格，!占一整行


class Algorithmic(Environment):
    packages = [Package("algorithmicx")]

    def __init__(self, enumeration_symbol=None, *, options=None, **kwargs):
        self._enumeration_symbol = enumeration_symbol

        if enumeration_symbol is not None:

            if options is not None:
                options = Options(options)
            else:
                options = Options()

        super().__init__(options=options, **kwargs)

    def caption(self, s):
        self.append(Command('caption', s))


class Algorithm(Environment):
    packages = [Package("algorithm"), Package("algpseudocode"), Package("amsmath")]

    def __init__(self, enumeration_symbol=None, *, options=None, **kwargs):
        self._enumeration_symbol = enumeration_symbol

        if enumeration_symbol is not None:

            if options is not None:
                options = Options(options)
            else:
                options = Options()

        super().__init__(options=options, **kwargs)

    def caption(self, s):
        self.append(Command('caption', s))

    def algorithmic(self, inp=None, out=None):
        alg = Algorithmic(options="1")
        if inp is not None:
            alg.append(Command('Require', inp))
        if out is not None:
            alg.append(Command('Ensure', out))
        self.append(alg)
        return alg


def algorithm(name, inp=None, out=None):
    al = Algorithm()
    al.caption(name)
    alc = al.algorithmic(inp, out)
    return alc


trans_dict = {"get": "**get**",
              "let": "**let**",
              }

key = re.compile(f"\bget\b", re.IGNORECASE)
