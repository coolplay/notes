reStructuredText 备忘录
=======================

参考链接
--------

* http://sphinx-doc.org/rest.html
* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* http://rest-sphinx-memo.readthedocs.org/en/latest/ReST.html


简单的行内公式
--------------

The standard way to markup inline math is to use the role ``:math:``. Actually if
you are tired of writing every inline formula in this tedious way, you can try
the following solutions, which are both quite clear:

* Use \$math\$ like $LaTeX$, with the help of extension `math_dollar
  <https://raw.githubusercontent.com/certik/theoretical-physics/master/exts/math_dollar.py>`_. 

  For example, the following code produces $\lim_{x \to \infty} \exp(-x) = 0$::

      \$\lim_{x \to \infty} \exp(-x) = 0\$


* Define default role to be math by adding to ``conf.py``::

      default_role = 'math'

  In this way, you can just include inline math by \`math\`. For example, the
  following code produces `\frac{n!}{k!(n-k)!} = \binom{n}{k}`::

      `\frac{n!}{k!(n-k)!} = \binom{n}{k}`

