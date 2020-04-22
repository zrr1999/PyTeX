import re
from .symbol2tex import sym2tex
from pylatex import MarkDownStr, NoEscapeStr
from pylatex.base_classes import LatexObject
from ..renderer import markdown


class MarkDown(LatexObject):
    """
    (暂未实现)MarkDown文件中第一行为文件模式，第二行为 # +标题名，非Section留空行

    """
    def __init__(self, file_path, mode='r', file_type="sec"):
        super().__init__()
        if isinstance(file_path, str):
            self.file = open(file_path, mode=mode, encoding='UTF-8')
        else:
            self.file = file_path

    def dumps(self):
        string = self.file.read()
        return NoEscapeStr(markdown(string))


def md2tex(file_path, mode='r'):
    """

    :param file_path: 传入的文件或文件地址
    :param mode:
    :return:
    """
    md = MarkDown(file_path, mode)
    return md


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
