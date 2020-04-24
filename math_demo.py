from pytex import MathDocument
from pytex.utils import md2tex
import os


doc = MathDocument('数学建模',
                   packages=["amsmath", "graphicx", "amssymb", "cite", "hyperref", "pythonhighlight"],
                   standard="GJS", preface=False)
doc.set_information()

doc.add_title()
doc.add_abstract(md2tex("md/abstract.md"))
doc.add_toc()
doc.add_section(path="md/问题重述.md")  # 问题重述
doc.add_section(path="md/问题分析.md")  # 问题分析
doc.add_section(path="md/模型假设.md")  # 模型假设
doc.add_section(title="符号说明", content=doc.var_table)  # 添加变量表
doc.add_section(path="md/模型的建立与求解.md")  # 模型的建立与求解
doc.add_section(path="md/模型的评价.md")  # 模型的评价
doc.add_section(path="md/模型的改进与推广.md")  # 模型的改进与推广
doc.add_bib("document.bib")

print("正在生成pdf")
path = "resources"
if not os.path.exists(path):
    os.mkdir(path)
doc.generate_pdf(path+'/math', compiler='XeLatex', clean_tex=False, clean=False)
