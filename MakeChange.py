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

# TODO: Figure out how to do multiple denominations of same value

from enum import Enum
from itertools import count

def MakeChange(total, denomStr):
    """Calculate the number of ways change can be made from the given amount for the given currency string"""
    
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

# ---------------------------------------------------------------------------------------

    def LoadUSCurrency():
        denom = list()
        
        denom.append(Denomination(0.01,   0, "penny",                   denomType.Coin));
        denom.append(Denomination(0.05,   0, "nickel",                  denomType.Coin));
        denom.append(Denomination(0.10,   0, "dime",                    denomType.Coin));
        denom.append(Denomination(0.25,   0, "quarter",                 denomType.Coin));
        denom.append(Denomination(0.50,   0, "half dollar",             denomType.Coin));
        denom.append(Denomination(1.00,   0, "dollar coin",             denomType.Coin));
        denom.append(Denomination(1.00,   0, "one dollar bill",         denomType.Bill));
        denom.append(Denomination(2.00,   0, "two dollar bill",         denomType.Bill));
        denom.append(Denomination(5.00,   0, "five dollar bill",        denomType.Bill));
        denom.append(Denomination(10.00,  0, "ten dollar bill",         denomType.Bill));
        denom.append(Denomination(20.00,  0, "twenty dollar bill",      denomType.Bill));
        denom.append(Denomination(50.00,  0, "fifty dollar bill",       denomType.Bill));
        denom.append(Denomination(100.00, 0, "one-hundred dollar bill", denomType.Bill));
        
        return denom

# ---------------------------------------------------------------------------------------

    def GetSmallest(denoms):
        smallestDenom = denoms[0].Worth
        for denom in denoms:
            if denom.Worth < smallestDenom:
                smallestDenom = denom.Worth
        
        return smallestDenom

# ---------------------------------------------------------------------------------------

    def GetLargest(denoms):
        largestDenom = denoms[-1].Worth
        for denom in denoms:
            if denom.Worth > largestDenom:
                largestDenom = denom.Worth
        
        return largestDenom

# ---------------------------------------------------------------------------------------

    # Will need to track coin combination of each
    # Advanced form will remember calculated amounts to speed up later
    
    #def FindCombos(remAmt, denoms):
    def FindCombos(remAmt):

        def PrintCombo():
            for denom in Denominations:
                print("{0} (1), ".format(denom.NumUsed, denom.Name))
        
        # Terminating condition
        if remAmt <= GetSmallest(Denominations):
            #PrintCombo()
            return 1
        
        totalCombos = 0
        changeRemains = True
        prevDenom = GetLargest(Denominations)

        while changeRemains:
            # Find next denomination step for current change combination
            highestDenom = 0.00
            for denom in Denominations:
                # If denomination is greater than current highest but less than remaining amount
                # ...and is less than the denomination of the previous loop
                print("{0} <= {1} <= {2} and {3} < {4}?\r\n".format(highestDenom, denom.Worth, remAmt, denom.Worth, prevDenom))
                if highestDenom <= denom.Worth <= remAmt and denom.Worth < prevDenom:
                    highestDenom = denom.Worth

            # If no denomination fit, done
            if highestDenom == GetSmallest(Denominations):
                changeRemains = False
            
            # Continue recursion with new amount, lowered by the denomination
            totalCombos += FindCombos(remAmt-highestDenom)
            prevDenom = highestDenom
        
        return totalCombos

# ---------------------------------------------------------------------------------------

    print("Starting to make change for {0} {1}...".format(total, denomStr))
    
    # TODO: More currencies
    if   "US Dollar" in denomStr:
        Denominations = LoadUSCurrency()
    elif "CAD"       in denomStr:
        print("Not implemented yet! Use \"US Dollar\".\r\n")
        return
    elif "Pound"     in denomStr:
        print("Not implemented yet! Use \"US Dollar\".\r\n")
        return
    elif "Euro"      in denomStr:
        print("Not implemented yet! Use \"US Dollar\".\r\n")
        return
    elif "Yen"       in denomStr:
        print("Not implemented yet! Use \"US Dollar\".\r\n")
        return
    elif "Yuan"      in denomStr:
        print("Not implemented yet! Use \"US Dollar\".\r\n")
        return
    elif "Bitcoin"   in denomStr:
        print("Very funny\r\n")
    else:
        print("Unknown currency\r\n")
        return
    
    # TODO: Improve rounding input amount to lowest denomination
    total = round(total / GetSmallest(Denominations)) * GetSmallest(Denominations)
    
    numMethods = FindCombos(total)
    
    
    
    return numMethods

# -------------------------------------------------------------

# Program execution
MakeChange(16.21, "CAD")
MakeChange(1.05, "US Dollar")
