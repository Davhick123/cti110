# David Hicks
# This program calculates an employee's salary, including regular and overtime pay.

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

regular_hours = 40
overtime_multiplier = 1.5
overtime_rate = overtime_multiplier * pay_rate

overtime_hours = max(0, hours_worked - regular_hours)
regular_hours_worked = min(hours_worked, regular_hours)

regular_pay = regular_hours_worked * pay_rate
overtime_pay = overtime_hours * overtime_rate
gross_pay = regular_pay + overtime_pay

print("----------------------------------")
print(f"Employee name: {employee_name}")
print("----------------------------------")
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("-" * 75)
print(f"{hours_worked:<15.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<10.2f}")
  