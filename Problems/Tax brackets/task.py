income = int(input())
tax = ''

if income < 15527:
    tax = 0
elif 15528 < income < 42707:
    tax = 15
elif 42708 < income < 85414:
    tax = 22
elif 85415 < income < 132406:
    tax = 26
else:
    tax = 28

tax_value = income * (tax / 100)
print("The tax for {} is {}%. That is {:.2f} dollars!".format(income, tax, tax_value))
