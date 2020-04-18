import sympy as sp


class Symbol(sp.Symbol):
    def __repr__(self):
        return sp.latex(self)
