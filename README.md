## Calculate Tax
Here's an application that will calculate how much of federal tax you owe based on a gross income

### Getting started
To quickly run this command, do `python3 calculate_tax.py <income>` where income is the amount you want to calculate on.

For example:
`python3 calculate_tax.py 50000`

### Command line arguments
`income`: The amount of gross income that you want to calcuate on.

`--verbose`: To gain a more detailed report of how much you owe.

For more information, check out `python3 calculate_tax.py --help`

### Testing
We use `pytest` to test this program. Ensure you have pytest installed before running this.

The tests are located in `test_calculate_tax.py`. To run tests, run `pytest` or `pytest test_calculate_tax.py`
