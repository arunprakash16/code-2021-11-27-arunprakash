from pybmi.pybmi import bmi_analysis


out_stat, bmi_agg = bmi_analysis('c:/test/input_file.txt')
assert bmi_agg == {'Overweight': 1}, "BMI calculation incorrect!"
