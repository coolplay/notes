Matplotlib
==========

Todo
----

* controll line properties
* set ticks and ticklabels
* spines visible

FAQ
---

How to controll line properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``plt.plot`` returns a list of lines, which can be controlled with::

    line, = plt.plot(x, y)
    line.get_*()
    line.set_*()

Alternatively, you can use ``plt.setp`` like this::

    lines = plt.plot(x, y)
    plt.setp(lines, linewidth=2.0)

which takes a single object or a list of objects.
