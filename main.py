# Cycle counting an annual income.
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

annual_income = 0
for month in range(12):
    print('{} {}:'.format('What is your income for', name_month[month], end=''))
    income = float(input())
    annual_income += income
print('Your annual income is', annual_income, '$')
tax_deduction = float(input('What is your tax deduction? '))
an_income = annual_income - tax_deduction
print('1')


