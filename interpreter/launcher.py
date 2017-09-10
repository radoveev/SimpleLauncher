# -*- coding: utf-8 -*-
'''Launcher module of SimpleLauncher

This will add the pythonsrc directory to the python path, so import can find
the modules there.

It also imports the module selected in launchersettings.json
'''

__version__ = "0.1"


# --------------------------------------------------------------------------- #
# Import libraries
# --------------------------------------------------------------------------- #
import os
import os.path
import sys
import json
import importlib
from pathlib import Path


# --------------------------------------------------------------------------- #
# Import python module or package
# --------------------------------------------------------------------------- #
# append the directory for python packages to the python path
cwd = Path(os.getcwd()).resolve()
sys.path.append(str(cwd.parent / "pythonsrc"))

# determine target application name from settings
with Path("../launchersettings.json").resolve().open() as f:
    settings = json.load(f)
targetpackage = settings["launch"]

# launch target application
importlib.import_module(targetpackage)
