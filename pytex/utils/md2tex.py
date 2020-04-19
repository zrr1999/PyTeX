import re
from .symbol2tex import sym2tex
from pylatex import NoEscape
from pylatex.base_classes import LatexObject


class MarkDown(LatexObject):
    """
    MarkDown文件中第一行为文件模式，第二行为 # +标题名，非Section留空行

    """
    def __init__(self, file_path, file_type="sec"):
        super().__init__()
        self.file = open(file_path, 'r', encoding='UTF-8')
        self.mode = next(self.file)
        string = next(self.file)
        if file_type == "sec":
            loc = re.match(r"# (\S+)", string).span()
            self._latex_name = string[loc[0]+2, loc[1]]

    def dumps(self):
        return md2tex(self.file)


def md2tex(file=None, path=None, mode='r'):
    """"""
    if file:
        string = file.read()
    else:
        string = open(path, mode, encoding='UTF-8').read()
    string = transform_formula(string)
    string = transform_struct(string)
    string = transform_itemize(string)
    return NoEscape(string)


def transform_formula(string):
    """

    :param string: 需要转化的文本
    :return: 转换后的文本
    """
    names = [
        re.compile(r"\*\*(\S+)\*\*"),
        re.compile(r"\*(\S+)\*"),
        re.compile(r"\$\$(\S+)\$\$"),
    ]
    codes = [
        lambda m: r"\textbf{"+m.group(1)+"}",
        lambda m: r"\emph{"+m.group(1)+"}",
        lambda m: sym2tex(m.group(1), False),
    ]
    for i, name in enumerate(names):
        code = codes[i]
        string = name.sub(code, string)
    return string


def transform_struct(string):
    """

    :param string: 需要转化的文本
    :return: 转换后的文本
    """
    names = [
        re.compile(r"### (\S+)\n"),
        re.compile(r"## (\S+)\n"),
        re.compile(r"# (\S+)\n"),
    ]
    codes = [
        lambda m: r"\subsubsection{"+m.group(1)+"}\n",
        lambda m: r"\subsection{"+m.group(1)+"}\n",
        lambda m: r"\section{"+m.group(1)+"}\n",
    ]
    for i, name in enumerate(names):
        code = codes[i]
        string = name.sub(code, string)
    return string


def transform_itemize(string):
    """

    :param string: 需要转化的文本
    :return: 转换后的文本
    """
    names = [
        re.compile(r"[0-9]\. "),
        re.compile(r"- "),
        re.compile(r"\[(\S+)]: (\S+)"),
    ]
    for name in names[:2]:
        string = name.sub(lambda m: r"\item ", string)
    string = names[2].sub(lambda m: f"\\{m.group(1)}{{{m.group(2)}}}\n", string)
    return string


def _beifen(string, *, replace=True, core=None):
    """

    :param replace:
    :param core:
    :param string:
    :return:
    """
    names = [
        re.compile(r"\*\*(\S+)\*\*", re.IGNORECASE),
        re.compile(r"\*(\S+)\*", re.IGNORECASE),
    ]
    codes = [
        lambda m: r"\textbf{"+m.group(1)+"}",
        lambda m: r"\emph{"+m.group(1)+"}",
    ]
    if replace:
        if core is None:
            raise ValueError("core cannot be None")
        with core.local_define(names, codes) as local_core:
            local_core.append(string, mode="re")
    else:
        for i, name in enumerate(names):
            code = codes[i]
            if type(name) is str:
                name = re.compile(f"{name}\b", re.IGNORECASE)
            string = name.sub(code, string)
        return string
