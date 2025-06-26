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

print("\n------ Salary Details ------")
print("Employee Name        :", Emp_ID)
print("Employee ID          :", Emp_ID)
print("Gross Monthly Salary : Rs {}".format(Gross_monthly_salary))
print("Annual Gross Salary  : Rs {}".format(Annual_gross_salary))

#Level 2: Taxable Income Calculation
standard_deduction = 50000
taxable__income = Annual_gross_salary - standard_deduction
print("Annual Gross Salary  : Rs {}".format(Annual_gross_salary))
print("Standard deduction amount is:",standard_deduction)
print("Taxable income is:",taxable__income)


#Level 3: Tax and Rebate Calculation
