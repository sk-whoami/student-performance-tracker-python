# Assignment: "Student Performance Tracker"
# Objective:
# Create a program that manages student records, calculates grades, and stores the results in a file.

# Requirements:
# Data Entry
# Allow the user to enter student details: Name & ID

# subject score for Maths
# Store the data in a dictionary with the student ID as the key.

# Grade Calculation
# Create a function that:
# Calculates the average score for each student.

# Assigns a letter grade:
# A = 90–100
# B = 80–89
# C = 70–79
# D = 60–69
# F = below 60

# Error Handling
# Ensure invalid inputs (e.g., negative scores, scores > 100) raise and handle exceptions gracefully.

# Saving Data
# Store all student records in a file (students.txt or students.json).

# Save and Exit
# Export data to a CSV file.

import json
import random
import csv 
student = {}

name_surname = input("Name & Surname: ")
while True:
    try:
      maths_score = int(input("What is your maths score?: "))
      break
    except ValueError:
      print("Numbers only !")
letter = "SID"
idnumber = random.randint(1,30)
print("Your Student ID number is : ",letter,idnumber)
student_id = "SID" + str(idnumber)   
students_info = {
     "name_surname": name_surname,
      "maths_score": maths_score,
      "student_id": student_id
  }
# # A = 90–100
# # B = 80–89
# # C = 70–79
# # D = 60–69
# # F = below 60
def grade(maths_score):
  if maths_score >=90:
    return "A"
  elif maths_score >=80:
    return "B"
  elif maths_score >=70:
    return "C"
  elif maths_score >=60:
    return "D"
  else:
    return "F"
print("Grade :", (grade(maths_score)))

grade(maths_score)

file_name =json.dumps(students_info)
print(file_name,".json")

with open(file_name, "w") as file:
  json.dumps(students_info)
  
with open(file_name, "w") as file:
  writer = csv.writer(file)
  writer.writerow(["Name","Maths Score", "Student ID" ] )
  writer.writerow([name_surname,maths_score,student_id ])
  print("Your Performance is ready to view . ",file_name)

