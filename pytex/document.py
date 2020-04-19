from .core import Core
from .paper import Abstract, DocTree, DocTreeNode
from .base import table
from .utils import sym2tex, md2tex
import sympy as sp
from pylatex import NoEscape, Package, Command, NewPage, PageStyle, Foot


class Document(Core):
    def __init__(self, title, packages=None, debug=None, **kwargs):
        super().__init__(packages, debug, **kwargs)
        if isinstance(title, dict):
            self.pre_append(**title)
        else:
            self.pre_append(title=title)

    def add_title(self):
        """
        给文档添加标题（包括文章标题、作者等）

        :return: None
        """
        self.body_append(Command('maketitle'))

    def add_abstract(self, content=None, key=None):
        """
        给文档添加摘要

        :param content: 摘要内容
        :param key: 摘要关键字
        :return: None
        """
        self.body_append(Abstract(content, key))

    def add_toc(self):
        """
        给文档添加目录

        :return: None
        """
        self.body_append(Command("tableofcontents"))

    def add_pdf(self, path: str, page=(1, "")):
        self.packages.append(Package("pdfpages"))
        self.pre_append(Command("includepdfset", NoEscape(r"pagecommand={\thispagestyle{fancy}}")))
        self.body_append(Command("includepdfmerge", NoEscape(f"{path}, {page[0]}-{page[1]}")))

    def add_page(self):
        """
        给文档添加一个新页

        :return: None
        """
        self.body_append(NewPage())

    def add_section(self, title, content):
        doc_tree = DocTree({"title": title, "content": content})
        self.body_append(doc_tree)

    def add_bib(self, path):
        """

        :param path: 参考文献位置
        :return:
        """
        self.body_append(NoEscape(f"\\bibliography{{{path}}}"))


class MathDocument(Document):
    def __init__(self, title, packages=None, debug=None, standard="XD", preface=True):
        """

        :param title: 论文标题
        :param packages: 论文需要用到的包（使用Python端创建的对象需要的包会自动添加）
        :param debug: 暂时无用
        :param standard: 论文格式，分为XD和GJS
        :param preface: 是否需要打印标准页（承诺书和评分），XD暂未添加
        """
        self.standard = standard
        if standard == "GJS":
            if preface:
                super().__init__(title, packages, debug, documentclass='cumcmthesis')
            else:
                super().__init__(title, packages, debug, documentclass='cumcmthesis',
                                 document_options=["withoutpreface", "bwprint"])
        elif standard == "XD":
            if packages is None:
                packages = [["geometry", "a4paper, centering, scale=0.8"]]
            else:
                packages.append(["geometry", "a4paper, centering, scale=0.8"])
            super().__init__(Command('ha', title), packages, debug)
            header = PageStyle("header")
            with header.create(Foot("C")):
                header.append(NoEscape(r"\thepage"))
            self.pre_append(header)
            self.change_document_style("header")
            self.define([r"\abstractname"], [r"\hb 摘要"], True)
            self.pre_append(NoEscape(r"\setCJKfamilyfont{zhsong}[AutoFakeBold = {2.17}]{SimSun}"))
            self.define([r"\ha", r"\hb", r"\hc", r"\neirong"], [
                r"\fontsize{15.75pt}{\baselineskip}\heiti",
                r"\fontsize{14pt}{\baselineskip}\heiti",
                r"\fontsize{12pt}{\baselineskip}\heiti",
                r"\fontsize{12pt}{\baselineskip}\songti",
            ])
        self.pre_append(NoEscape(r"\bibliographystyle{plain}"))
        self.var_table = table()

    def add_abstract(self, content=None, key=None):
        """
        给文档添加摘要

        :param content: 摘要内容
        :param key: 摘要关键字
        :return: None
        """
        self.body_append(Abstract(content, key, self.standard))

    def add_section(self, title=None, content=None, path=None):
        if path:
            self.add_md(path)  # 问题重述
        else:
            doc_tree = DocTreeNode({"title": title, "content": content}, auto_font=(self.standard == "XD"))
            self.body_append(NoEscape("\n"), doc_tree)

    def add_var(self, name, describe=""):
        var = sp.Symbol(name)
        self.var_table.add_row(NoEscape(f"${name}$"), describe)
        return var

    def add_math(self, math, inline=True):
        self.body_append(sym2tex(math, inline))
        return math

    def add_md(self, path):
        self.body_append(md2tex(open(path, 'r', encoding='UTF-8')))


class ExamDocument(Document):
    def __init__(self, packages=None, debug=None, **kwargs):
        super().__init__(packages, debug, **kwargs)
        self.big_num = 0
        self.num = 0

    def set(self, add_big_num, add_num):
        self.big_num += add_big_num
        self.num += add_num
