# coding: utf-8
"""
XXX: 存在bug，code-block(::)无法保持断行
http://blog.csdn.net/ancale/article/details/27982553

walkaround: 在行尾加入\
"""
from docutils.nodes import *

def setup(app):
    app.connect('doctree-resolved', process_chinese_paragraph)

class ParagraphVisitor(NodeVisitor):
    def dispatch_visit(self, node):
        if isinstance(node, TextElement):
            for i in range(len(node.children)):
                if type(node[i]) == Text:
                    node[i] = Text(node[i].astext().replace('\r', '').replace('\n', ''))

def process_chinese_paragraph(app, doctree, docname):
    pv = ParagraphVisitor(doctree)
    doctree.walk(pv)
