'''
U-calculator

Defines the main window.
Author: Shuhang Li
Date: Jun 25, 2023
'''
from PySide6 import QtCore, QtWidgets, QtGui

from parts import QParts
from const import *
from calculate import calculate


class MainWindow(QtWidgets.QMainWindow):
    def setupUI(self):
        '''
        Add and set widgets to the main window.
        '''
        self.setWindowTitle("U-calculator")
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Display the U value with an edit.
        # Therefore the result could be copied, and read only is also necessary
        # so that the result wouldn't be modified.
        self.U = QtWidgets.QLineEdit(self)
        self.U.setGeometry(QtCore.QRect(
            0,
            0,
            self.width(),
            U_HEIGHT
        ))
        self.U.setStyleSheet(U_STYLESHEET.format(color=U_VALID_TEXT_COLOR))
        self.U.setReadOnly(True)

        # The parts widget is the container of the different material parts.
        self.parts = QParts(self)
        self.parts.setGeometry(QtCore.QRect(
            0,
            self.U.height(),
            self.width(),
            self.height() - self.U.height()
        ))
        self.parts.initWidgets(self.calculate)

    def calculate(self):
        """
        When edited, calculate current r_total and display in U_widget.
        This is a slot function that should be called everywhere if parts_widget.collect()
        would be changed.
        """
        U = calculate(self.parts.collect())
        self.U.setStyleSheet(U_STYLESHEET.format(color=U_INVALID_TEXT_COLOR))
        if U is not None:
            self.U.setText(str(U))
            self.U.setStyleSheet(U_STYLESHEET.format(color=U_VALID_TEXT_COLOR))
        self.U.setCursorPosition(0)