
class EnergyPlus(object):
    # construction method
    def __init__(self, window_U_value, window_SHGC_value):
        self.window_U_value = window_U_value
        self.window_SHGC_value = window_SHGC_value

    # getter function of window_U_value
    def set_window_U_value(self, window_U_value):
        if type(window_U_value) == str:
            window_U_value = float(window_U_value)
        if window_U_value < 0.25 or window_U_value > 0.75:
            print('Invalid window U value:', window_U_value)
        else:
            self.window_U_value = window_U_value

    # setter function of window_U_value
    def get_window_U_value(self):
        return self.window_U_value

    # getter function of window_SHGC_value
    def set_window_SHGC_value(self, window_SHGC_value):
        if type(window_SHGC_value) == str:
            window_SHGC_value = float(window_SHGC_value)
        if window_SHGC_value < 1.0 or window_SHGC_value > 2.5:
            print('Invalid window SHGC value:', window_SHGC_value)
        else:
            self.window_SHGC_value = window_SHGC_value

    # setter function of window_SHGC_value
    def get_window_SHGC_value(self):
        return self.window_SHGC_value

    def simulate(self):
        print('Parameter values with highest average indoor air temperature:',
              (self.window_U_value ** 1.2, (self.window_SHGC_value - 1) ** 2 + 1.2))
    