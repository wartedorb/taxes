'''

Case-study #2 TAXES
Developers:
Bikmetov Ed. (40%) Bychkov K. (40%) Kondrashov M. (40%)

'''

# Cycle counting an annual income.

name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

annual_income = 0
for month in range(12):
    print('{} {}:'.format('What is your income for', name_month[month], end=''))
    income = float(input())
    annual_income += income
print('Your annual income is', annual_income, '$')

# Tax deduction
tax_deduction = float(input('What is your tax deduction? '))

# Income for tax counting
an_income = annual_income - tax_deduction

# Status of a person
status = int(input('If you are single, enter 1. If you have a spouse, enter 2. If you have children but no spouse, enter 3. '))

# Income measures for different statuses
if status == 1:
    a = 9075
    b = 36900
    c = 89350
    d = 186350
    e = 405100
    f = 406750
elif status == 2:
    a = 18150
    b = 73800
    c = 148850
    d = 226850
    e = 405100
    f = 457600
elif status == 3:
    a = 12950
    b = 49400
    c = 127550
    d = 206600
    e = 405100
    f = 432200

# Tax counter
if 0 <= an_income <= a:
    N1 = 0.1*an_income
    n=N1
elif a < an_income <= b:
    N1 = (an_income-a)
    n = a*0.10 + 0.15*N1
elif b < an_income <= c:
    N1 = (an_income-b)
    n = a*0.10+((b-a)*0.15)+N1*0.25
elif c < an_income <= d:
    N1 = an_income - c
    n = a*0.10+((b-a)*0.15)+(c-b)*0.25+N1*0.28
elif d < an_income <= e:
    N1 = an_income - d
    n = a*0.10+((b-a)*0.15)+(c-b)*0.25+(d-c)*0.28+N1*0.33
elif e < an_income <= f:
    N1 = an_income - e
    n = a*0.10+((b-a)*0.15)+(c-b)*0.25+(d-c)*0.28+(e-d)*0.33+N1*0.35
elif f < an_income:
    N1 = an_income - f
    n = a*0.10+((b-a)*0.15)+(c-b)*0.25+(d-c)*0.28+(e-d)*0.33+(f-e)*0.35+N1*0.396

# Total tax

print(n)
