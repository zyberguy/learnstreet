# This def calculates the tax according to the given tax-structure and returns the tax
def calculate_tax(inc):
    inc = int(inc)
    tax = 0.0
    if inc > 40000:
        print inc
        tax += (float(30)/float(100)) * (inc-40000)
        inc = 40000
    if inc > 20000:
        tax += (float(20)/float(100)) * (inc-20000)
        inc = 20000
    if inc > 10000:
        tax += (float(10)/float(100)) * (inc-10000)
        inc = 10000
    return tax
    

# This def reads a series of incomes from comma separated values in the string text and then formats the income and tax in a table and returns the string
def income_list(text):
    result =[]    
    incomes = text.split(",")
    taxes = []
    for i in range(0, len(incomes)):
        taxes.append(calculate_tax(incomes[i]))
        result.append(incomes[i] +"-"+ str(taxes[i]))
    return result