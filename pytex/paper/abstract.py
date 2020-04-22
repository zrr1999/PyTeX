from pylatex import Subsection, Enumerate, NoEscapeStr, NewLine
from pylatex.base_classes import Environment, Options, Command, LatexObject, CommandBase


class Key(LatexObject):
    def __init__(self, name):
        super().__init__()
        self.key = NoEscapeStr(f"\\textbf {{{name}: }}")

    def append(self, key):
        if isinstance(key, list):
            self.key += r"\quad "+r"\quad ".join(key)
        else:
            self.key += key + r"\quad "

    def dumps(self):
        return NoEscapeStr(self.key)


class Keywords(CommandBase):
    latex_name = "keywords"

    def __init__(self, arguments=None, options=None, *, extra_arguments=None):
        if arguments is None:
            self.args = []
        else:
            self.args = arguments
        self.opts = options
        self.ex_args = extra_arguments
        super().__init__(arguments, options, extra_arguments=extra_arguments)

    def set(self):
        super().__init__(self.args, self.opts, extra_arguments=self.ex_args)

    def append(self, keys):
        if isinstance(keys, list):
            for key in keys:
                self.args.append(r"{}".format(key))
                self.args.append(Command("quad"))
        else:
            self.args.append(r"{}".format(keys))
            self.args.append(Command("quad"))
        self.set()


class Abstract(Environment):
    def __init__(self, content=None, key=None, standard="XD", **kwargs):
        super().__init__(**kwargs)
        self.standard = standard
        if standard == "GJS":
            self.key = Keywords()
        else:
            self.append(NoEscapeStr(r"\neirong"))
            self.key = Key("关键词")
        if content:
            self.add_content(content)
        if key:
            self.add_key(key)

    def add_content(self, s, space=None):
        self.append(s)
        if self.standard == "XD":
            if space:
                self.append(NoEscapeStr(r"\vspace{" + space + "cm}"))
            else:
                self.append(NewLine())
        self.append(self.key)

    def add_key(self, key):
        self.key.append(key)


def abstract(content, key):
    return Abstract(NoEscapeStr(content), key)
