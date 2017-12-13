import math
print("===============================")
print("Task 1_3")
print("===============================")

def example1(a, b, c):
    return (a+b*c)**2

def example2(a, b, c):
    return a-4*b/c

def example3(a, b, c):
    return (a*b+4)/(c-1)

a = 10
b = 20
c = 30
result1 = example1(a, b, c)
result2 = example2(a, b, c)
result3 = example3(a, b, c)

power2 = "\u00B2"

print("For example (a+b*c)%s the answer = %0.2f" % (power2, result1))
print("For example a-4*b/c the answer = %0.2f" % result2)
print("For example (a*b+4)/(c-1) the answer = %0.2f" % result3)