from mistune import escape, Markdown, escape_html
from mistune.renderers import BaseRenderer
import re

FORMULA_PATTERN = re.compile(r"\$\$\n((.+\n)*)\$\$")
VAR_PATTERN = r"\{(.+)}"


def parse_formula(self, m, state):
    text = m.group(1)
    return {'type': 'formula', 'text': text}


def render_tex_formula(text):
    return '\n\\begin{equation}\n' + text + '\\end{equation}\n'


def parse_var(self, m, state):
    text = self.var[m.group(1)]
    return {'type': 'formula', 'text': text}


def render_tex_var(text):
    return '$' + text + '$'


def plugin_pytex(md):
    md.block.register_rule('formula', FORMULA_PATTERN, parse_formula)
    md.block.rules.append('formula')
    # md.inline.register_rule('var', VAR_PATTERN, parse_var)
    # md.inline.rules.append('var')

    if md.renderer.NAME == 'tex':
        md.renderer.register('formula', render_tex_formula)
        # md.renderer.register('var', render_tex_var)


class Renderer(BaseRenderer):
    NAME = 'tex'
    IS_TREE = False

    def __init__(self, escape=False, **var):
        super().__init__()
        self._escape = escape
        self.var = var

    def text(self, text):
        return text.replace("%", r"\%")

    def link(self, link, text=None, title=None):
        if text is None:
            text = link
        return f"\\href{{{link}}}{{{text}}}"

    def image(self, src, alt="", title=None):
        return f"\\includegraphics[{title}]{{{src}}}"

    def emphasis(self, text):
        return '\\emph{' + text + '}'

    def strong(self, text):
        return '\\textbf{' + text + '}'

    def codespan(self, text):
        return '<code>' + escape(text) + '</code>'

    def linebreak(self):
        return '\\newline\n'

    def inline_html(self, html):
        if self._escape:
            return escape(html)
        return html

    def paragraph(self, text):
        return '\n' + text + '\n'

    def heading(self, text, level):
        tag = "sub"*(level-1)+"section"
        return f'\\{tag}{{{text}}}\n'

    def newline(self):
        return ''

    def thematic_break(self):
        return '<hr />\n'

    def block_text(self, text):
        return text

    def block_code(self, code, info=None):
        html = '<pre><code'
        if info is not None:
            info = info.strip()
        if info:
            lang = info.split(None, 1)[0]
            lang = escape_html(lang)
            html += ' class="language-' + lang + '"'
        return html + '>' + escape(code) + '</code></pre>\n'

    def block_quote(self, text):
        return '<blockquote>\n' + text + '</blockquote>\n'

    def block_html(self, html):
        if not self._escape:
            return html + '\n'
        return '<p>' + escape(html) + '</p>\n'

    def block_error(self, html):
        return '<div class="error">' + html + '</div>\n'

    def list(self, text, ordered, level, start=None):
        if ordered:
            ordered = "enumerate"
        else:
            ordered = "itemize"
        return f'\\begin{{{ordered}}}\n{text}\\end{{{ordered}}}\n'

    def list_item(self, text, level):
        return '\\item\n' + text + '\n'


markdown = Markdown(Renderer(), plugins=[plugin_pytex])

if __name__ == '__main__':
    markdown = Markdown(Renderer(), plugins=[plugin_pytex])
    print(markdown("fasdfasdf"))
