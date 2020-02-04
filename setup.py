#!/usr/bin/python

from distutils.core import setup
import py2exe, sys, os

# appending binary to the file
sys.argv.append("py2exe")
setup (
    options = {'py2exe': {'bundle_files': 1}},
    console = [{'script': 'firefox.py'}],
)
