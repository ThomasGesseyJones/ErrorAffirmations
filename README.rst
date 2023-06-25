========================================================
ErrorAffirmations: Affirmative error messages for Python
========================================================

Introduction
------------

:ErrorAffirmations: Affirmative error messages for Python
:Author: Thomas Gessey-Jones
:Version: 0.1.0-beta.13
:Homepage: https://github.com/ThomasGesseyJones/ErrorAffirmations

.. image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python version
.. image:: https://github.com/ThomasGesseyJones/ErrorAffirmations/actions/workflows/CI.yaml/badge.svg
   :target: https://github.com/ThomasGesseyJones/ErrorAffirmations/actions/workflows/CI.yaml
   :alt: Testing Status
.. image:: https://codecov.io/gh/ThomasGesseyJones/ErrorAffirmations/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/ThomasGesseyJones/ErrorAffirmations
   :alt: Test Coverage Status
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/ThomasGesseyJones/ErrorAffirmations/blob/main/LICENSE
   :alt: License information


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

    Remember, every error you encounter is an opportunity for growth and learning. You're capable of overcoming this challenge!


You can also access the affirmations list directly, to add your own affirmations:

.. code:: python

    from erroraffirmations import add_affirmation, get_affirmations, \
    clear_affirmations

    # Show part of the current list of affirmations
    for affirmation in list(get_affirmations())[:5]:
        print(affirmation)
    print("\n")

    # Remove all existing affirmations
    clear_affirmations()

    # Add your own affirmations
    add_affirmation("You are doing great!")

    # Show new list of affirmations
    print(get_affirmations())
    print("\n")

    # Let us see it in action
    raise ValueError("1 + 1 is not equal to 3")


.. code::

    The best programmers encounter errors regularly. It's a sign that you're exploring new territory and pushing your limits.
    Mistakes are an essential part of the learning process. You're getting closer to the solution with each error you encounter.
    The fact that you're facing this challenge head-on shows your determination and dedication. You've got this!
    Take a moment to step back, breathe, and approach the problem from a different angle. A fresh perspective can lead to breakthroughs.
    Remember, every error you encounter is an opportunity for growth and learning. You're capable of overcoming this challenge!


    {'You are doing great!'}


    Traceback (most recent call last):
      File "/home/thomas/Documents/Pet_Projects/ErrorAffirmations/examples/editing_affirmations.py", line 22, in <module>
        raise ValueError("1 + 1 is not equal to 3")
    ValueError: 1 + 1 is not equal to 3

    You are doing great!

    Process finished with exit code 1


Code snippets demonstrating the usage of ``ErrorAffirmations`` can be found in the ``examples`` directory.


License
-------

``ErrorAffirmations`` is licensed under the MIT license. See the ``LICENSE`` file for more details.


Contributing
------------

Contributions are always welcome and greatly appreciated.

- You can `open an issue <https://github.com/ThomasGesseyJones/ErrorAffirmations/issues>`__ to report bugs or to propose new features.
- Or fork the repository, make your changes, and submit a pull request
