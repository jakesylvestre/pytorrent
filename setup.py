#!/usr/bin/env python
from __future__ import with_statement
import sys
import unittest

try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.command.build_ext import build_ext
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

VERSION = '0.0.0'
DESCRIPTION = 'A simple python Bittorrent client'

with open('README.rst', 'r') as f:
    LONG_DESCRIPTION = f.read()

CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 0 - Development
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

class BuildFailed(Exception):
    pass

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        raise SystemExit(
            subprocess.call([sys.executable,
                             # Turn on deprecation warnings
                             '-Wd',
                             'tests/__init__.py']))

def run_setup():
    cmdclass = dict(test=TestCommand)

    kw = dict(cmdclass=cmdclass)

    setup(
        name="pytorrent",
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        classifiers=CLASSIFIERS,
        author="Jake Sylvestre",
        author_email="jakesyl@gmail.com",
        url="http://github.com/jakesyl/btclient",
        license="MIT License",
        packages=['pytorrent'],
        platforms=['any'],
        **kw)

def main():
    return run_setup()
    #runner = unittest.TextTestRunner(verbosity=1 + sys.argv.count('-v'))
    #suite = all_tests_suite()
    #raise SystemExit(not runner.run(suite).wasSuccessful())

if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()
