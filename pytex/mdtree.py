from pylatex import Section, Subsection, Subsubsection, Package, Command, NoEscapeStr, Itemize, Enumerate
from pylatex.base_classes import LatexObject
import sympy as sp

Section = [Section, Subsection, Subsubsection]
Itemize = [Itemize, Enumerate]
font = ["hb", "hc", "hc"]


class MDTree(LatexObject):
    def __init__(self, markdown):
        super().__init__()
        self.data = []
        self.packages = []
        if not isinstance(markdown, list):
            markdown = [markdown]
        for md in markdown:
            if md['type'] == 'heading':
                self.data.append(Section[md['level']](MDTree(md['children'])))
            elif md['type'] == 'paragraph':
                self.data.append(MDTree(md['children']))
            elif md['type'] == 'text':
                self.data.append(md['text'])
            elif md['type'] == 'list':
                self.data.append(Itemize[md['ordered']]())
                for child in md['children']:



        for struct in structs:
            self.data.append(DocTreeNode(struct, top, auto_font))
        if packages is not None:
            for package in packages:
                self.packages.append(package)
        for node in self.data:
            self.packages.extend(node.packages)

    def __repr__(self):
        return self.dumps()

    def dumps(self):
        out = ""
        for data in self.data:
            out += data + "\n"
        return out
