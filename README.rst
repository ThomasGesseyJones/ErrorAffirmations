========================================================
ErrorAffirmations: Affirmative error messages for Python
========================================================

Introduction
------------

:ErrorAffirmations: Affirmative error messages for Python
:Author: Thomas Gessey-Jones
:Version: 0.1.0-rc.2
:Homepage: https://github.com/ThomasGesseyJones/ErrorAffirmations
:Documentation: https://erroraffirmations.readthedocs.io

.. image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python version
.. image:: https://github.com/ThomasGesseyJones/ErrorAffirmations/actions/workflows/CI.yaml/badge.svg
   :target: https://github.com/ThomasGesseyJones/ErrorAffirmations/actions/workflows/CI.yaml
   :alt: Testing Status
.. image:: https://codecov.io/gh/ThomasGesseyJones/ErrorAffirmations/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/ThomasGesseyJones/ErrorAffirmations
   :alt: Test Coverage Status
.. image:: https://readthedocs.org/projects/erroraffirmations/badge/?version=latest
   :target: https://erroraffirmations.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/ThomasGesseyJones/ErrorAffirmations/blob/main/LICENSE
   :alt: License information

``ErrorAffirmations`` is a Python package that appends affirmations to
to help you feel better about your errors.

Quickstart
----------

First install ``ErrorAffirmations``:

.. code:: bash

   pip install erroraffirmations

Then import the ``erroraffirmations`` module:

.. code:: python

   import erroraffirmations

and your ready to go! All errors will now be appended with an affirmation.


Features
--------

Currently, ``ErrorAffirmations`` has the following features:

- Appends affirmations to all errors
- Allows you to add your own affirmations and remove existing affirmations
- Allows you to enable/disable the adding of affirmations
- Utilities to load affirmations from a file
- A set of default affirmations to keep you motivated


Requirements
------------

``ErrorAffirmations`` requires Python 3.7 or higher. It has no
required dependencies.

For documentation generation you will need:

- Sphinx
- sphinx-rtd-theme
- numpydoc

Testing requires:

- pytest
- pytest-cov
- flake8
- pydocstyle
- pre-commit
- packaging



Installation
------------

``ErrorAffirmations`` can be  directly installed via pip:

.. code:: bash

   pip install erroraffirmations 

or from the repository:

.. code:: bash

  git clone git@github.com:ThomasGesseyJones/ErrorAffirmations.git
  cd ErrorAffirmations
  python -m pip install .

A new installation can be verified as working by running the tests suite:

.. code:: bash

   python -m pip install ".[test]"
   python -m pytest


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


Code snippets demonstrating the advanced usage of ``ErrorAffirmations`` can be
found in the `examples <https://github.com/ThomasGesseyJones/ErrorAffirmations/tree/main/examples>`__ directory.


Documentation
-------------

The documentation for ``ErrorAffirmations`` can be found at
`erroraffirmations.readthedocs.io <https://erroraffirmations.readthedocs.io/en/latest/>`__.

To build the documentation locally, you will need to install the
documentation dependencies:

.. code:: bash

   python -m pip install ".[docs]"

Then you can build the documentation:

.. code:: bash

   cd docs
   make html

The documentation will be built in the ``docs/build`` directory.
Open ``docs/build/html/index.html`` in your browser to view the documentation.

License
-------

``ErrorAffirmations`` is licensed under the MIT license. See the
`LICENSE <https://github.com/ThomasGesseyJones/ErrorAffirmations/blob/main/LICENSE>`__
file for more details.


Contributing
------------

Contributions are always welcome and greatly appreciated.

- You can `open an issue <https://github.com/ThomasGesseyJones/ErrorAffirmations/issues>`__ to report bugs or to propose new features.
- Or fork the `repository <https://github.com/ThomasGesseyJones/ErrorAffirmations>`__, make your changes, and submit a `pull request <https://github.com/ThomasGesseyJones/ErrorAffirmations/pulls>`__.

If it is your
first time contributing to ``ErrorAffirmations``, please read the
`contributing guidelines <https://github.com/ThomasGesseyJones/ErrorAffirmations/blob/main/.github/CONTRIBUTING.md>`__
before making a pull request.
