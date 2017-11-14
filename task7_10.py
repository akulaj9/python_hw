print("===============================")
print("Task #7")
print("===============================")

current_date = "11.14.2017"

print(current_date)
lst = current_date.split(".")
mounth = lst[0]
day = lst[1]
year = lst[2]
new_format = day + "." + mounth + "." + year
print(new_format)


print("===============================")
print("Task #8")
print("===============================")

student_old = "Eugenia Nikolaeva"
print(student_old)
lst = student_old.split(" ")
name = lst[0]
surname = lst[1]
student_new = surname + " " + name
print(student_new)