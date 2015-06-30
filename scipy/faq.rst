Frequently asked questions
==========================

Numpy
-----

How do I find out the right function for my task?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can search for help in iPython terminal::

    np.lookfor('keyword')

How do I sort an array?
~~~~~~~~~~~~~~~~~~~~~~~

np.sort(a)
    Return a sorted copy
a.sort()
    Sort a array, in-place
np.argsort(a)
    Return the indices that would sort an array

How do I flatten an array?
~~~~~~~~~~~~~~~~~~~~~~~~~~

a.flatten()
    Return a flattened copy
np.ravel()
    Return a flattened copy only if needed
a.flat
    Return a 1D iterator, an instance of `np.flatiter`
np.flatiter
    C-contiguous iterator returned by ``a.flat``, which also supports advanced
    indexing.

What is np.newaxis?
~~~~~~~~~~~~~~~~~~~

It's just an alias for `None`, which is used in indexing to add a new axis of
length 1.

What is axis?
~~~~~~~~~~~~~

In Numpy dimensions are called ``axes`` (plural of axis) and the number of dimensions are called ``rank``. ``axis = 1`` means the row orientation in a matrix, which corresponds to the second index in ``[]``.

What is the difference between copy and view?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the difference through an example::

    # Simple assignment just binds `b` to the same object as `a` in Python
    a = np.arange(10)
    b = a
    b is a

    # Slicing creates a view (new object) of ``a``, which shares the same base
    b = a[:]
    b is not a
    b.base is a

    # This creates an entirely new object
    b = a.copy()
    b is not a
    b.base is not a


* In Python, assignment just binds ``name`` to the ``object`` returned from expression in
  RHS. Mutable parameter also passes a reference in function call.

* Different array objects can share the same data, while maintaining their own
  other attributes, like ``a.shape`` and ``a.strides``. ``a.view`` method, basic
  indexing and many array operations create view object. ``a[:]`` in the above
  example creates a view of ``a``.  Making changes to the view changes the
  original array.

* ``a.copy`` method returns an exact new array object. ``a.copy`` method,
  advanced indexing and some array operations, such as those failed to create a
  view object return a copy.

How do I re-interpret an array?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This re-interpret the underlying memory data with specified ``dtype``::

    a.view(dtype)


Why operations like np.reshape may sometimes return copy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When reshaping an array, Numpy tries to avoid copying data when possible. But
operations like ``a.T.reshape(-1)`` for a 2D array fails to create an expected
view with only one stride.

How do I find out the memory address of a single element a[i, j]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    offset = a.strides[0] * i + a.strides[1] * j

What is the rule for broadcasting?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Broadcasting rule allows you to make computations on arrays with different but
compatible shapes, so you don't always need to reshape or tile your arrays to
make them match.

* Prepend ``1`` to smaller arrays so that all arrays share the same  rank
  (``a.ndim``).
* Replace ``1`` with the largest dimension in each axis.
* If all arrays share the same shape, then it is called ``compatible``.

What is the difference between ``a *= 2`` and ``a = a * 2``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # in-place operation, faster
    a *= 2
    # or
    a[:] = a * 2

    # implicit-copy operation, slower
    a = a * 2

What is the difference between basic and advanced indexing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ndarray can be indexed using the standard Python ``x[obj]`` syntax, and ``obj``
determines the kind of indexing used.

Basic indexing
~~~~~~~~~~~~~~

Basic indexing is similar to standard Python sequence indexing.

* Invokes when ``obj`` is `slice` (:), `int` or a `tuple` of `slice`\s and `int`\s.
  `Ellipsis` (...) and `np.newaxis` (None) can also be interspersed.

* Returns *view* 

Advanced indexing
~~~~~~~~~~~~~~~~~

* Invokes when basic indexing condition is not satisfied. More specificly, it
  occurs when ``obj`` is any non-\ `tuple` sequence, or a `tuple` containing
  more than `slice`, `int`, `Ellipsis` and `np.newaxis`. Two most important
  types are ``integer array`` and ``boolean array`` (mask array).

* Returns *copy* 

* Boolean array is identical to ``a.nonzero()``, which returns indices of the
  elements. This then falls into integer array indexing.

Matplotlib
----------

Why no figure shows up after ``plt.show()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have chosen a non-interactive matplotlib backend like 'Agg'. Try to switch
to some interactive backends like 'GTKAgg', 'TkAgg' or 'Qt4Agg' (case
insensitive)

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


What's the difference between subplots and axes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While both are used to create new axes object, subplot positions the plot in a
regular grid and axes allows free placement in the figure.
