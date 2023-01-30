'''
U-calculator

Defines consts.
Author: Shuhang Li
Date: Jun 27, 2023
'''

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 550

# U widget
U_MARGIN = 20
U_VALID_TEXT_COLOR = "cyan"
U_INVALID_TEXT_COLOR = "darkgray"
U_PIXEL_SIZE = 40  # height of font size in pixels
U_HEIGHT = 100
U_STYLESHEET = """
    margin: {U_MARGIN}px;
    font-size:{U_PIXEL_SIZE}px;
    font-weight:bold;
    color: {color};
    border-radius: 5px;
""".format(U_MARGIN=U_MARGIN, U_PIXEL_SIZE=U_PIXEL_SIZE,color="{color}")

# the parts widget
PARTS_MARGIN = 20
PARTS_PADDING = 0

# the scroll area
DISPLAYAREA_STYLESHEET = f"""
    margin: {PARTS_MARGIN}px;
    padding: {PARTS_PADDING}px;
    background-color: #31363B;
    border-radius: 5px;
"""

# material widget group
MATERIAL_STYLESHEET = """
    margin: 2px;
    padding: 2px;
    border: 1px solid darkgray;
    border-radius: 5px;
    font-weight: bold;
    background-color:#232629;
    color:black;
"""
MATERIAL_LABEL_STYLESHEET = """
    border: 0px;
    text-align: right;
    color: cyan;
    font-weight: normal;
"""
MATERIAL_VALUE_STYLESHEET = """
QLineEdit {
    color: white;
    border: 1px solid darkgray;
}
"""
MATERIAL_VALUE_INVALID_STYLESHEET = """
QLineEdit {
    color: red;
    border: 1px solid red;
}
"""

# the ADD NEW MATERIAL button
ADD_BUTTON_HEIGHT = 100
ADD_BUTTON_MARGIN = 10
ADD_BUTTON_STYLESHEET = """
QPushButton:hover {
    color: LightCyan;
}
QPushButton:pressed {
    color: white;
    border: 1px solid white;
}
"""

# the close button
CLOSE_BUTTON_WIDTH = 70
CLOSE_BUTTON_HEIGHT = 50
CLOSE_BUTTON_STYLESHEET = """
QPushButton {
    color: DeepPink;
    margin-left: 150px;
}
QPushButton:hover {
    color: Pink;
}
QPushButton:pressed {
    color: white;
    border: 1px solid white;
}
"""