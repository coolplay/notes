.. highlight:: rest

常见问题
========

如何使得程序代码高亮显示
------------------------

在 Sphinx 中，语法高亮通过 Pygments 实现，并通过如下方式灵活地处理：

* 每一个文档都有默认的语法高亮规则，即 ``'python'`` ，不过你可以在 config.py 中
  设定常用的语言，需要修改的变量为 ``highlight_language`` 。
* 你也可以在特定文档中加入 ``highlight`` 指令的值::

    .. highlight:: c

  这样该文件中的代码段会渲染成 C 语言，直到你又重新指定 ``highlight`` 指令。
* 除此之外，你也可以明确的指定单个段的语法高亮规则，这就需要用到
  ``code-block`` 或者等价的 ``sourcecode`` 指令。比如下面是一段 Ruby 程序:

  .. code-block:: ruby

      # Output "I love Ruby"
      say = "I love Ruby"
      puts say

      # Output "I *LOVE* RUBY"
      say['love'] = "*love*"
      puts say.upcase

      # Output "I *love* Ruby"
      # five times
      5.times { puts say }

* 支持语法高亮的语言，参见 http://pygments.org/docs/lexers/
