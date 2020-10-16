import argparse
import json
# TEST CASES:
# 1) Different configurations for federal tax
# 2) Multiple happy paths (IE, section 1, section 2, section 3, up to section other)
# 3) Verbose is indeed verbose.
def calculate(percentages, bracket, income):
    """
    Calculate total tax given income and a configuration of percentages, and bracket

    percentages: A Python list that represents the amount of percent tax to be
    deducted on a specific tax bracket
    bracket: A Python list representing the specific cut off point of a tax
    bracket number.
    income: An integer representing the income. 

    Returns a list of taxed values.
    """
    
    counter = 0
    tax = []
    for i,e in enumerate(bracket):
        # Keep iterating until we are over the last bracket
        if income > e:
            income -= e
            tax.append(e * percentages[i])
        else:
            # Early termination because we are in between brackets
            tax.append(income * percentages[i])
            return tax
    # We've extended beyond all brackets, so calculate the remaining bracket.
    tax.append(percentages[-1] * income)
    return tax

def extended_output(percentages, bracket, tax_amount, income):
    """
    Calculate a formatted string to report back.

    percentages: A Python list that represents the amount of percent tax to be
    deducted on a specific tax bracket
    bracket: A Python list representing the specific cut off point of a tax
    bracket number.
    income: An integer representing the income. 
    
    Returns a prettier string of calculations.
    """
    answer = ""
    current_total = 0
    for i,e in enumerate(tax_amount):
        # If the income extends beyond the last bracket, append properly.
        if i == len(tax_amount) - 1:
            answer += f"Income up to ${income:,.2f} taxed at {percentages[i]*100:.2f}%: ${tax_amount[i]:>10,.2f}\n"
        else:
            current_total += bracket[i]
            answer += f"Income up to ${current_total:,.2f} taxed at {percentages[i]*100:.2f}%: ${tax_amount[i]:>10,.2f}\n"

    
    answer += f"\nYou paid ${sum(tax_amount):,.2f} in taxes, for a net income in ${income-sum(tax_amount):,.2f}"
    return answer

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Calculate federal tax from your gross annual income rounded to the nearest dollar.")
    parser.add_argument('income', metavar='I', type=int, help='An integer as your gross annual income.')
    parser.add_argument('--verbose', action='store_true', help='Print more information about your income tax.' )
    
    args = parser.parse_args()
    tax_values = None
    income = args.income

    with open('config.json', 'r') as config:
        tax_values = json.load(config)

    # Parse the JSON object to lists for better processing.
    percentages = []
    brackets = []

    # Note that by the configuration of json file, we len(percentages) + 1 == len(income) 
    for i in tax_values:
        if i == 'other':
            percentages.append(tax_values[i])
        else:
            percentages.append(tax_values[i][1])
            brackets.append(tax_values[i][0])
    tax_amount = calculate(percentages, brackets, income)

    if args.verbose:
        print(extended_output(percentages, brackets, tax_amount, income))
    else:
        print("You paid ${:,.2f} in taxes, for a net income in ${:,.2f}".format(sum(tax_amount), income-sum(tax_amount)))
