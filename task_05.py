#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Set defaults value in a function definition"""


def defaults(my_required=None, my_optional=True):
    """Sets a default in the function and compares boolean parameters.

    Args:
        my_required (bool): compares to my_optional.
        my_optional (bool): compares to my_required.  default: True.

    Returns:
        boolean: compares the two arguments.

    Examples:
        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
    """

    return my_optional is my_required
