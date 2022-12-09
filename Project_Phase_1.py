print('Edna Brodnax-Hunter')
print('CIS261')
print('Phase 1')

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

#write the GetHoursWorked function

def GetHoursWorked():
    hrsWrkd = float(input("Enter hours worked: "))
    return hrsWrkd

#write the GetHourlyRate function

def GetHourlyRate():
    hrlyRate = float(input("Enter hourly rate: "))
    return hrlyRate

# write the GetTaxRate function

def GetTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    return taxRate


def CalcTaxAndNetPay(hrsWrkd, hrlyRate, taxRate):
    grosspay = hrsWrkd * hrlyRate
    incometax = grosspay * taxRate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empName, hrsWrkd, hrlyRate, grosspay, taxRate, incometax, netpay):
    print(empName, f"{hrsWrkd:,.2f}",  f"{hrlyRate:,.2f}", f"{grosspay:,.2f}",  f"{taxRate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    # write the code to print TotHours, TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Total number of hours: {TotHours}.2.f")
    print(f"Total gross pay: {TotGrossPay},.2f")
    print(f"Total tax: {TotTax},.2f")
    print(f"Total net pay: {TotNetPay},.2f")

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empName = GetEmpName()
        if empName.upper() == "END":
            break
        # write the code to assign to hours the return value from GetHoursWorked
        hrsWrkd = GetHoursWorked()  # Swapped the order of variable and function call
        TotHours += hrsWrkd
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        hrlyRate = GetHourlyRate()  # Swapped the order of variable and function call
        # write the code to assign to taxrate the return value from GetTaxRate
        taxRate = GetTaxRate()      # Swapped the order of variable and function call
        grosspay, incometax, netpay = CalcTaxAndNetPay(hrsWrkd, hrlyRate, taxRate)
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        printinfo(empName, hrsWrkd, hrlyRate, grosspay, taxRate, incometax, netpay)
        TotEmployees += 1
        # write the code to increment the other total variables with the appropriate values

    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)





















































