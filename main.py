master
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
status=input('If you are single, enter 1. If you have a spouse, enter 2. If you have children but no spouse, enter 3.')
if status==1:

if status==2:

if status==3:



Ed
