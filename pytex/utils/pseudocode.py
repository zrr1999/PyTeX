import re
from pylatex.base_classes import Environment, Options, Command
from pylatex.package import Package
from pylatex.utils import NoEscapeStr


class PseudoCodeEnv(Environment):
    packages = [Package("algpseudocode")]

    def __init__(self, command, name, args=None, enumeration_symbol=None, *, options=None, **kwargs):
        self._enumeration_symbol = enumeration_symbol

        if enumeration_symbol is not None:

            if options is not None:
                options = Options(options)
            else:
                options = Options()

        super().__init__(options=options, **kwargs)
        self.command = command
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

        if self.args is not None:
            begin = Command(self.command, arguments=(self.name, self.args))
        else:
            begin = Command(self.command, arguments=self.name)

        string += begin.dumps() + self.content_separator
        string += content + self.content_separator
        string += Command('End' + self.command).dumps()

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


def algorithm(name, inp=None, out=None, core=None, label=None):
    al = Algorithm()
    al.caption(name)
    alc = al.algorithmic(inp, out)
    if core is not None:
        if label is not None:
            core.pre_append(Command("floatname", arguments=("algorithm", label[0])))
            core.global_define([r"\algorithmicrequire", r"\algorithmicensure"],
                               [f"\\textbf{{{label[1]}:}}", f"\\textbf{{{label[2]}:}}"], True)
    return al, alc


def al_function(name, args=""):
    return PseudoCodeEnv("Function", name, args)


def al_if(condition):
    return PseudoCodeEnv("If", condition)


def al_while(condition):
    return PseudoCodeEnv("While", condition)


def al_for(condition):
    return PseudoCodeEnv("For", condition)


trans_dict = {"get": "**get**",
              "let": "**let**",
              }

key = re.compile(f"\bget\b", re.IGNORECASE)
