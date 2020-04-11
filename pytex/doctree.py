from pylatex import Section, Subsection, Subsubsection, Package
from pylatex.base_classes import LatexObject

marker_prefix = ["section", "subsection", "subsubsection"]


class DocTreeNode(Section):
    def __init__(self, struct, top=0):
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


class DocTree(LatexObject):
    def __init__(self, *structs, packages=None):
        super().__init__()
        self.nodes = []
        for struct in structs:
            self.nodes.append(DocTreeNode(struct))
        if packages is not None:
            for package in packages:
                self.packages.append(package)

    def __repr__(self):
        return self.dumps()

    def dumps(self):
        out = ""
        for node in self.nodes:
            out += node.dumps()
        return out
