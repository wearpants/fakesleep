#!/usr/bin/env python
from distutils.core import setup

setup(name='fakesleep',
      version="0.1",
      description='fake time.sleep() for use in tests',
      author='Pete Fein',
      author_email='pete@wearpants.org',
      url='http://github.com/wearpants/fakesleep',
      py_modules=['fakesleep'],
      license = "BSD",
      classifiers = [
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 3",
      "Development Status :: 5 - Production/Stable",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: BSD License",],
      long_description=open('README.rst').read(),
      )
