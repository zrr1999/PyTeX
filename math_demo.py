import os

from pylatex import Command, NewPage, LongTable, MultiColumn
from pylatex.position import Center
from pylatex.utils import NoEscape

from pytex import MathDocument
from pytex.math import DocTree, Appendices, appendices, table

doc = MathDocument('数学建模', packages=["amsmath", "graphicx", "amssymb", "cite"], standard="GJS", preface=False)
# doc.add_pdf("standard.pdf")  # 你可以使用你自己的标准页（GJS标准默认参数会自带标准页）

data_table = table()
row = ["Content1", "这个描述最好不要超过一行"]
for i in range(5):
    data_table.add_row(row)
# 问题重述
wtcs = [{
    "title": "背景资料与条件",
    "content": "出租车是市民出行的重要交通工具之一，"
               "“打车难”是人们关注的一个社会热点问题。"
               "随着“互联网+”时代的到来，有多家公司依托移动互联网建立了打车软件服务平台，"
               "实现了乘客与出租车司机之间的信息互通，同时推出了多种出租车的补贴方案。"
}, {
    "title": "需要解决的问题",
    "content": "0_0"
}]
# 模型的建立与求解
mxjl = NoEscape(r"小明研究过\cite{name1}小黑根据哈士奇原理\cite{name2}发明的冰淇淋\cite{name3}，不过后来放弃了。")

doc.add_title()
doc.add_abstract("这是一个摘要的示例", ["关键词1", "关键词2"])
doc.add_toc()
doc.add_section(title="问题重述", content=wtcs)
doc.add_section(title="问题分析", content=wtcs)
doc.add_section(title="模型假设", content=wtcs)
doc.add_section(title="符号说明", content=data_table)
doc.add_section(title="模型的建立与求解", content=mxjl)
doc.add_section(title="模型的评价", content=data_table)
doc.add_section(title="模型的改进与推广", content=data_table)

doc.body_append(NoEscape(r"\bibliography{document.bib}"))
# doc.body_append(appendices("../", "main.py", 10))

print("正在生成pdf")
doc.generate_pdf('resources/math', compiler='XeLatex', clean_tex=False, clean=False)
