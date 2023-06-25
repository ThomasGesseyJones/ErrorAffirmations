========
Examples
========

Here are some examples of how to use ``ErrorAffirmations`` and its various
features:

- `Quick Start`_
- `Add/Remove Affirmations`_
- `Affirmations From File`_
- `Enable/Disable Affirmations`_



Quick Start
-----------

The quickest way to get started is to just import ``erroraffirmations`` and
you're ready to go. Try running the following code:

.. code:: python

   import erroraffirmations

   raise Exception('Something went wrong')

You should see something like this:

.. code:: text

    Traceback (most recent call last):
      File "examples/quick_start.py", line 4, in <module>
        raise Exception('Something went wrong')
    Exception: Something went wrong

    You're a skilled programmer, and this error is just a temporary challenge. Keep going!

Notice the last line of the error message. That's the affirmation. It's
randomly selected from a list of affirmations that come with the package. You
can add your own affirmations, or even disable them entirely. See the next
example for more details.

Affirmations are only appended to the error message if the error message is
not caught. If you catch the error, the affirmation will not be appended.

The above example is also available as a script in the ``examples`` folder
called ``quick_start.py``.

Add/Remove Affirmations
-----------------------

You can add your own affirmations to the list of affirmations that come with
the package. You can also remove affirmations from the list. Here's an example
of how to do that:

.. code:: python

    from erroraffirmations import add_affirmations, remove_affirmations, \
        get_affirmations, clear_affirmations

    # Let us start by clearing the affirmations
    clear_affirmations()

    # Add some affirmations
    add_affirmations(["You are doing great!", "An affirmation we don't like"])

    # Show the current set of affirmations
    print(get_affirmations())
    print("\n")

    # Remove an affirmation
    remove_affirmations("An affirmation we don't like")

    # Show the current set of affirmations
    print(get_affirmations())

    # And finally show the affirmations in action
    raise ValueError("1 + 1 is not equal to 3")

The output of the above code is:

.. code:: text

    {"An affirmation we don't like", 'You are doing great!'}


    {'You are doing great!'}
    Traceback (most recent call last):
      File "../examples/editing_affirmations.py", line 23, in <module>
        raise ValueError("1 + 1 is not equal to 3")
    ValueError: 1 + 1 is not equal to 3

    You are doing great!

Note one or multiple affirmations can be added or removed at once. This
example also serves to illustrate the ``clear_affirmations`` and
``get_affirmations`` functions.

If you ever want to revert to the default affirmations, you can do so by
calling the ``reset_affirmations`` function.

The above example is also available as a script in the ``examples`` folder
called ``editing_affirmations.py``.


Affirmations From File
----------------------

You can also load affirmations from a file. The file should be a text file
with one affirmation per line. Such a text file ``my_affirmations.txt`` is
included in the ``examples`` folder. With three affirmations:

.. code:: text

    Example affirmation 1
    Example affirmation 2
    Example affirmation 3

Here's an example of how to do load it, overriding the existing affirmations,

.. code:: python

    from erroraffirmations import load_affirmations_from_file

    # Add affirmations from a file
    load_affirmations_from_file("my_affirmations.txt", append=False)

    _ = 1/0

The output of the above code is:

.. code:: text

    Traceback (most recent call last):
      File "loading_affirmations.py", line 8, in <module>
        _ = 1/0
    ZeroDivisionError: division by zero

    Example affirmation 3

Rather than overriding the existing affirmations, you can also append the
affirmations from the file to the existing affirmations. To do that, just
change ``append=False`` to ``append=True`` in the above example. Appending
affirmations is the default behavior.

The above example is also available as a script in the ``examples`` folder
called ``loading_affirmations.py``.


Enable/Disable Affirmations
---------------------------

You can enable or disable affirmations through the
``enable_affirmations`` and ``disable_affirmations`` functions.
To check if affirmations call the ``affirmations_enabled`` function.
By default affirmations are enabled.

Here's an example of how to do that:

.. code:: python

    from erroraffirmations import disable_affirmations, affirmations_enabled

    # Defaults to on
    print(affirmations_enabled())

    # Turn off affirmations
    disable_affirmations()

    # Now affirmations are off
    print(affirmations_enabled())

    # And finally show that affirmations are not displayed
    raise TypeError("Boring regular error message")


The output of the above code is:

.. code:: text

    True
    False
    Traceback (most recent call last):
      File "../examples/disabling_affirmations.py", line 15, in <module>
        raise TypeError("Boring regular error message")
    TypeError: Boring regular error message

The above example is also available as a script in the ``examples`` folder
called ``disabling_affirmations.py``.

Affirmations are also disabled if there are no affirmations to display. E.g.
if you run the following code:

.. code:: python

    from erroraffirmations import clear_affirmations

    # Remove all existing affirmations
    clear_affirmations()

    # No affirmation is displayed
    raise ValueError("A normal error message")


The output of the above code is:

.. code:: text

    Traceback (most recent call last):
      File "../examples/empty_affirmations.py", line 9, in <module>
        raise ValueError("A normal error message")
    ValueError: A normal error message

As with all the other examples, this example is also available as a script in
the ``examples`` folder called ``empty_affirmations.py``.

