#!/usr/bin/env python

import os
import sys

import flat_flog

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.md')) as f:
        README = f.read()
except IOError:
    README = ''
try:
    with open(os.path.join(here, 'CHANGES.md')) as f:
        CHANGES = f.read()
except IOError:
    CHANGES = ''

requires = [
    'Flask >= 0.10',
    'Flask-FlatPages >= 0.5',
    'Frozen-Flask >= 0.11',
    'cssmin >= 0.1.4'
]

setup(
    name='Flat-Flog',
    version=flat_flog.__version__,
    description='An flat-page blog written in Python using the Flask Microframework and its extensions.',
    long_description=README + '\n\n' + CHANGES,
    author='Josh Finnie',
    author_email='josh.finnie@gmail.com',
    url='https://github.com/joshfinnie/flat-flog',
    packages=find_packages(),
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
