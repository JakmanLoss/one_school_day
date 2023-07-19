f = open('pr.txt')
# school_class = [int(x) for x in f.readlines()] #считывание файла в список с помощью генератора списков
school_class = []
for x in f.readlines():
    school_class.append(int(x))  # альтернативное считывание, делаем int, чтобы убрать знак переноса

k = 0
mink = 10**10 #счётчик для кол-ва пар и нахождения минимума, мин задан 10**10 т.к. числа, сравнимые с ним будут меньше
for i in range(len(school_class) - 1):
    if (school_class[i] % 10 == school_class[i + 1] % 10) and (school_class[i] % 4 != school_class[i + 1] % 4):#проверка на последнюю цифру и разные остатки
        if ((school_class[i]**2 + school_class[i + 1]**2) % 2 != 0) and ((school_class[i]**2 + school_class[i + 1]**2) > 100):
            k += 1
            mink = min(mink, school_class[i] + school_class[i + 1])

print(k, mink)
