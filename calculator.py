# ID: reachvidu@gmail.com; pass: Vidu@1234
import json
import numpy

'''
Calculator functions
'''

# Fixed Deposit Calculator
def FD(one,two,three):        # Principal amount, rate of interest, tenure in months
    annual_interest = (one*two)/100
    monthly_interest = annual_interest/12
    total_interest = monthly_interest*three
    total_receivable = one+total_interest
    monthly_interest = float("{0:.2f}".format(monthly_interest))
    total_interest = float("{0:.2f}".format(total_interest))
    total_receivable = float("{0:.2f}".format(total_receivable))
    return ("Monthly interest is " + str(monthly_interest) + " ,total interest is " + str(total_interest) + " and total receivable is " + str(total_receivable))


# Compound Interest Calculator
def CI(one,two,three):		# Principal amount, rate of interest, tenure in months
    interest = 0;
    interest = interest + (one*two)/100
    interest = float("{0:.2f}".format(interest))
    return ("The net compound interest is " + str(interest))


# EMI Calculator
def EMI(one,two,three):		#Principal amount, rate of interest, tenure in months
    r = (two/12)/100
    Numerator = one*r*((1+r)**three)
    Denominator = ((1+r)**three - 1)
    E = Numerator/Denominator
    E = float("{0:.2f}".format(E))
    return 'The EMI is ' + str(E);
