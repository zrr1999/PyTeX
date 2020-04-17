from .variable import Variable


class Graph(Variable):
    def __init__(self, name=None):
        if name is None:
            name = "<未命名的变量>"
        super().__init__(name)

    def __repr__(self):
        pass

