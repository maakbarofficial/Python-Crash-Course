# Complex data type -> Collection of datatypes

marks = [95, 98, 97, "DSA", "JavaScript", "Python"]
print(marks)
print(marks[0])

# the index can be minus one to start from reverse orders
print(marks[-1])

# 0 and 1 index will be included 2 will be not included
print(marks[0:2])

# for loop on marks
for score in marks:
    print(score)

# List Operation
marks.append(99)

print(marks)

marks.insert(0, 99)

print(marks)

print(99 in marks)

# Length of marks
print(len(marks))

# while loop on list
i = 0

while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()

print(marks)

# break and continue

students = ["ali", "akbar", "misbah", "cristiano", "imran khan"]

for student in students:
    if student == "cristiano":
        break
    print(student)

for student in students:
    if student == "akbar":
        continue
    print(student)
