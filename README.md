# pybmi

Calculate BMI based on height and weight and analyze riskcategory

## Installation

```bash
$ pip install pybmi
```

## Usage

`pybmi` can be used to calculate bmi and identify bmi category and health risk associated to the bmi and provide the count of people in specific category as follows:
from pybmi.pybmi import bmi_analysis
out_stat, bmi_agg = bmi_analysis('/path/input_file.txt')
if out_stat == 0:
    for bmi, bmi_cnt in bmi_agg.items():
        print (bmi + ' : ' + str(bmi_cnt))


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pybmi` was created by Arun Prakash J. It is licensed under the terms of the MIT license.

## Credits

`pybmi` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
