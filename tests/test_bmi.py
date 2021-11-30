from pybmi.bmi import bmi_calculator

out_stat, bmi_val = bmi_calculator(171, 75)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == 25.64891761567662, "Incorrect BMI value!"

out_stat, bmi_val = bmi_calculator(2.9241, 75, ht_unit='sqm')
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == 25.64891761567662, "Incorrect BMI value!"

out_stat, bmi_val = bmi_calculator(171, 150, wt_unit='lb')
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == 23.26527820525974, "Incorrect BMI value!"

out_stat, bmi_val = bmi_calculator(1.71, 75, ht_unit='m')
assert out_stat == 1, "Output status doesn't match the expectation"
assert bmi_val == 0, "Incorrect BMI value!"

out_stat, bmi_val = bmi_calculator(171, 75, wt_unit='oz')
assert out_stat == 1, "Output status doesn't match the expectation"
assert bmi_val == 0, "Incorrect BMI value!"
