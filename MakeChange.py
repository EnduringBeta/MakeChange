# Make Change
# Ross' first significant Python excursion
# 14 April 2014
#
# This program takes in a monetary value and
# calculates the number of ways that value can
# be reached through coinage and paper bills.
#
# The values for denominations can be changed.
# I plan to include a parameter for default currencies.
# (US Dollar, Pound, Euro, Yuan, Yen)
#
# Currently output through print statements?

from enum import Enum
from itertools import count

def MakeChange(total, denomStr):

    USDollarDenoms = [0.01, 0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00]

    class denomType(Enum):
        Coin = 0
        Bill = 1

    class Denomination:
        
        def __init__(self, Worth, NumUsed, Name, Type):
            self.Worth   = Worth
            self.NumUsed = NumUsed
            self.Name    = Name
            self.Type    = Type
        
        Worth = 0
        NumUsed = 0
        Name = ""
        Type = denomType.Coin

    print("Starting to make change for ${0}...".format(total))

    Denominations = list()
    if "US Dollar" in denomStr:
        for n in USDollarDenoms:
            Denominations.append(Denomination(n, 0, "", denomType.Coin)) # Shouldn't be like this.
            

    numMethods = 0

# Recursion might be best? Split amount into largest few, then break down each one of those items, and so on.
# Number of breaks... multiplied together equals ways to make change?

    done = False
    while not done:
        print("Done for now.")
        done = True


# Program execution
MakeChange(1.05, "US Dollar")
