#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
main script
"""
import sys
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from distutils import util

import os
import sys

import pyossia

from explorer import ZeroConfExplorer

from PyQt5.QtCore import QSettings, pyqtSignal
from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QTreeView, QSlider, QListView, QGroupBox, QCheckBox, QComboBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.Qt import *


class MainWindow(QWidget):
    """
    Main Window
    """
    valueChanged = pyqtSignal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        # create a ZeroConf Explorer
        self.explorer = ZeroConfExplorer("oscjson apps")
        layout = QGridLayout()
        layout.addWidget(self.explorer, 0, 0)
        self.setLayout(layout)
        #self.setMaximumSize(600, 400)
        self.setWindowTitle("OSCQuery Explorer")
        self.readSettings()

    def closeEvent(self, closevent):
        """
        method called when the main window wants to be closed
        """
        self.writeSettings()
        import time
        time.sleep(1)
        closevent.accept()

    def readSettings(self):
        """
        read the settings
        """
        settings = QSettings('pixel-stereo', 'oscquery_explorer')
        pos = settings.value('pos')
        size = settings.value('size')
        if pos:
            self.move(pos)
        if size:
            self.resize(size)

    def writeSettings(self):
        """
        write settings
        """
        settings = QSettings('pixel-stereo', 'oscquery_explorer')
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())


if __name__ == "__main__":
    # python2 only
    try:
        reload(sys)
        sys.setdefaultencoding('utf8')
    except NameError:
        pass
    # end python 2 only
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
    zeroconf.close()
