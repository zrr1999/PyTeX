import re
from pylatex import NoEscape, Package, Command


class Core:
    def __init__(self, doc, packages):
        self.big_num = 0
        self.num = 0
        self.doc = doc

        for package in packages:
            if type(package) is list:
                doc.packages.append(Package(*package))
            else:
                doc.packages.append(Package(package))

    def set(self, add_big_num, add_num):
        self.big_num += add_big_num
        self.num += add_num

    def body_append(self, *items):
        for item in items:
            self.doc.append(item)

    def pre_append(self, *items):
        for item in items:
            self.doc.preamble.append(item)

    def global_define(self, names, codes):
        if type(names) is list:
            for i, name in enumerate(names):
                self.doc.preamble.append(Command('newcommand', [NoEscape(name), NoEscape(codes[i])]))
        else:
            self.doc.preamble.append(Command('newcommand', [NoEscape(names), NoEscape(codes)]))

    def local_define(self, names, codes):
        if type(names) is not list:
            names = [names]
            codes = [codes]
        return LocalCore(self, names, codes)

    def __add__(self, other):
        self.body_append(other)
        return self


class LocalCore:
    def __init__(self, core, names, codes):
        self.core = core
        self.doc = core.doc
        self.names = names
        self.codes = codes

    def append(self, *items, mode="str"):
        if mode == "str":
            for item in items:
                for i, name in enumerate(self.names):
                    code = self.codes[i]
                    item = item.replace(name, code)
                if type(item) is NoEscape:
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




