#!/usr/bin/env python
""" Get Version

This script will print the version of the current project.
"""


import sys
from check_version import run_on_commandline, version_file


def main():
    """ Print the current version of the project """

    # Get current version from version file
    current_version = run_on_commandline("cat", version_file)
    current_version = current_version.split("=")[-1].strip().strip("'")

    # Print current version
    sys.stdout.write(f"{current_version}")


if __name__ == '__main__':
    main()
