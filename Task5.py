a = 20
b = 21
c = 22

a = int(input("Количество студентов в первой группе: "))
b = int(input("Количество студентов во второй группе: "))
c = int(input("Количество студентов в третьей группе: "))

desks = int(round(a / 2 + b / 2 + c / 2))

print(desks)

# desks = (a // 2) + (b // 2) + (c // 2) + (a % 2) + (b % 2) + (c % 2)

