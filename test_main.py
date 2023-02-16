from parametric_simulation import run_two_parameter_parametric
from Energy_Plus import EnergyPlus
import csv

eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'

energyPlus = EnergyPlus()
# set two parameters
window_U_key = ['WindowMaterial:SimpleGlazingSystem',
                'SimpleWindow:DOUBLE PANE WINDOW',
                'solar_heat_gain_coefficient']

window_U_vals = [i / 100 for i in range(25, 75, 20)]
energyPlus.set_window_U_key(window_U_key)
energyPlus.set_window_U_value(window_U_vals)

window_SHGC_key = ['WindowMaterial:SimpleGlazingSystem',
                   'SimpleWindow:DOUBLE PANE WINDOW',
                   'u_factor']

window_SHGC_vals = [i / 10 for i in range(10, 25, 5)]
energyPlus.set_window_SHGC_key(window_SHGC_key)
energyPlus.set_window_SHGC_value(window_SHGC_vals)

output_dir = 'output'
# execute simulation
output_paths = run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                                            energyPlus.get_window_U_key(),
                                                            energyPlus.get_window_U_value(),
                                                            energyPlus.get_window_SHGC_key(),
                                                            energyPlus.get_window_SHGC_value())

max_mean_temperature = 0.0
max_val_of_parameter = ''

for val_of_parameter in output_paths.keys():
    file = open('./' + output_paths[val_of_parameter], 'r')
    csv_reader = csv.reader(file)

    temperature_of_different_hour = []
    index = 0
    for line in csv_reader:
        if index > 0:
            temperature_of_different_hour.append(float(line[8]))
        index += 1

    # calculate the mean value
    mean_temperature = 0.0 if len(temperature_of_different_hour) == 0 \
        else sum(temperature_of_different_hour) / len(temperature_of_different_hour)

    if mean_temperature > max_mean_temperature:
        max_mean_temperature = mean_temperature
        max_val_of_parameter = val_of_parameter


two_param_val = val_of_parameter.split('-')
print('Window U optimal parameter val: ', two_param_val[0])
print('Window SHGC optimal parameter val: ', two_param_val[1])
