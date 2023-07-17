def rost(n):  # проверка условия роста(больше 50 и меньше 200)
    if 50 < n < 200:
        return True
    return False


f = open('journal.txt')
# school_class = [int(x) for x in f.readlines()] #считывание файла в список с помощью генератора списков
school_class = []
for x in f.readlines():
    school_class.append(int(x))  # альтернативное считывание, делаем int, чтобы убрать знак переноса

nepod = 0
max_nepod = 0  # счётчики количества и суммы
'''for i in range(1, len(school_class) - 1):
    flag = True
    if rost(school_class[i - 1]) and rost(school_class[i]) and rost(school_class[i + 1]) and (school_class[i - 1] + school_class[i + 1] >= school_class[i]**2):
        flag = False
    else:
        flag = True
    if flag:
        nepod += 1
        if (school_class[i - 1] + school_class[i] + school_class[i + 1]) % 2 == 0:#проверка суммы на четность
            max_nepod = max(max_nepod, school_class[i - 1] + school_class[i] + school_class[i + 1])
print(nepod, max_nepod)'''

for i in range(1, len(school_class) - 1):
    if not (rost(school_class[i - 1]) and rost(school_class[i]) and rost(school_class[i + 1]) and (
            school_class[i - 1] + school_class[i + 1] >= school_class[i] ** 2)):
        nepod += 1
        if (school_class[i - 1] + school_class[i] + school_class[i + 1]) % 2 == 0:  # проверка суммы на четность
            max_nepod = max(max_nepod, school_class[i - 1] + school_class[i] + school_class[i + 1])
print(nepod, max_nepod)  # альтернативное решение, смотрим, когда условие не подходит
