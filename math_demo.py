from pylatex.position import Center
from pylatex.utils import NoEscape

from pytex import MathDocument
from pytex.base import table
from pytex.utils import SymbolTransformer, md2tex
doc = MathDocument('数学建模', packages=["amsmath", "graphicx", "amssymb", "cite"], standard="GJS", preface=False)
# doc.add_pdf("standard.pdf")  # 你可以使用你自己的标准页（GJS标准默认参数会自带标准页）

x = doc.add_var("x")

st = SymbolTransformer()
formula = st.sym2tex((x**2+7)*5)
wtfx = formula[0]
# 模型的建立与求解
mxjl = NoEscape(r"小明研究过\cite{name1}小黑根据哈士奇原理\cite{name2}发明的冰淇淋\cite{name3}，不过后来放弃了。")

doc.add_title()
doc.add_abstract("这是一个摘要的示例", ["关键词1", "关键词2"])
doc.add_toc()
# 问题重述
doc.add_md("wtcs.md")
doc.add_section(title="问题分析", content=wtfx[0])
doc.add_section(title="模型假设", content="wtcs")
doc.add_section(title="符号说明", content=doc.var_table)
doc.add_section(title="模型的建立与求解", content=mxjl)
doc.add_section(title="模型的评价", content=doc.var_table)
doc.add_section(title="模型的改进与推广", content=doc.var_table)
doc.add_bib("document.bib")
# doc.body_append(appendices("../", "main.py", 10))
print("正在生成pdf")
doc.generate_pdf('resources/math', compiler='XeLatex', clean_tex=False, clean=False)
