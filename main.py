name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

annual_income = 0
for month in range(12):
    print('{} {}:'.format('What is your income for', name_month[month], end=''))
    income = float(input())
    annual_income += income
print('Your annual income is', annual_income, '$')
tax_deduction = float(input('What is your tax deduction? '))
an_income = annual_income - tax_deduction
status=int(input('If you are single, enter 1. If you have a spouse, enter 2. If you have children but no spouse, enter 3.'))

if status==1 :
    a=9075
    b=36900
    c=89350
    d=186350
    e=405100
    f=406750
elif status==2 :
    a = 9075*2
    b = 36900*2
    c = 148850
    d = 226850
    e = 405100
    f = 457600
elif status==3 :
    a = 12950
    b = 49400
    c = 127550
    d = 20660
    e = 405100
    f = 432200
