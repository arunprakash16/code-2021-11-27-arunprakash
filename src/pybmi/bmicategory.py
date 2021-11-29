import pandas as pd


class PyBmiCategory:
    """PyBmiCategory class - acts as an interface to fetch health category & risk for the passed on bmi value"""

    def __init__(self):
        """Initialize bmi category and risk data as dataframe"""

        bmi_category_risk = [{"category": "Underweight", "bmi_min_range": 0.0, "bmi_max_range": 18.4,
                              "health_risk": "Malnutrition risk"},
                             {"category": "Normal weight", "bmi_min_range": 18.5, "bmi_max_range": 24.9,
                              "health_risk": "Low risk"},
                             {"category": "Overweight", "bmi_min_range": 25, "bmi_max_range": 29.9,
                              "health_risk": "Enhanced risk"},
                             {"category": "Moderately Obese", "bmi_min_range": 30, "bmi_max_range": 34.9,
                              "health_risk": "Medium risk"},
                             {"category": "Severely Obese", "bmi_min_range": 35, "bmi_max_range": 39.9,
                              "health_risk": "High risk"},
                             {"category": "Very Severely Obese", "bmi_min_range": 40, "bmi_max_range": 999.9,
                              "health_risk": "Very High risk"}]

        self.bmi_cat_risk_df = pd.DataFrame.from_dict(bmi_category_risk, orient='columns')

    def get_bmi_cat_risk(self, bmi_value):
        """Provides health category and risk based on provided BMI value

        Parameters
        ----------
        self: onject of PyBmiCategory
        bmi_value: double
            Provided bmi value

        Returns
        -------
        int, str, str
            int value to represent function successfullness
                0 - success
                1 - failure due to unit value not supported
            first string value provides health category
            second string value provides health risk

        Examples
        --------
        >>> get_bmi_cat_risk(24.489795918367346)
        0, "Normal weight", "Low risk"

        """

        # global bmi_category_risk
        # bmi_cat_risk_df = pd.DataFrame.from_dict(bmi_category_risk, orient='columns')
        bmi_value_out = self.bmi_cat_risk_df[(self.bmi_cat_risk_df['bmi_min_range'] <= bmi_value)
                                             & (self.bmi_cat_risk_df['bmi_max_range'] >= bmi_value)]
        if bmi_value_out.count()[0] > 0:
            return 0, \
                   bmi_value_out['category'].values[0], \
                   bmi_value_out['health_risk'].values[0]
        else:
            return 1, \
                   "Couldn't fetch health category for - " + str(bmi_value), \
                   "Couldn't fetch health risk for - " + str(bmi_value)
