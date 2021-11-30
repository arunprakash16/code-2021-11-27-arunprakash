
def ht_cm_sqm(ht):
    """Converts height from centimeter to squared meter

    Parameters
    ----------
    ht: double
        height in cms

    Returns
    -------
    double
        height in squared meter.

    Examples
    --------
    >>> ht_cm_sqm(175)
    1.75
    """

    return (ht / 100) ** 2


def wt_lb_kg(wt):
    """Converts height from centimeter to squared meter

    Parameters
    ----------
    wt: double
        weight in pound

    Returns
    -------
    double
        weight in kilogram.

    Examples
    --------
    >>> wt_lb_kg(200)
    90.8
    """

    return wt * 0.454


def bmi_calculator(ht, wt, ht_unit='cms', wt_unit='kg'):
    """Calculates BMI

    Before calculating bmi height will be converted to squared meter and weight to kilograms depending

    Parameters
    ----------
    ht: double
    wt: double
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

    Returns
    -------
    int, double
        int value to represent function successfulness
            0 - success
            1 - failure due to unit value not supported
        bmi value.

    Examples
    --------
    >>> bmi_calculator(3.0625, 75, 'sqm', 'kg')
    0, 24.49

    """

    if ht_unit not in ['cms', 'sqm'] or wt_unit not in ['kg', 'lb']:
        return 1, 0

    ht_sqm = ht

    if ht_unit == 'cms':
        ht_sqm = ht_cm_sqm(ht)

    wt_kg = wt

    if wt_unit == 'lb':
        wt_kg = wt_lb_kg(wt)

    return 0, (wt_kg / ht_sqm)
