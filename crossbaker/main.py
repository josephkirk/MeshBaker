#/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys

try:
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    try:
        from PySide2 import QtCore, QtGui
        QtWidgets = QtGui
    except:
        sys.exit()

from .main_ui import UI
