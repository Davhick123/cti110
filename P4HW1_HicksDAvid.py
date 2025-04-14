# Your Name: [David Hicks]
# Date: [4/13/25]
# Assignment Name: [P4HW1_HicksDAvid.py]
# Description: This program allows the user to input multiple test scores,
#              validates each entry, removes the lowest score, calculates
#              the average of the remaining scores, and assigns a letter grade.
def main():
    score_list = []

    num_scores = int(input("How many scores do you want to enter? "))

    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score #{i}: "))
                if 0 <= score <= 100:
                    score_list.append(score)
                    break
                else:
                    print("\nINVALID Score entered!!!!")
                    print("Score should be between 0 and 100")
                    print(f"Enter score #{i} again:", end=" ")
            except ValueError:
                print("\nInvalid input! Please enter a numeric value.")
                print(f"Enter score #{i} again:", end=" ")

    # Find lowest score
    lowest_score = min(score_list)

    # Remove lowest score for modified list
    modified_scores = score_list.copy()
    modified_scores.remove(lowest_score)

    # Calculate average
    average = sum(modified_scores) / len(modified_scores)

    # Determine grade
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Display results with formatting
    print("\n--------------Results-------------")
    print(f"Lowest Score   : {lowest_score:.1f}")
    print(f"Modified List  : {modified_scores}")
    print(f"Scores Average : {average:.2f}")
    print(f"Grade          : {grade}")
    print("----------------------------------")

# Run the program
main()