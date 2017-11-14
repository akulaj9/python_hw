import math
print("===============================")
print("Task #1")
print("===============================")

a = 10
b = 25
c = 30
equation = a + b * (c / 2)
result = "Выражение a + b * (c / 2) при a = %d, b = %d, c = %d, равно %d." % (a, b, c, equation)
print(result)


print("===============================")
print("Task #2")
print("===============================")

a = 10
b = 5
equation = (a**2 + b**2) % 2
result = "Выражение №2 при a = %d, b = %d, равно %d." % (a,b, equation)
print(result)


print("===============================")
print("Task #3")
print("===============================")

a = 10
b = 20
c = 30
equation = (a + b) / 12 * c % 4 + b
result = "При a = %d, b = %d, c = %d, b = %d, равно %d." % (a, b, c, b, equation)
print(result)


print("===============================")
print("Task #4")
print("===============================")

a = 15
b = 26
c = 35
equation = (a - b * c) / (a + b) % c
result = "При a = %d, b = %d, c = %d, a = %d, b = %d, c = %d, равно %d." % (a, b, c, a, b, c, equation)
print(result)


print("===============================")
print("Task #5")
print("===============================")

a = 50
b = 30
c = 15
equation = math.fabs(a - b)/(a + b)**3 - math.cos(c)
print("При a = %d,  b = %d, c = %d равно %.2f" % (a, b, c, equation))
print(result)


print("===============================")
print("Task #6")
print("===============================")

a = 20
b = 10
c = 5
equation = (math.log1p(1 + c) / -b)**4+math.fabs(a)
print("При a = %d,  b = %d, c = %d равно %.2f" % (a, b, c, equation))
print(result)