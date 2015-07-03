# coding: utf-8

import sys
import os

sys.path.append(os.path.abspath('sphinxext'))

extensions = [
    # 'process_chinese_paragraph',
    'sphinx.ext.mathjax',
    'math_dollar',
]

# project info
project = u'我的笔记'
copyright = u'骆炜炜'

# html output
html_title = project
html_theme = 'sphinxdoc'

# add `math` support
default_role = 'math'
# path to local mathjax.js
# mathjax_path = 'MathJax/MathJax.js'


# chinese
language = 'zh_CN'
# 中文xelatex
# http://codeblog.niwyclin.org/posts/196526-sphinx-chinese-pdf
# sphinx/writers/latex.py
latex_documents = [# (startdocname, targetname, title, author, documentclass, toctree_only)
                   ('contents', 'contents.tex', '', copyright, 'ctexbook',
                   False),
                   # ('submit', 'assignment.tex', u'Listening Assignment', u'骆炜炜 DG1422039', 'ctexart', False),
                   ]
latex_elements = {
    # two hardcoded packages (latex.py): sphinx, multirow
    # others can be selected using following options

    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',
    'classoptions': ',oneside',
    'inputenc':'', #必須，写中文时没必要。input encoding
    'utf8extra':'', #必須
    'cmappkg': '', #        '\\usepackage{cmap}',
    'fontenc': '', #        '\\usepackage[T1]{fontenc}',
    'babel':'',   #必須, 与xelatex冲突
    'fontpkg': '', # use `Computer Modern fonts` instead of the default `times`
    'fncychap': '', #       '\\usepackage[Bjarne]{fncychap}',
    'longtable': '', #      '\\usepackage{longtable}',
    # 'tableofcontents': '', # disable it
    # Additional stuff for the LaTeX preamble.
    # Comment this out when documentclass is ctexart
    'preamble': (
# start newline for description
# http://tex.stackexchange.com/questions/35481/description-list-how-to-put-the-definition-on-a-new-line#answer-70724
r"""
\usepackage{enumitem}
\setlist[description]{style=nextline}
"""
#http://tex.stackexchange.com/questions/664/why-should-i-use-usepackaget1fontenc
# r"""
# \usepackage[T1]{fontenc}
# """
)
    # 'preamble': r"""
    # \usepackage[BoldFont,SlantFont,CJKchecksingle]{xeCJK}
    # \setCJKmainfont[BoldFont=SimHei]{SimSun}
    # \setCJKmonofont{SimSun}
    # \parindent 2em
    # """
    # """
    # \usepackage{indentfirst}
    # \setlength{\parindent}{2em}
    # \setCJKfamilyfont{song}{SimSun}
    # \setCJKfamilyfont{sf}{SimSun}
    # \XeTeXlinebreaklocale "zh"
    # \XeTeXlinebreakskip = 0pt plus 1pt
    # """ #必須

}
