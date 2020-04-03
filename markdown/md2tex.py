from pylatex import NoEscape
import re


def md2tex(core, string):
    """

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

    with core.local_define(names, codes) as local_core:
        local_core.append(string)
