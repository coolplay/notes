.. highlight:: vim

vim 备忘录
==========

常用快捷键
----------

.. For key-value pairs to list hotkeys, we can use ``:Field list:`` or
   ``Definition list``(We use this here). See
   http://rest-sphinx-memo.readthedocs.org/en/latest/ReST.html#definition-list

zt, zb, zz
    将光标所在行移动到页首，页尾，页中。

e, w, b
    将光标移动到词尾，下一个词头，上一个词头。这里的词(word)类似于程序中的变量名
    ，由字母数字和下划线组成。与之相对应的大写版命令 ``E, W, B`` 以 WORD 作为单
    位，将非空格字符当做字符。

gq{motion}
    格式化 motion 所经历的文本行。gqq: 当前行。gqj: 当前行与下一行。gqG: 当前行
    到文本末尾。gqap: 所在段落。

Ctrl-O, Ctrl-I 
    跳转回上一个，下一个光标的历史访问行 (参见 ``:ju[mps]``)。

Ctrl-R + ``"``
    用于插入和末行模式，将寄存器 ``"`` 中的内容粘贴到相应位置。类似于命令行模式
    下的 ``" + "`` 。

\:w !sudo tee %
    可在事后保存需 root 权限的文件，如 ``/etc/hosts`` 。


常见问题列表
------------

``let`` 与 ``set`` 的区别
~~~~~~~~~~~~~~~~~~~~~~~~~

``set`` 用于设置 *选项(option)* ， ``let`` 则用于给 *变量(variable)* 赋值。在
vim 中，选项与变量可以具有相同的名字，当两者并不代表同一个事物。这可以通过以下两
个命令的结果看出::

    " This shows the value of variable ``number``, which is undefined
    :echo  number 
    " This shows the value of option ``number``, which is 0 when lineno is off
    :echo &number
    
选项的值恰巧通过在选项前加 ``&`` 获取，因此以下两条语句等价::
    
    :set  tw = 40
    :let &tw = 40

参见 http://learnvimscriptthehardway.stevelosh.com/chapters/19.html

