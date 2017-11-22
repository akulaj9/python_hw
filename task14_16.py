import math
print("===============================")
print("Task #14")
print("===============================")

n = float(input("Введите число, которое нужно проверить на четность:"))

def is_even(n):
    return n % 2 == 0

if is_even(n):
    print("\nОтвет: число '%d' - четное." % n)
else:
    print("\nОтвет: число '%d' - не четное." % n)


print("===============================")
print("Task #15")
print("===============================")

input_data = input("Enter data for the 1st circle (x,y,r): ")
x1, y1, r1 = [float(x.strip()) for x in input_data.split(',')]

input_data = input("Enter data for the 2nd circle (x,y,r): ")
x2, y2, r2 = [float(x.strip()) for x in input_data.split(',')]

def d(x1, y1, x2, y2):
    return abs(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))

def distant(d, r1, r2):
    return d > r1+r2

def within(d, r1, r2):
    return d < abs(r1-r2)

d = d(x1, y1, x2, y2)

if not distant(d, r1, r2) and not within(d, r1, r2):
    print("\nОтвет: окружности пересикаються.")
else:
    print("\nОтвет: окружности не пересекаються.")


print("===============================")
print("Task #16")
print("===============================")

V1 = float(input("Скорость первого поезда:"))
V2 = float(input("Скорость второго поезда:"))
S = float(input("Растояние между поездами:"))
S1 = float(input("Дистанция до запасного пути:"))
S2 = S - S1

def elapsed_time (S, V):
    return S/V

def collision (elapsed_time1, elapsed_time2):
    return elapsed_time1 >= elapsed_time2

if collision(elapsed_time(S1, V1), elapsed_time(S2, V2)):
    print("Ответ: поезда столкнутся.")
else:
    print("Ответ: поезда разъедутся.")
