print("===============================")
print("Task #17")
print("===============================")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c

print("Дискриминант D = %.2f" % discr)

def discr_great_zero(discr):
    return discr > 0

def discr_zero(discr):
    return discr == 0

def roots(a, b):
    import math
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    return x1, x2

def root(a, b):
    x = -b / (2 * a)
    return x

if discr_great_zero(discr):
    print("x1 = %.2f \nx2 = %.2f" % roots(a, b))

elif discr_zero(discr):
    print("x = %.2f" % root(a, b))

else:
    print("Корней нет")


print("===============================")
print("Task #18")
print("===============================")

