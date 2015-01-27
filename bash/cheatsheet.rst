Shell 备忘录
============


常用快捷键
----------

Alt + f
    Jump forward a word
Alt + b
    Jump backword a word

    .. note::

      如果将 ``alt`` 键改为 ``ctrl`` ，表示移动的单位是character。为方便起见，可
      以自定义快捷键，在 ``~/.inputrc`` 中添加如下代码::

          "\e[1;5C": forward-word   # ctrl + right
          "\e[1;5D": backward-word  # ctrl + left

Alt + d
    删除光标后的一个单词    
Ctrl + a,e
    跳至行首，行尾
Ctrl + n,p
    上一条，下一条命令。类似于上下箭头。
Ctrl + xx
    切换至上一个光标位置，默认为行首。

参考:

* `Readline shortcuts <http://www.bigsmoke.us/readline/shortcuts>`_

* `Bash Reference Manual
  <http://www.gnu.org/software/bash/manual/bashref.html#Bindable-Readline-Commands>`_


常用命令
--------

zip zipfile folder/\*.dat \*.dat
    将 ``folder`` 和 当前目录下的 ``.dat`` 文件都添加到 ``zipfile.zip`` 压缩文件
    中。 若 ``zipfile.zip`` 已存在，则表示向其中添加新文件，覆盖旧文件。 

unzip -l zipfile.zip
    查看 ``zipfile.zip`` 压缩文件中的目录结构。

