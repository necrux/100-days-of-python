#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

count = 0
total = 0

for student in student_heights:
    count += 1
    total += student

average = round(total / count)

print(average)
