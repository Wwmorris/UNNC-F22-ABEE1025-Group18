class EnergyPlus(object):
    # construction method
    def __init__(self):
        self.window_U_values = []
        self.window_SHGC_values = []
        self.window_U_key = []
        self.window_SHGC_key = []

    # getter function of window_U_value
    def set_window_U_value(self, window_U_values):
        for window_U_value in window_U_values:
            if type(window_U_value) == str:
                window_U_value = float(window_U_value)
            if window_U_value < 0.25 or window_U_value > 0.75:
                print('Invalid window U value:', window_U_value)
            else:
                self.window_U_values.append(window_U_value)

    # setter function of window_U_value
    def get_window_U_value(self):
        return self.window_U_values

    # getter function of window_SHGC_value
    def set_window_SHGC_value(self, window_SHGC_values):
        for window_SHGC_value in window_SHGC_values:
            if type(window_SHGC_value) == str:
                window_SHGC_value = float(window_SHGC_value)
            if window_SHGC_value < 1.0 or window_SHGC_value > 2.5:
                print('Invalid window SHGC value:', window_SHGC_value)
            else:
                self.window_SHGC_values.append(window_SHGC_value)

    # setter function of window_SHGC_value
    def get_window_SHGC_value(self):
        return self.window_SHGC_values

    # set key of window_U
    def set_window_U_key(self, window_U_key):
        self.window_U_key = window_U_key

    # set key of window_SHGC
    def set_window_SHGC_key(self, widow_SHGC_key):
        self.window_SHGC_key = widow_SHGC_key

    # get key of window_U
    def get_window_U_key(self):
        return self.window_U_key

    # get key of window_SHGC
    def get_window_SHGC_key(self):
        return self.window_SHGC_key