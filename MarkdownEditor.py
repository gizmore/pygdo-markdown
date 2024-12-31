import markdown

from gdo.message.editor.Editor import Editor


class MarkdownEditor(Editor):

    @classmethod
    def get_name(cls) -> str:
        return 'markdown'

    @classmethod
    def to_html(cls, input: str) -> str:
        html = markdown.markdown(input)
        return super().to_html(html)
