#! /usr/bin/env python
from setuptools import setup, find_packages
from os import path, listdir
import re

pkg_name = "calculator"
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), "r") as f:
    long_description = f.read()

with open(path.join(here, pkg_name, 'version.py')) as f:
    exec(f.read())

requirements = []
if path.isfile(path.join(here, 'requirements.txt')):
    with open(path.join(here, 'requirements.txt')) as f:
        requirements = ['{pkg} @ {target}#egg={pkg}'.format(pkg=re.search('/([A-Za-z0-9\-]+)\.git',
            r).group(1), target=r) if '+' in r else r for r in f.read().split()]

setup(
    name=pkg_name,
    version=__version__,
    author="Raphael Guzman",
    author_email="raphael.h.guzman@gmail.com",
    description="A demo calculator app...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://doesnt.exist",
    packages=find_packages(exclude=['test*', 'docs']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
)
