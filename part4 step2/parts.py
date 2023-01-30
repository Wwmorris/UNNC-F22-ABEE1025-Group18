'''
U-calculator

Defines the parts widget.
The parts widget inherits from the QGroupBox, which allows different parts of material being
modified.

Author: Shuhang Li
Date: Jun 27, 2023
'''

import re

from PySide6 import QtCore, QtGui, QtWidgets

from const import *
from material import Material
import resources

class QParts(QtWidgets.QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        layout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMinimumSize)

        self.setWidgetResizable(True)
        displayArea = QtWidgets.QGroupBox() # the actual place showing the materials
        self.setWidget(displayArea)
        displayArea.setLayout(layout)
        displayArea.setStyleSheet(DISPLAYAREA_STYLESHEET)

        self.layout = layout
        self.display = displayArea
        self.calc_func = None

    def initWidgets(self, calc_func):
        """
        Initialize inner widgets (mainly the add button).
        calc_func(function): slot function for material widgets to connect
          on modefied or removed.
        """
        self.calc_func = calc_func

        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setIcon(QtGui.QIcon(":add-circle.svg"))
        self.add_button.setText("Add a material")
        self.add_button.setGeometry(QtCore.QRect(
            0,
            0,
            self.width(),
            ADD_BUTTON_HEIGHT
        ))
        self.add_button.setStyleSheet(ADD_BUTTON_STYLESHEET)

        self.layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add)

    def add(self):
        """
        Add a new material.
        """
        new_material=Material(calc_func=self.calc_func)

        # the order issue :)
        count=self.layout.count()
        self.layout.removeWidget(self.layout.itemAt(count-1).widget())
        self.layout.addWidget(new_material)
        self.layout.addWidget(self.add_button)

    def collect(self):
        """
        Return current material information.
        Format:
        [
            {
                "name": "A",
                "l": 1,
                "k": 0.5
            },
            {
                "name": "B",
                "l": 1.5,
                "k": 0.8
            },
            ...
        ]
        """
        ret = []
        for i in range(0, self.layout.count() - 1):
            material = self.layout.itemAt(i).widget()
            data = material.collect()
            if data is not None:
                ret.append(data)
        return ret