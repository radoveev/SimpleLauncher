# -*- coding: utf-8 -*-
'''Launcher module of SimpleLauncher

This will add the pythonsrc directory to the python path, so import can find
the modules there.

It also imports the module selected in launchersettings.json

Copyright (C) 2017  Radomir Matveev

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
'''

# --------------------------------------------------------------------------- #
# Import libraries
# --------------------------------------------------------------------------- #
import sys
import json
import importlib
from pathlib import Path

# import Qt
from PyQt5 import (QtWidgets, QtGui, QtCore, QtSvg, QtChart,
                   QtWebEngineCore, QtWebEngineWidgets)
from PyQt5.QtCore import Qt


# --------------------------------------------------------------------------- #
# Declare module globals
# --------------------------------------------------------------------------- #
__version__ = "0.2"


# --------------------------------------------------------------------------- #
# Import python module or package
# --------------------------------------------------------------------------- #
module_path = Path(__file__).resolve()  # absolute path to this file
launcher_parent = module_path.parent.parent

# load settings
settings_path = (launcher_parent / "launchersettings.json").resolve()
with settings_path.open() as f:
    settings = json.load(f)

# append the directory for python packages to the python path
srcdirpath = (launcher_parent / settings["source_directory"]).resolve()
sys.path.append(str(srcdirpath))

# determine target application name from settings
targetpackage = settings["launch_module"]

# launch target application
importlib.import_module(targetpackage)
# TODO: show nice error if this fails
