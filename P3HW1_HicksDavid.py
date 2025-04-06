Hicks

# This program takes a number grade, determines the average, and displays the letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Determine letter grade for the average
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("------------Results------------")
print(f"Lowest Grade: {low:.1f}")
print(f"Highest Grade: {high:.1f}")
print(f"Sum of Grades: {total:.1f}")
print(f"Average: {avg:.2f}")
print("--------------------------------")
print(f"Your grade is: {grade}")

  