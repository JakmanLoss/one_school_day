f = open('pr.txt')
# school_class = [int(x) for x in f.readlines()] #считывание файла в список с помощью генератора списков
school_class = []
for x in f.readlines():
    school_class.append(int(x))  # альтернативное считывание, делаем int, чтобы убрать знак переноса

ch_poz = 10**10
nc_poz = 10**10

for i in range(0, len(school_class), 2):
    if school_class[i] % 2 != 0:
        ch_poz = min(ch_poz, school_class[i])#нахождение минимального нечетного на чет поз

for j in range(1, len(school_class), 2):
    if school_class[j] % 2 == 0:
        nc_poz = min(nc_poz, school_class[j])#нахождение минимального четного на неч поз

kc = 0
kn = 0
for l in range(2, len(school_class), 2):
    if (school_class[l] % ch_poz == 0 and school_class[l - 2] % ch_poz != 0) or (school_class[l - 2] % ch_poz == 0 and school_class[l] % ch_poz != 0):
        kc += 1
#нахождение напрямую
'''masch = []
for i in range(len(school_class)):
    if i % 2 == 0:
        masch.append(school_class[i])#добавляем в массив все элементы на чётной позиции

for i in range(masch) - 1):
    if (masch[i] % ch_poz == 0 and masch[i + 1] % ch_poz != 0) or (masch[i + 1] % ch_poz == 0 and masch[i] % ch_poz != 0):
        kc += 1
#альтернативное нахождение пар'''


for l in range(3, len(school_class), 2):
    if (school_class[l] % nc_poz == 0 and school_class[l - 2] % nc_poz != 0) or (school_class[l - 2] % nc_poz == 0 and school_class[l] % nc_poz != 0):
        kn += 1

'''masnc = []
for i in range(len(school_class)):
    if i % 2 == 1:
        masnc.append(school_class[i])#добавляем в массив все элементы на чётной позиции

for i in range(len(masnc) - 1):
    if (masnc[i] % nc_poz == 0 and masnc[i + 1] % nc_poz != 0) or (masnc[i + 1] % nc_poz == 0 and masnc[i] % nc_poz != 0):
        kn += 1'''
#альтернативное нахождение пар
print(kc, kn)
