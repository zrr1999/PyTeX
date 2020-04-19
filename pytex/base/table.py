from pylatex import Section, NoEscape, NewLine, Package, LongTable
from pylatex.base_classes import Environment, Options, Command, LatexObject


def long_table(num=2, title=("符号", "说明")):
    data_table = LongTable("l "*num)
    data_table.add_hline()
    data_table.add_hline()
    data_table.add_row(title)
    data_table.add_hline()
    data_table.end_table_header()
    data_table.add_hline()
    data_table.end_table_footer()
    data_table.add_hline()
    data_table.add_hline()
    data_table.end_table_last_footer()
    return data_table


def table(num=2, title=("符号", "说明")):
    data_table = LongTable("c "*num)
    data_table.add_hline()
    data_table.add_hline()
    data_table.add_row(title)
    data_table.add_hline()
    data_table.end_table_header()
    data_table.add_hline()
    data_table.end_table_footer()
    data_table.add_hline()
    data_table.add_hline()
    data_table.end_table_last_footer()
    return data_table
