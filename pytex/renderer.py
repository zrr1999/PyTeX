from mistune import escape, Markdown, escape_html
from mistune.renderers import BaseRenderer
import re

FORMULA_PATTERN = re.compile(r"\$\$\n((.+\n)*)\$\$")


def parse_formula(self, m, state):
    text = m.group(1)
    return {'type': 'formula', 'text': text}


def render_tex_formula(text):
    return '\n\\begin{equation}\n' + text + '\\end{equation}\n'


def plugin_formula(md):
    md.block.register_rule('formula', FORMULA_PATTERN, parse_formula)
    md.block.rules.append('formula')

    if md.renderer.NAME == 'tex':
        md.renderer.register('formula', render_tex_formula)


class Renderer(BaseRenderer):
    NAME = 'tex'
    IS_TREE = False

    def __init__(self, escape=False):
        super().__init__()
        self._escape = escape

    def text(self, text):
        return text.replace("%", r"\%")

    def link(self, link, text=None, title=None):
        if text is None:
            text = link

        s = '<a href="' + self._safe_url(link) + '"'
        if title:
            s += ' title="' + escape_html(title) + '"'
        return s + '>' + (text or link) + '</a>'

    def image(self, src, alt="", title=None):
        s = '<img src="' + src + '" alt="' + alt + '"'
        if title:
            s += ' title="' + escape_html(title) + '"'
        return s + ' />'

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


markdown = Markdown(Renderer(), plugins=[plugin_formula])

if __name__ == '__main__':
    markdown = Markdown(Renderer(), plugins=[plugin_formula])
