========================================================
ErrorAffirmations: Affirmative error messages for Python
========================================================

Introduction
------------

:ErrorAffirmations: Affirmative error messages for Python
:Author: Thomas Gessey-Jones
:Version: 0.0.5
:Homepage: https://github.com/ThomasGesseyJones/ErrorAffirmations

``ErrorAffirmations`` is a Python library that provides affirmative error messages, to help you feel better about your
errors.


Installation
------------

Currently, the only way to install ``ErrorAffirmations`` is to clone the repository and install it manually:

.. code:: bash

  git clone git@github.com:ThomasGesseyJones/ErrorAffirmations.git
  cd ErrorAffirmations
  pip install .

Usage
-----

Simply import the ``erroraffirmations`` module and all errors will be appended with an affirmation:

.. code:: python

    import erroraffirmations

    raise Exception('Something went wrong')

.. code:: 

    Traceback (most recent call last):
      File "basic_usage.py", line 3, in <module>
        raise Exception('Something went wrong')
    Exception: Something went wrong

    At least you know that there is a problem, an invisible error is the worst kind.


You can also access the affirmations list directly, to add your own affirmations:

.. code:: python

    from erroraffirmations.affirmations import affirmations

    # Show current list of affirmations
    for affirmation in affirmations:
        print(affirmation)
    print("\n")

    # Remove all existing affirmations
    affirmations.clear()

    # Add your own affirmations
    affirmations.append("You are doing great!")

    # Show new list of affirmations
    print(affirmations)
    print("\n")

    # Let us see it in action
    raise ValueError("1 + 1 is not equal to 3")


.. code::

    You only learn by making mistakes.
    At least you know that there is a problem, an invisible error is the worst kind.
    Keep trying, we are sure your code will be perfect soon.
    Why not have a quick break? You deserve it, and it might help you solve this error.
    Thank you for using ErrorAffirmations, you have our full support in debugging this difficult error.


    ['You are doing great!']


    Traceback (most recent call last):
      File "editing_affirmations.py", line 20, in <module>
        raise ValueError("1 + 1 is not equal to 3")
    ValueError: 1 + 1 is not equal to 3

    You are doing great!

Code snippets demonstrating the usage of ``ErrorAffirmations`` can be found in the ``examples`` directory.


License
-------

``ErrorAffirmations`` is licensed under the MIT license. See the ``LICENSE`` file for more details.


Contributing
------------

Contributions are always welcome and greatly appreciated.

- You can `open an issue <https://github.com/ThomasGesseyJones/ErrorAffirmations/issues>`__ to report bugs or to propose new features.
- Or fork the repository, make your changes, and submit a pull request
