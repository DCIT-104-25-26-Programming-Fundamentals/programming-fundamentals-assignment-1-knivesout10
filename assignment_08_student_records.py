# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_average(scores):
    """Calculates and returns the average of a list of scores rounded to 2 decimal places."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def add_student():
    """Prompts the user for student details and appends the dictionary record to students_list."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    while True:
        try:
            num_scores = int(input("How many scores? "))
            if num_scores < 0:
                print("Number of scores cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of scores.")

    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid input! Please enter a numeric score.")

    # Create record dictionary and append to main list
    student_record = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students_list.append(student_record)
    print(f'Student "{name}" added successfully.')


def display_all_students():
    """Displays all student records in a formatted table."""
    if not students_list:
        print("\nNo student records found.")
        return

    print("\n" + "-" * 50)
    print(f"{'Name':<15} {'ID':<11} {'Scores':<14} {'Average':<8}")
    print("-" * 50)

    for student in students_list:
        scores_str = ", ".join(str(int(s) if s.is_integer() else s) for s in student["scores"])
        avg = calculate_average(student["scores"])
        print(f"{student['name']:<15} {student['id']:<11} {scores_str:<14} {avg:<8.2f}")

    print("-" * 50)


def calculate_student_average():
    """Searches for a student by ID and prints their average score."""
    search_id = input("Enter student ID: ").strip()

    for student in students_list:
        if student["id"] == search_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    print(f"Error: Student with ID '{search_id}' not found.")


# --- MAIN PROGRAM LOOP ---

def main():
    while True:
        print("\n================================")
        print("   STUDENT RECORD SYSTEM MENU   ")
        print("================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            calculate_student_average()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()