import json
import os
from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "new_grades.json")  

# Load JSON data (single student object)
with open(file_path, "r") as file:
    student = json.load(file)

print("\n===================================")
print(f"Name: {student['Name']} (Age: {student['Age']})")

# Create Grades and Weights objects
my_grades = Grades()
weights = GradeWeights()

# Map JSON keys to Grades attributes
json_to_attr = {
    "quiz_1": "quiz_1",
    "quiz_2": "quiz_2",
    "midterm": "midterm",
    "project": "project",
    "final": "final"
}

# Set Grades object attributes from JSON
for json_key, attr_name in json_to_attr.items():
    if json_key in student:
        setattr(my_grades, attr_name, student[json_key])

# Print Grades object nicely
print("Grades object:", my_grades)

# Calculate overall course percentage
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f"The letter grade with an overall {percentage_grade * 100:.2f}% is {letter_grade}")

# Calculate optimistic grade (if remaining assignments are 100%)
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f"If all other assignments are 100%, the overall course would be {optimistic_percentage_grade * 100:.2f}%, which is a {optimistic_letter_grade}")
print("===================================\n")
