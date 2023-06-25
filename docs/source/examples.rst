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

The above example is also available as a script in the ``examples`` folder
called ``editing_affirmations.py``.


Affirmations From File
----------------------



Enable/Disable Affirmations
---------------------------