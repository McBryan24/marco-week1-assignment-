#3. Write a program that checks if a student’s grade (0–100) is:
# - A: 80+ - B: 70–7 - C: 60–69 - D: 50–59 - F: < 50
stdt_grade = int(input("Enter student's grade:"))
if stdt_grade >= 80:
    print("Grade A")
elif stdt_grade >= 70:
    print("Grade B")
elif stdt_grade >= 60:
    print("Grade C")
elif stdt_grade >= 50:
    print("Grade D")
else:
    print("Grade F")
