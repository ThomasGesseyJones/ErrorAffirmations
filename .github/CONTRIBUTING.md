# Contributing

Thank you for your interest in contributing to ErrorAffirmations.
If you have a new feature or bug fix, please first consult the list of
[open issues](https://github.com/ThomasGesseyJones/ErrorAffirmations/issues)
in case your contribution is already under development. If it is not, please
[submit a new issue](https://github.com/ThomasGesseyJones/ErrorAffirmations/issues/new)
so that we can discuss it and figure out how to integrate it into the project.

To make a contribution, fork the 
[repository](https://github.com/ThomasGesseyJones/ErrorAffirmations)
and create an appropriately-named branch. When you are finished with your work,
submit a [pull request](https://github.com/ThomasGesseyJones/ErrorAffirmations/pulls) 
from your forked repository to this one. Your pull request will be reviewed and
merged if everything looks good. If you have any questions, feel free to ask!

## Pre-commit hooks

ErrorAffirmations uses flakes8 and pydocstyle to ensure that all code is
formatted correctly and of a consistent style. To avoid linting errors, you may
want to install a pre-commit hook. This will run the linters on your code
before you commit it and will prevent you from committing code that does not
pass the linters. To install the pre-commit hook, run the following commands:

```bash
pip install pre-commit flake8 pydocstyle
pre-commit install
``` 

You can uninstall the pre-commit hook by running the following command:

```bash
pre-commit uninstall
```

You can also run the linters manually by running the following commands:

```bash
flake8 erroraffirmations bin examples tests
pydocstyle --convention=numpy erroraffirmations bin examples tests
```

## Testing

ErrorAffirmations uses pytest for testing. First, make sure that pytest is
installed:

```bash
pip install pytest
```

Then run the tests with the following command:

```bash
python -m pytest
```

All tests should pass before you submit a pull request. 
New features and bug fixes should be accompanied by tests. If you are
unsure how to test your code, the issue or pull request comment thread 
is a good place to ask for help. If your contribution reduces the
coverage of the test suite, it will fail testing and will not be merged.


## Versioning

ErrorAffirmations uses [semantic versioning](https://semver.org/). The version
number is stored in both `erroraffirmations/_version.py` and `README.rst`.
When you make a contribution, please increment the version number appropriately
in both of these files. The version number should be incremented according to
the following rules:

* If the new contribution is a bug fix, increment the patch version number.
* If the new contribution adds a new feature without breaking backward
  compatibility, increment the minor version number.
* If the new contribution breaks backward compatibility, increment the major
  version number.
* Pre-release versions should be suffixed with a hyphen and a pre-release identifier. 


## Documentation

ErrorAffirmations uses [Sphinx](https://www.sphinx-doc.org/en/master/) for
documentation. To build the documentation, first install Sphinx and the
documentation dependencies:

.. code:: bash

   python -m pip install ".[docs]"

Then you can build the documentation:

.. code:: bash

   cd docs
   make html

The documentation will be built in the `docs/build` directory. You can view it
by opening `docs/build/html/index.html` in your web browser.

If you are adding a new feature, please add documentation for it. In particular,
please ensure any new API functions are documented in the appropriate place in
`docs/source/api.rst`. If your change is substantial, you may want to add a new 
example to the documentation
and `examples` to illustrate how to use the new feature. 



## License

ErrorAffirmations is licensed under the MIT license. See the
[LICENSE](https://github.com/ThomasGesseyJones/ErrorAffirmations/blob/main/LICENSE)
file for more information.

