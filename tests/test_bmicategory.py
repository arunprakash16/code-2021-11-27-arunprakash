from pybmi.bmicategory import BmiCategory

bmi_analysis = BmiCategory()

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(4.5)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Underweight', 'Malnutrition risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(18.4)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Underweight', 'Malnutrition risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(18.4)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Underweight', 'Malnutrition risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(18.5)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Normal weight', 'Low risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(24.9)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Normal weight', 'Low risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(25.6)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Overweight', 'Enhanced risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(29.9)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Overweight', 'Enhanced risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(30)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Moderately obese', 'Medium risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(34.9)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Moderately obese', 'Medium risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(35)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Severely obese', 'High risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(39.9)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Severely obese', 'High risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(40)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Very Severely obese', 'Very High risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(70)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Very Severely obese', 'Very High risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(999.9)
assert out_stat == 0, "Output status doesn't match the expectation"
assert bmi_val == ('Very Severely obese', 'Very High risk'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(-1)
assert out_stat == 1, "Output status doesn't match the expectation"
assert bmi_val == ('Couldn't fetch health category for - -1', 'Couldn't fetch health category for - -1'), "Incorrect bmi category / health risk!"

out_stat, bmi_val = bmi_analysis.get_bmi_cat_risk(1000.1)
assert out_stat == 1, "Output status doesn't match the expectation"
assert bmi_val == ('Couldn't fetch health category for - 1000.1', 'Couldn't fetch health category for - 1000.1'), "Incorrect bmi category / health risk!"
