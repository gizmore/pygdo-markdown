import markdown

from gdo.base.Render import Mode
from gdo.base.Util import Strings


class MDConvert:

    _text: str

    def __init__(self, text: str):
        self._text = text

    def to(self, mode: Mode):
        try:
            method_name = f'to_{mode.name.lower()}'
            if method := getattr(self, method_name):
                return method(self._text)
        except AttributeError:
            return self.to_html(self._text)

    def to_html(self, text):
        return markdown.markdown(text)

    def to_telegram(self, text):
        return Strings.html_to_text(self.to_html(text))

    def to_irc(self, text):
        return Strings.html_to_text(self.to_html(text))

    def to_txt(self, text):
        return Strings.html_to_text(self.to_html(text))
