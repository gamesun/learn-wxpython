# -*- coding:utf-8 -*-

from distutils.core import setup
import py2exe


myOptions = {"py2exe":
    {"compressed": 1,
     "optimize": 2,
     "ascii": 1,
#      "includes":includes,
     "dll_excludes": ["MSVCP90.dll"],
     "bundle_files": 1}}

setup(
    options = myOptions,
    zipfile = None,
    windows = [{"script": "main.py"}]
)