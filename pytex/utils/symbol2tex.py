import sympy as sp
from pylatex import NoEscape


class SymbolTransformer(object):
    def __init__(self):
        self.num = 0

    def sym2tex(self, symbol, name=None):
        self.num += 1
        if name is None:
            name = self.num
        return sym2tex(symbol, False, f"Eq:{name}")

    def ref(self, name=None):
        if name is None:
            name = self.num
        return f"\\ref{{Eq:{name}}}"


def sym2tex(symbol, inline, label=None):
    if isinstance(symbol, str):
        math_tex = symbol
    else:
        math_tex = sp.latex(symbol)
    if inline:
        return NoEscape(f"${math_tex}$")
    else:
        if label is not None:
            return NoEscape(f"\\begin{{equation}}\n"
                            f"\\label{{{label}}}\n"
                            f"{math_tex}\n"
                            f"\\end{{equation}}"), label
        else:
            return NoEscape(f"\\begin{{equation}}\n"
                            f"{math_tex}\n"
                            r"\end{equation}")
