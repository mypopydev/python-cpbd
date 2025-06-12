#!/usr/bin/env python

from __future__ import absolute_import, print_function, unicode_literals

# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Read the contents of README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="cpbd",
    version="1.0.7",
    description="A Python implementation of the CPBD (Cumulative Probability of Blur Detection) sharpness metric",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jun Zhao",
    author_email="junzhao@mypopydev.com",
    url="https://github.com/mypopydev/python-cpbd",
    packages=["cpbd"],
    python_requires=">=3.7"
)
