from gdo.base.GDO_Module import GDO_Module
from gdo.markdown.MarkdownEditor import MarkdownEditor
from gdo.message.editor.GDT_Editor import GDT_Editor


class module_markdown(GDO_Module):

    def gdo_init(self):
        GDT_Editor.register(MarkdownEditor)
