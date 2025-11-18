import os
import unittest

from gdo.base.Application import Application
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Render import Mode
from gdo.message.GDT_Message import GDT_Message
from gdotest.TestUtil import web_plug, GDOTestCase, install_module


class GDO_Foo(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Message('foo_msg').label_raw('MSG'),
        ]


class MarkdownTest(GDOTestCase):

    def setUp(self):
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        install_module('markdown')
        loader.init_modules(True, True)

    def test_01_markdown_to_telegram(self):
        foo = GDO_Foo.blank({
            'foo_msg': '# Title\n\nparagraph\nof text\n\n[ChATTACA](https://www.wechall.net/challenge/gizmore/chattaca)\n',
            'foo_msg_editor': 'markdown',
        }).insert()
        gdt = foo.column('foo_msg')
        html = gdt.render(Mode.render_html)
        self.assertIn('<h1>Title</h1>', html, "markdown editor does not render html #1")
        self.assertIn('<p>paragraph', html, "markdown editor does not render html #2")
        self.assertIn('<a href="https://www.wechall', html, "markdown editor does not render html #3")
        self.assertIn('ChATTACA</a>', html, "markdown editor does not render html #4")
        markdown = gdt.render(Mode.render_markdown)
        self.assertIn('# Title', markdown, "markdown rendering failed #1.")
        self.assertIn('[ChATTACA](https://www.wechall.net/challenge/gizmore/chattaca)', markdown, "markdown rendering failed #2.")


if __name__ == '__main__':
    unittest.main()
