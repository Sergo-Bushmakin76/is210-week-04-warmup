#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Takes a string, miltiplies its instance by two and inserts it into a
        string statement.

    Args:
        wink (str): Arg string to be mutliplied by numwink.
        numwink (int): Arg to multiply quanitity of wink. Default: 2.

    Returns:
        variable: contains a String statement with 2 args.

    Examples:

        >>> know_what_i_mean('wink ')
        'Know what I mean? wink wink, nudge nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
