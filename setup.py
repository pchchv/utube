#!/usr/bin/env python
"""This module contains setup instructions for tube."""
import os
import codecs
from setuptools import setup
from tube.version import __version__

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open(os.path.join(here, "tube", "version.py")) as fp:
    exec(fp.read())

setup(
    name="tube",
    version=__version__,  # noqa: F821
    author="Evgenii Pochechuev",
    author_email="ipchchv@gmail.com",
    packages=["tube", ],
    package_data={"": ["LICENSE"], },
    url="https://github.com/pchchv/tube",
    license="Apache-2.0 license",
    entry_points={
        "console_scripts": [
            "tube = tube.cli:main"], },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache-2.0 license",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    description=("Python 3 library for downloading YouTube Videos."),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description,
    zip_safe=True,
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": "https://github.com/pchchv/tube/issues",
        "Read the Docs": "https://github.com/pchchv/tube/docs",
    },
    keywords=["youtube", "download", "video", "stream",],
)
