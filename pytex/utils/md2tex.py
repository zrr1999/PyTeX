import re


def md2tex(string, *, replace=True, core=None):
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
