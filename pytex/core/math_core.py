from pylatex import NoEscape, PageStyle, Foot
from .core import Core


class MathCore(Core):
    def __init__(self, packages=None, debug=None, standard="XD", withoutpreface=True):
        self.standard = standard
        if standard == "GJS":
            if withoutpreface:
                super().__init__(packages, debug, documentclass='cumcmthesis')
            else:
                super().__init__(packages, debug, documentclass='cumcmthesis', option=["withoutpreface", "bwprint"])
        elif standard == "XD":
            if packages is None:
                packages = [["geometry", "a4paper, centering, scale=0.8"]]
            else:
                packages.append(["geometry", "a4paper, centering, scale=0.8"])
            super().__init__(packages, debug)
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
