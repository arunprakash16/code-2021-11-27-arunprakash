import pathlib
import pandas as pd
import json


import bmi
import bmicategory


def load_data(input_file, read_count):
    """Reads the file chunk based on the read_count and loads the data into a dataframe and return it
    Parameters
    ----------
    input_file: json file name with path
    read_count: int
        data chunk cap

    Returns
    -------
    dataframe
        input file chunk loaded in dataframe
    """
    input_file_data = list()
    counter = 0
    with open(input_file, 'r') as inp_file:
        for line in inp_file:
            line = line.strip(',\n').strip('[').strip(']')
            input_file_data.append(json.loads(line.strip('\n')))
            counter += 1
            if counter == read_count:
                df = pd.DataFrame.from_dict(input_file_data, orient='columns')
                yield df
                counter = 0
                input_file_data.clear()


def add_bmi_health_stat(ht, wt, ht_unit, wt_unit, count_cat):
    """Gets bmi value for each height & weight series element and fetches the bmi category and health risk"""
    bmi_health = dict()
    bmi_stat = dict()
    bmi_cat_risk = bmicategory.BmiCategory()
    for ind, height in ht.items():
        bmi_value = bmi.bmi_calculator(height, wt.at[ind], ht_unit, wt_unit)[1]
        health_check_stat, bmi_cat, health_risk = bmi_cat_risk.get_bmi_cat_risk(round(bmi_value, 1))
        if health_check_stat != 0:
            print('Has issue in getting health category & risk for height: {}, weight: {}, bmi: {}'.format(height,
                                                                                                           wt.at[ind],
                                                                                                           bmi))
        elif bmi_cat in count_cat:
            for cat in count_cat:
                bmi_stat[cat] = bmi_stat.get(cat, 0) + 1

        bmi_health[ind] = {'bmi': bmi_value, 'bmi_category': bmi_cat, 'health_risk': health_risk}

    return bmi_stat, pd.DataFrame.from_dict(bmi_health, orient='index')


def bmi_analysis(input_file, ht_unit='cms', wt_unit='kg', count_cat=['Overweight']):
    """Performs bmi analysis
    Reads from input json (list of dict format) data and calculates bmi and health category and risk
    returns total number of people in provided category(s)

    Parameters
    ----------
    input_file: list of dict / json file
    ht_unit: str
        incoming height units - to convert height value into squared meter
        supported units
        ---------------
            cms = centimeters
            sqm = squared meter
    wt_unit: str
        incoming weight units - to convert them into kilogram if its not
        supported units
        ---------------
            kg = kilogram
            lb = pound
    count_cat: list
        one or more categories for which the function has to return number of people in the specified category

    Returns
    -------
    int, dict
        int value to represent function successfulness
            0 - success
            1 - failure due to unit value not supported
        dictionary containing count of provided bmi categories.
    """

    file = pathlib.Path(input_file)

    if file.exists():
        proceed = True
    else:
        proceed = False
        print('{} file does not exist'.format(input_file))

    if proceed:
        file_data = load_data(input_file, 30)
        data_df = list()
        bmi_stat_out = dict()
        while True:
            try:
                input_df = next(file_data)
                ht = input_df['HeightCm']
                wt = input_df['WeightKg']
                temp_bmi_stat, bmi_cat_risk = add_bmi_health_stat(ht, wt, ht_unit, wt_unit, count_cat)

                for key_val, key_count in temp_bmi_stat.items():
                    bmi_stat_out[key_val] = bmi_stat_out.get(key_val, 0) + key_count

                bmi_out = pd.merge(input_df, bmi_cat_risk, left_index=True, right_index=True)
                data_df.append(bmi_out)
            except StopIteration as e:
                print('Completed iterating over the input file' + str(e))
                return 0, bmi_stat_out
    else:
        return 1, {}

