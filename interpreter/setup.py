# -*- coding: utf-8 -*-
'''Build script for SimpleLauncher

This script uses cx_Freeze to create a distributable version of SimpleLauncher.
cx_Freeze is cross platform, but this script currently only supports windows

It requires stdlib_list to be available to your python installation. You can
install it via pip:
    pip install stdlib_list
'''

# import libraries
import importlib
import os.path

from cx_Freeze import setup, Executable
from stdlib_list import stdlib_list


# set environment variables necessary for cxfreeze and some stdlib modules
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# import the standard library
imported_stdlib = []
for libname in stdlib_list("3.6"):
    if libname in {"macpath", "os.path"}:
        print("INFO: Skipped", libname)
        continue
    if (libname.startswith("__") or
        libname.startswith("test") or
        libname.startswith("xml.parsers.expat") or
        libname.startswith("tkinter")):
        print("INFO: Skipped", libname)
        continue
    try:
        importlib.import_module(libname)
        imported_stdlib.append(libname)
    except ImportError:
        print("WARNING: Failed to import", libname)

## add some modules manually
#includes = imported_stdlib + ["xml.parsers.expat.errors"]

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": imported_stdlib,
                     "excludes": ["launcher", "tkinter", "tcl"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

exe = Executable(
    script="launcher.py",
    base=base)

# TODO fetch version and description from launcher.py
setup(
    name="Simple Launcher",
    version="0.1",
    description=("Imports a python module or package. " +
                 "Comes with Qt included."),
    options={"build_exe": build_exe_options},
    executables=[exe])
