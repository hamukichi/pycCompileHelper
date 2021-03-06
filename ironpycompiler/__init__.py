#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Helps to compile IronPython scripts, using pyc.py.

This library helps you compile your IronPython scripts requiring the
Python standard library (or third-party pure-Python modules) into a
.NET assembly, using pyc.py.

.. note :: This library should be used on **CPython**, not IronPython,
           because :mod:`modulefinder` of IronPython does not work
           correctly.
"""

__author__ = "Hamukichi (Nombiri)"
__version__ = "1.0.0.a1"
__date__ = "2014-09-08"
__licence__ = "MIT License"
