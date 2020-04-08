from pylatex import NoEscape, Package, Command, Document, Section, Subsection, Subsubsection
from pylatex.base_classes import LatexObject
from .core import Core

Section = [Section, Subsection, Subsubsection]


class DocTreeNode(LatexObject):
    def __init__(self, struct, top=0):
        super().__init__()
        self.title = struct["title"]
        self.contents = struct["content"]
        self.top = top
        if type(self.contents) is list:
            for i, content in enumerate(self.contents):
                if type(content) is dict:
                    self.contents[i] = DocTreeNode(content, top+1)
        elif type(self.contents) is dict:
            self.contents = [DocTreeNode(self.contents, top+1)]
        else:
            self.contents = [self.contents]

    def __repr__(self):
        return self.dumps()

    def dumps(self):
        section = Section[self.top](self.title)
        for content in self.contents:
            section.append(content)
        return section.dumps()


class DocTree(DocTreeNode):
    def __init__(self, struct):
        super().__init__(struct, top=0)
