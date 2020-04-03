from pylatex import NoEscape, Package, Command, Document
import re


class Core:
    def __init__(self, doc=None, packages=None, debug=None):
        """
        LaTex代码生成的核心。

        :param doc: 用于兼容pylatex库中的操作
        :param packages: 文档包含的包
        """

        self.big_num = 0
        self.num = 0
        self.debug = debug
        if doc is not None:
            self.doc = doc
        else:
            self.doc = Document(default_filepath='basic', documentclass='ctexart')

        if packages is not None:
            for package in packages:
                if type(package) is list:
                    self.doc.packages.append(Package(*package))
                else:
                    self.doc.packages.append(Package(package))

    def set(self, add_big_num, add_num):
        self.big_num += add_big_num
        self.num += add_num

    def body_append(self, *items):
        for item in items:
            self.doc.append(item)

    def pre_append(self, *items, **commands):
        for item in items:
            self.doc.preamble.append(item)
        for command, content in commands.items():
            command = Command(command, content)
            self.doc.preamble.append(command)

    def global_define(self, names, codes):
        if type(names) is list:
            for i, name in enumerate(names):
                self.doc.preamble.append(Command('newcommand', [NoEscape(name), NoEscape(codes[i])]))
        else:
            self.doc.preamble.append(Command('newcommand', [NoEscape(names), NoEscape(codes)]))

    def local_define(self, names, codes, package=None):
        if package is not None:
            self.doc.packages.append(Package(package))
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
        self.doc = core.doc
        self.names = names
        self.codes = codes
        self.debug = debug

    def append(self, *items, mode="str"):
        if mode == "str":
            for item in items:
                for i, name in enumerate(self.names):
                    code = self.codes[i]
                    if type(name) is str:
                        name = re.compile(f"{name}\b", re.IGNORECASE)
                    item = name.sub(code, item)
                    if self.debug:
                        print(item)
                if type(item) is not NoEscape:
                    item = NoEscape(item)
                self.doc.append(item)
        elif mode == "command":
            raise NotImplementedError("Command mode is not implemented!")
            # for item in items:
            #     for i, name in enumerate(self.names):
            #         code = self.codes[i]
            #         if type(item) is NoEscape:
            #             r = re.compile('{name}[^A-z]')
            #             print(f'{name}[^A-z]')
            #             item = NoEscape(r.sub(code, item))
            #         else:
            #             item = item.replace(name, code)
            #     if type(item) is NoEscape:
            #         item = NoEscape(item)
            #     self.doc.append(item)
        else:
            raise NotImplementedError("Command mode is not implemented!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
