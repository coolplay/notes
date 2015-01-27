LaTex Writer
============

输出的 tex 文件分析
-------------------

包括以下六个部分:

* header.

  对应 LaTeX preamble 部分，包括 documentclass 和所需的 package 。绝大多数默认包
  含的包可以通过 ``conf.py`` 中的 ``latex_elements`` disable 掉，但其中有两个包
  是写死在writer 中： ``sphinx`` 和 ``multirow`` 。经过测试，只保留 ``sphinx``
  ，去掉其他所有默认的包是不会报错的。因此，你可以在配置文件 ``conf.py`` 中修改
  ``latex_elements`` ，将包选项置空，只在 ``preamble`` 选项中加入你需要的包和配
  置代码即可。

* highlighter

  这部分也包括在 preamble 中，提供由 Pygments 定义的 LaTeX 高亮命令。

* body

  文章主体部分，这就是 rst 文件转换后对应的 tex 代码。

* optional footer

  由 ``latex_elements`` 中的 ``footer`` 控制，默认为空。对应的 tex 代码位于 indices 之
  前。

* index

  产生的索引。

* footer

  两件事情： printindex，end document

