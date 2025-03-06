import csv
from collections import defaultdict

grades_data = []
with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])
        grades_data.append(row)

subject_grades = defaultdict(list)

for row in grades_data:
    subject_grades[row["Subject"]].append(row["Grade"])

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, round(avg_grade, 1)])

print("'average_grades.csv' has been created successfully!")
