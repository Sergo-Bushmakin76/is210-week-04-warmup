#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defines a function with three paramters."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Function that answers if we have too many kittens for the litterboxes.

    Args:
        kittens (mixed): Arg defining number of kittens.
        litterboxes (int): Arg defining number of available litterboxes.
        catfood (boolean): represents whether any catfood exists.

    Returns:
        This statement ensures we have at least one litterbox for each kitten
        and that we have some catfood. It then uses inversion via not to answer
        whether or not we have too many kittens.

    Examples:
        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False
    """

    return not (litterboxes >= kittens and catfood)
