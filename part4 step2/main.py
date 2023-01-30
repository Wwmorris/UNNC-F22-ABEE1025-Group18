'''
U-calculator

Application entry point.
Author: Shuhang Li
Date: Jun 25, 2023
'''
from PySide6 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet

import sys

from window import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_cyan.xml')
    main_window = MainWindow()
    main_window.setupUI()
    main_window.show()
    sys.exit(app.exec())