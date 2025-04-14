# David Hicks
# 4/13/2025
#  P4HW2_HicksDavid.py
# This program calculates pay including overtime for multiple employees
# and stops when the user enters "Done" as the employee name.

def main():
    total_employees = 0
    total_overtime_pay = 0.0
    total_regular_pay = 0.0
    total_gross_pay = 0.0

    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

    while employee_name != "Done":
        hours_worked = float(input("How many hours did " + employee_name + " work? "))
        pay_rate = float(input("What is " + employee_name + "'s pay rate? "))

        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            regular_hours = 40
        else:
            overtime_hours = 0
            regular_hours = hours_worked

        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = regular_hours * pay_rate
        gross_pay = overtime_pay + regular_pay

        # Totals
        total_employees = total_employees + 1
        total_overtime_pay = total_overtime_pay + overtime_pay
        total_regular_pay = total_regular_pay + regular_pay
        total_gross_pay = total_gross_pay + gross_pay

        # Print employee results
        print("\nEmployee name:   " + employee_name)
        print("")
        print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
        print("-------------------------------------------------------------------------")
        print("   " + str(hours_worked) + "        " + str(pay_rate) + "      " + str(overtime_hours) +
              "         " + str(round(overtime_pay, 2)) + "         " + str(round(regular_pay, 2)) +
              "       " + str(round(gross_pay, 2)))
        print("")

        # Ask for next employee
        employee_name = input('Enter employee\'s name or "Done" to terminate: ')

    # Final totals
    print("")
    print("Total number of employees entered: " + str(total_employees))
    print("Total amount paid for overtime: $" + str(round(total_overtime_pay, 2)))
    print("Total amount paid for regular hours: $" + str(round(total_regular_pay, 2)))
    print("Total amount paid in gross: $" + str(round(total_gross_pay, 2)))

# Run the program
main()