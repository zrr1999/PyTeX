from pylatex import Subsection, Enumerate, NoEscape, NewLine
from pylatex.base_classes import Environment, Options, Command, LatexObject


class Key(LatexObject):
    def __init__(self, name):
        super().__init__()
        self.key = NoEscape(f"\\textbf {{{name}: }}")

    def append(self, key):
        if isinstance(key, list):
            self.key += " ".join(key) + " "
        else:
            self.key += key + " "

    def dumps(self):
        return self.key


class Abstract(Environment):
    def __init__(self, content=None, key=None,  **kwargs):
        super().__init__(**kwargs)
        self.append(NoEscape(r"\neirong"))
        self.key = Key("关键词")
        if content:
            self.add_content(content)
        if key:
            self.add_key(key)

    def add_content(self, s, space=None):
        self.append(s)
        if space:
            self.append(NoEscape(r"\vspace{"+space+"cm}"))
        else:
            self.append(NewLine())
        self.append(self.key)

    def add_key(self, key):
        self.key.append(key)


def abstract(content, key):
    return Abstract(NoEscape(content), key)
