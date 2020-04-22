from pylatex import Section, NoEscapeStr, NewLine, Package
from pylatex.base_classes import Environment, Options, Command, LatexObject


class Appendices(Environment):
    packages = [Package("appendix"), Package("pythonhighlight")]

    def __init__(self, path="./"):
        super().__init__()
        self.path = path
        self.append(Section("附录"))

    def add_file(self, files, line_sum=20):
        if isinstance(files, list):
            for i, file in enumerate(files):
                if isinstance(line_sum, list):
                    self.append(NoEscapeStr(f"{file}\n\\inputpython{{{self.path + file}}}{{1}}{{{line_sum[i]}}}\n"))
                else:
                    self.append(NoEscapeStr(f"{file}\n\\inputpython{{{self.path + file}}}{{1}}{{{line_sum}}}\n"))
        else:
            self.append(NoEscapeStr(f"{files}\n\\inputpython{{{self.path + files}}}{{1}}{{{line_sum}}}\n"))


def appendices(path, files, line_sum):
    a = Appendices(path)
    a.add_file(files, line_sum=line_sum)
    return a
