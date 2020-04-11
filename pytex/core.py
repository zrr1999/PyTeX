from pylatex import NoEscape, Package, Command, Document
import re


class Core(Document):
    def __init__(self, packages=None, debug=None, **kwargs):
        """
        LaTex代码生成的核心。

        :param packages: 文档包含的包
        :param debug: 是否输出debug参数
        :param kwargs: pylatex中Document的参数。
        """
        if kwargs:
            super(Core, self).__init__(**kwargs)
        else:
            super(Core, self).__init__(default_filepath='basic', documentclass='ctexart')

        self.big_num = 0
        self.num = 0
        self.debug = debug

        if packages is not None:
            for package in packages:
                if type(package) is list:
                    self.packages.append(Package(*package))
                else:
                    self.packages.append(Package(package))

    def set(self, add_big_num, add_num):
        self.big_num += add_big_num
        self.num += add_num

    def body_append(self, *items):
        self.extend(items)

    def pre_append(self, *items, **commands):
        for item in items:
            self.preamble.append(item)
        for command, content in commands.items():
            command = Command(command, content)
            self.preamble.append(command)

    def global_define(self, names, codes, replace=False):
        if replace:
            new_command = 'renewcommand'
        else:
            new_command = 'newcommand'

        if type(names) is list:
            for i, name in enumerate(names):
                self.preamble.append(Command(new_command, [NoEscape(name), NoEscape(codes[i])]))
        else:
            self.preamble.append(Command(new_command, [NoEscape(names), NoEscape(codes)]))

    def local_define(self, names, codes, package=None):
        if package is not None:
            self.packages.append(Package(package))
        if type(names) is not list:
            names = [names]
            codes = [codes]
        return LocalCore(self, names, codes, self.debug)

    def __add__(self, other):
        self.body_append(other)
        return self


class LocalCore:
    def __init__(self, core, names, codes, debug=None):
        self.core = core
        self.names = names
        self.codes = codes
        self.debug = debug

    def append(self, *items, mode="str"):
        if mode == "str":
            for item in items:
                for i, name in enumerate(self.names):
                    code = self.codes[i]
                    item = item.replace(name, code)
                    if self.debug:
                        print(item)
                if type(item) is not NoEscape:
                    item = NoEscape(item)
                self.core.append(item)
        elif mode == "re":
            for item in items:
                for i, name in enumerate(self.names):
                    code = self.codes[i]
                    item = name.sub(code, item)
                    if self.debug:
                        print(item)
                if type(item) is not NoEscape:
                    item = NoEscape(item)
                self.core.append(item)
        elif mode == "auto":
            raise NotImplementedError("Auto mode is not implemented!")
        else:
            raise NotImplementedError("Other mode is not implemented!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
