#Taxation Problem

#Level 1: Basic Input and Salary Calculation
Emp_name = input("Enter your name:")
Emp_ID = int(input("Enter your employee ID: "))
Basic_salary = int(input("Enter your monthly salary (Rs): "))
Special_allowances = int(input("Enter monthly special aloowences (Rs): "))
bonus_percentage = int(input("Enter your bonus percentage (%): ")) # Annual Bonus as % of Gross Salary

Gross_monthly_salary = Basic_salary + Special_allowances
Bonus = (Gross_monthly_salary * 12) * (bonus_percentage / 100)
Annual_gross_salary = (Gross_monthly_salary * 12) + Bonus

print("Employee Name        :", Emp_ID)
print("Employee ID          :", Emp_ID)
print("Gross Monthly Salary : Rs {}".format(Gross_monthly_salary))
print("Annual Gross Salary  : Rs {}".format(Annual_gross_salary))

#Level 2: Taxable Income Calculation
standard_deduction = 50000
taxable_income = Annual_gross_salary - standard_deduction
print("Annual Gross Salary  : Rs {}".format(Annual_gross_salary))
print("Standard deduction amount is:",standard_deduction)
print("Taxable income is:",taxable_income)


#Level 3: Tax and Rebate Calculation
tax=0
if 0 <= taxable_income <= 300000:
    tax=0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = (300000 * 0.05) + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30

# Rebate
if taxable_income <= 700000:
    tax = 0
# Cess
cess = tax * 0.04
total_tax = tax + cess

print("Tax Before Cess: Rs {:.2f}".format(tax))
print("Health & Edu Cess 4%: Rs {:.2f}".format(cess))
print("Final Tax Payable: Rs {:.2f}".format(total_tax))

# Level 4: Net Salary Calculation
net_salary = Annual_gross_salary - total_tax
print("Annual Gross Salary: Rs {:.2f}".format(Annual_gross_salary))
print("Total Tax Payable: Rs {:.2f}".format(total_tax))
print("Annual Net Salary: Rs {:.2f}".format(net_salary))

#Level 5: Report Generation
print("   EMPLOYEE SALARY & TAX REPORT   ")
print(f"Employee Name: {Emp_name}")
print(f"Employee ID: {Emp_ID}")
print(f"Gross Monthly Salary: Rs {Gross_monthly_salary:,.2f}")
print(f"Annual Bonus ({bonus_percentage}%): Rs {Bonus:,.2f}")
print(f"Annual Gross Salary: Rs {Annual_gross_salary:,.2f}")
print(f"Standard Deduction: Rs {standard_deduction:,.2f}")
print(f"Taxable Income: Rs {taxable_income:,.2f}")
print(f"Tax Before Cess: Rs {tax:,.2f}")
print(f"Health & Edu Cess (4%): Rs {cess:,.2f}")
print(f"Total Tax Payable: Rs {total_tax:,.2f}")
print(f"Annual Net Salary: Rs {net_salary:,.2f}")
 
#Level 6: Input Validation Rules
