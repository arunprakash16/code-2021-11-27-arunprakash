from pybmi import pybmi

out_stat, bmi_agg = bmi_analysis('c:/test/input_file.txt')
if out_stat == 0:
    for bmi, bmi_cnt in bmi_agg.items():
        print (bmi + ' : ' + str(bmi_cnt))