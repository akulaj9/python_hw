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

print("===============================")
print("Task #9")
print("===============================")

string = "employee_first_name"
print(string)
lst = string.split("_")
employee = lst[0]
first = lst[1]
name = lst[2]
result = employee.title() + first.title() + name.title()
print(result)


print("===============================")
print("Task #10")
print("===============================")

s = 'Leo Tolstoy*1828-08-28*1910-11-20'
lst = s.split('*')
print(lst)
name = s.split( "*")[0]
date1 = lst[1]
date2 = lst[2]
year1 = date1.split('-')[0]
year2 = date2.split('-')[0]
age = int(year2) - int(year1)
result = "%s, %d" % (name, age)
print(result)