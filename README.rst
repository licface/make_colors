\$ make_colors\_
==================

This is make command line text colored


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    $ pip install make_colors

make_colors supports Python 2 and newer, Python 3 and newer, and PyPy.

.. _pip: https://pip.pypa.io/en/stable/quickstart/


A Simple Example
----------------

What does it look like? Here is an example of a simple make_colors program:

.. code-block:: python

    from make_colors import make_colors
    
    print make_colors('This is White on Red', 'white', 'red')
    print make_colors('This is Light White on Light Red', 'lightwhite', 'lightred')
    print make_colors('This is Light White on Light Magenta', 'lw', 'm')


And what it looks like when run:

.. code-block:: text

    $ python hello.py 
    This is White on Red
    This is Light White on Light Red
    This is Light White on Light Magenta


Support
------

*   Python 2.7 +, Python 3.x
*   Windows, Linux

Links
-----

*   License: `BSD <https://github.com/licface/make_colors/blob/master/LICENSE.rst>`_
*   Code: https://github.com/licface/make_colors
*   Issue tracker: https://github.com/licface/make_color/issues