from pylatex import NoEscapeStr, MarkDownStr

from pytex import MathDocument
from pytex.base import table
from pytex.utils import SymbolTransformer, md2tex


doc = MathDocument('数学建模', packages=["amsmath", "graphicx", "amssymb", "cite", "hyperref"],
                   standard="GJS", preface=False)
doc.set_information()
# doc.add_pdf("standard.pdf")  # 你可以使用你自己的标准页（GJS标准默认参数会自带标准页）

x = doc.add_var(r"\eta", NoEscapeStr(r"这是一个优秀的$\eta$"))
st = SymbolTransformer()
formula = st.sym2tex((x**2+7)*5)
wtfx = formula[0]

keys = ["出租车资源配置", "供求匹配模型", "缓解程度判断模型", "分区域动态实时补贴方案"]
doc.add_title()
doc.add_abstract(md2tex("md/abstract.md"), keys)
doc.add_toc()
doc.add_section(path="md/wtcs.md")  # 问题重述
doc.add_section(path="md/wtfx.md")  # 问题分析
doc.add_section(path="md/mxjs.md")  # 模型假设
doc.add_section(title="符号说明", content=doc.var_table)  # 添加变量表
doc.add_section(path="md/mxjl.md")  # 模型的建立与求解
doc.add_section(path="md/mxpj.md")  # 模型的评价
doc.add_section(path="md/mxgj.md")  # 模型的改进与推广
doc.add_bib("document.bib")

# doc.body_append(appendices("../", "main.py", 10))
print("正在生成pdf")
doc.generate_pdf('resources/math', compiler='XeLatex', clean_tex=False, clean=False)
