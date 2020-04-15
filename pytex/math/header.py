from pylatex import PageStyle, Head, LineBreak, simple_page_number, Foot
from pytex import Core

def generate_header():
    geometry_options = {"margin": "0.7in"}
    doc = Document(geometry_options=geometry_options)
    # Add document header
    header = PageStyle("header")
    # Create left header
    with header.create(Head("L")):
        header.append("Page date: ")
        header.append(LineBreak())
        header.append("R3")
    # Create center header
    with header.create(Head("C")):
        header.append("Company")
    # Create right header
    with header.create(Head("R")):
        header.append(simple_page_number())
    # Create left footer
    with header.create(Foot("L")):
        header.append("Left Footer")
    # Create center footer
    with header.create(Foot("C")):
        header.append("Center Footer")
    # Create right footer
    with header.create(Foot("R")):
        header.append("Right Footer")

    doc.preamble.append(header)
    doc.change_document_style("header")