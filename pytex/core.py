from pylatex import NoEscape, Package, Command, Document, NewPage
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
            super().__init__(**kwargs)
        else:
            super().__init__(default_filepath='basic', documentclass='ctexart')
        self.debug = debug
        if packages is not None:
            for package in packages:
                if type(package) is list:
                    self.packages.append(Package(*package))
                else:
                    self.packages.append(Package(package))

    def __add__(self, other):
        self.body_append(other)
        return self

    def __radd__(self, other):
        self.pre_append(other)
        return self

    def body_append(self, *items, **commands):
        """
        向文档主体中添加内容。

        :param items: 文字序列
        :param commands: 命令序列
        :return: None
        """
        self.extend(items)
        for command, content in commands.items():
            command = Command(command, content)
            self.append(command)

    def pre_append(self, *items, **commands):
        """
        向文档前言中添加内容。

        :param items: 文字序列
        :param commands: 命令序列
        :return: None
        """
        self.preamble.extend(items)
        for command, content in commands.items():
            command = Command(command, content)
            self.preamble.append(command)

    def define(self, names: list, codes, replace=False):
        if replace:
            new_command = 'renewcommand'
        else:
            new_command = 'newcommand'

        if type(names) is list:
            for i, name in enumerate(names):
                self.preamble.append(Command(new_command, [NoEscape(name), NoEscape(codes[i])]))
        else:
            self.preamble.append(Command(new_command, [NoEscape(names), NoEscape(codes)]))
