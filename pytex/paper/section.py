from pylatex.base_classes import Container, Command
from pylatex.labelref import Marker, Label


class Section(Container):
    """A class that represents a section.

    :argument end_paragraph: A section should normally start in its own paragraph
    :argument marker_prefix: Default prefix to use with Marker
    :argument numbering: Number the sections when the section element is compatible,
    by changing the `~.Section` class default all subclasses will also have the new default.
    """

    end_paragraph = True
    marker_prefix = "sec"
    numbering = True

    def __init__(self, title, numbering=None, *, label=True, **kwargs):
        """

        :param title: The section title.
        :param numbering: Add a number before the section title.
        :param label: Label or bool or str Can set a label manually
        or use a boolean to set preference between automatic or no label.
        :param kwargs:
        """

        self.title = title

        if numbering is not None:
            self.numbering = numbering
        if isinstance(label, Label):
            self.label = label
        elif isinstance(label, str):
            if ':' in label:
                label = label.split(':', 1)
                self.label = Label(Marker(label[1], label[0]))
            else:
                self.label = Label(Marker(label, self.marker_prefix))
        elif label:
            self.label = Label(Marker(title, self.marker_prefix))
        else:
            self.label = None

        super().__init__(**kwargs)

    def dumps(self):
        """Represent the section as a string in LaTeX syntax.

        :return:
        """

        if not self.numbering:
            num = '*'
        else:
            num = ''

        string = Command(self.latex_name + num, self.title).dumps()
        if self.label is not None:
            string += '%\n' + self.label.dumps()
        string += '%\n' + self.dumps_content()

        return string
