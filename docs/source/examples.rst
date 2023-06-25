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


Add/Remove Affirmations
-----------------------



Affirmations From File
----------------------



Enable/Disable Affirmations
---------------------------