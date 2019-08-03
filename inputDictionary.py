
number_of_student = int(input('How many student in class '))
student = []

for i in range(number_of_student):
    student.append(input('Enter the student name'))

print(student)

list1 = []
list2 = []
list3 = []

di = {}

for i in range(len(student)):

    list1.append(int(input(f"Enter Math's Marks of student {student[i]}  ")))
    list2.append(int(input(f'Enter Physics Marks of student {student[i]} ')))
    list3.append(int(input(f'Enter Chemistry Marks of student {student[i]} ')))

    di[student[i]] = [list1[i], list2[i], list3[i]]

print(di)

sum = 0
newlist = []

for i in student:
    for j in di[i]:
        sum += j

    di[i] = sum
    newlist.append(sum)
    sum = 0

print(di)
newlist = sorted(newlist)
print(newlist)

di2 = {}

for i in newlist:
    for j in di:

        if i == di[j]:
            di2[j] = di[j]


print(di2)