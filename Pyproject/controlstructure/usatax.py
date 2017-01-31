
fedtax= .1
statetax = {"CA":.1, "MA" : .15}
def tax_calculate(income,state):
        return (income * (1-fedtax + statetax[state]))


caincome = tax_calculate(1000,"CA")
print(caincome)
maincome = tax_calculate(1000,"MA")
print(maincome)
