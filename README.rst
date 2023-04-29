========================================================
ErrorAffirmations: Affirmative error messages for Python
========================================================

Introduction
------------

:ErrorAffirmations: Affirmative error messages for Python
:Author: Thomas Gessey-Jones
:Version: 0.0.1
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

.. code:: bash
    Traceback (most recent call last):
      File "basic_usage.py", line 3, in <module>
        raise Exception('Something went wrong')
    Exception: Something went wrong

    At least you know that there is a problem, an invisible error is the worst kind.

