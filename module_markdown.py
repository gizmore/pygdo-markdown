from gdo.markdown.MarkdownEditor import MarkdownEditor
from gdo.base.GDO_Module import GDO_Module
from gdo.message.editor.GDT_Editor import GDT_Editor


class module_markdown(GDO_Module):

    def gdo_dependencies(self) -> list:
        return [
            'message',
        ]

    async def gdo_install(self):
        from gdo.message.module_message import module_message
        await module_message.instance().save_config_val('default_editor', 'markdown')

    def gdo_init(self):
        GDT_Editor.register(MarkdownEditor)
