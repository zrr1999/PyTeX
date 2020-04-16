from pylatex import Section, Subsection, Subsubsection, Package, Command, NoEscape
from pylatex.base_classes import LatexObject

marker_prefix = ["section", "subsection", "subsubsection"]
font = ["hb", "hc", "hc"]


class DocTreeNode(Section):
    def __init__(self, struct, top=0, auto_font=True):
        if auto_font:
            super().__init__(NoEscape(Command(font[top], struct["title"]).dumps()))
        else:
            super().__init__(struct["title"])

        self._latex_name = marker_prefix[top]
        if type(struct["content"]) is list:
            for i, content in enumerate(struct["content"]):
                if type(content) is dict:
                    self.append(DocTreeNode(content, top+1))
        elif type(struct["content"]) is dict:
            self.append(DocTreeNode(struct["content"], top+1))
        else:
            self.append(struct["content"])
        self.dumps_packages()


class DocTree(LatexObject):
    def __init__(self, *structs, packages=None, top=0, font_mode="Auto"):
        super().__init__()
        self.data = []
        self.packages = []
        for struct in structs:
            self.data.append(DocTreeNode(struct, top))
        if packages is not None:
            for package in packages:
                self.packages.append(package)
        for node in self.data:
            self.packages.extend(node.packages)

    def __repr__(self):
        return self.dumps()

    def dumps(self):
        out = ""
        for node in self.data:
            out += node.dumps()
        return out
