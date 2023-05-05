import tabulate
import random
import time

def Kondorse(Matrix, Alter): # Входные параметры Matrix-групповой профиль, Alter-альтернативы
    Matr = Matrix.copy()
    Matr.pop(0) # Убираем строку выборщиков, так как она нам не нужна
    A = Alter.copy()
    if (Kondorse_Paradox(Matr)):
        print("Парадокс Кондорсе обнаружен.")
    else:
        if (len(Alter) < 2 or len(Matrix[0]) < 2): # Случай, когда либо 1 выборщик, либо 1 альтернатива
            print("Задача выбора вырождена, решение очевидно")
        alt = [0] * len(A) # Для каждой альтернативы смотрим насколько "высоко" данная альтернатива
        N = [] # Столбец матрицы для подсчета числа альтернатив ниже данной
        k = -1 # Индекс массива alt

        for el in A:
            k = k + 1
            for i in range (0, len(Matrix[0])):
                N = [x[i] for x in Matr] # Берем i-ый столбец
                alt[k] = alt[k] + Kondorse_N(N, el) # Подсчет альтернатив для i-ого столбца
                N = [] # Посчитали для i-ого столбца, очистили для следующего
        
        # Раскладываем в порядке убывания альтернативы и кладём их в res
        # Имеем ввиду, что alt[i] - число для альтернативы A[i]
        res = []
        for i in range(len(alt)):
            res.append([0] * len(alt))

        mn1 = -1 #0
        k = -1
        equal_alt = []
        while alt != []:
            k = k + 1
            mn = min(alt) # Находим минимальный элемент
            el = alt[0]
            i = 0
            while el != mn: # Находим индекс минимального элемента
                i = i + 1
                el = alt[i]
            if (mn == mn1): # Если равноправные альтернативы
                k = k - 1
                equal_alt.append(A[i])
                res[k] = equal_alt
            else:
                res[k]=A[i] # Добавляем альтернативу в начало
                equal_alt = []
            mn1 = mn # Сохраняем число на случай, если есть равнопранвые альтернативы
            equal_alt.append(res[k])
            alt.pop(i) # Удаляем этот элемент
            A.pop(i)
        
        # Итог - групповая ранжировка
        for row in res:
            if (type(row) != type([])): # Если это просто числа, то выводим их в столбик
                print(row)
            else: # Если есть равноправные, выводим их рядом
                for elem in row:
                    if (elem!=0 and type(elem)!=type([])):
                        print(elem, end = ' ')
                print()

# Функция для подсчета альтернатив в каждом столбце
def Kondorse_N(N, el): # Входные параметры N-столбец группового профиля, el-альтернатива, которую мы ищем в столбце
    i = 0
    res = 0
    while (not(el in N[i])): # Идём по списку, пока не найдём нужный элемент
        i = i + 1
    res = i # i - индекс элемента в столбце
    return res

# Функция для проверки парадокса Кондорсе
def Kondorse_Paradox(Matrix): # Входные параметры Matrix-групповой профиль без выборщиков
    # Получаем размеры матрицы
    n = len(Matrix[0])
    m = len(Matrix)
    # Создаем список рангов всех альтернатив
    ranks = [0] * m
    # Проходим по всем парам альтернатив и подсчитываем количество побед для каждой альтернативы
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            wins = 0
            for k in range(n):
                if Matrix[i][k] > Matrix[j][k]:
                    wins += 1
                    if Matrix[j][k] == '':
                        wins -= 1
                elif Matrix[i][k] < Matrix[j][k]:
                    if Matrix[i][k] == '':
                        wins -= 1
                elif Matrix[i][k] == Matrix[j][k]:
                    if Matrix[i][k] == '':
                        wins += 1
            # Если альтернативы не имеют разницы в голосах, то пропускаем
            if wins == n // 2:
                ranks[i] += 0.5
                ranks[j] += 0.5
                continue
            # Если i-ая альтернатива победила j-ую, то прибавляем единицу к рангу i-ой альтернативы
            if wins > n // 2:
                ranks[i] += 1
            # Иначе прибавляем единицу к рангу j-ой альтернативы
            else:              
                ranks[j] += 1
    # Получаем отсортированный по рангам список индексов альтернатив
    rank_order = sorted(range(m), key=lambda i: ranks[i], reverse=True)
    # Если две или более альтернатив имеют одинаковое количество голосов, то выводим сообщение о парадоксе Кондорсе
    if len(rank_order) > 1 and ranks[rank_order[0]] == ranks[rank_order[1]]:
        return 1
    else:
        return 0

#-------------------------------------------------------------------------------

# Функция Борда
def Borda(Matrix, Alter): # Входные параметры Matrix-групповой профиль, Alter-альтернативы
    Matr = Matrix.copy()
    Matr.pop(0) # Убираем строку выборщиков, так как она нам не нужна
    A = Alter.copy()
    if (len(Alter) < 2 or len(Matrix[0]) < 2): # Случай, когда либо 1 выборщик, либо 1 альтернатива
            print("Задача выбора вырождена, решение очевидно")
    alt = [0] * len(A) # Для каждой альтернативы считает число альтернатив, ниже данной
    N = [] # Столбец матрицы для подсчета числа альтернатив ниже данной
    k = -1 # Индекс массива alt
    
    for el in A:
        k = k + 1
        for i in range (0, len(Matrix[0])):
            N = [x[i] for x in Matr] # Берем i-ый столбец
        #for i in range (0, len(Matr) - 1):
            #for j in range (1, len(Matr[i]) +  1):
                #N.append(Matr[j][i]) # Составляем столбец
            #print(N)
            alt[k] = alt[k] + Borda_N(N, el, len(A)) # Подсчет альтернатив для i-ого столбца
            N = [] # Посчитали для i-ого столбца, очистили для следующего
        #print(alt[k])
    #print(alt)

    # Раскладываем в порядке убывания альтернативы и кладём их в res
    # Имеем ввиду, что alt[i] - число для альтернативы A[i]
    res = []
    for i in range(len(alt)):
        res.append([0] * len(alt))

    mx1 = 0
    k = -1
    equal_alt = []
    while alt != []:
        k = k + 1
        mx = max(alt) # Находим максимальный элемент
        el = alt[0]
        i = 0
        while el != mx: # Находим индекс максимального элемента
            i = i + 1
            el = alt[i]
        if (mx == mx1): # Если равноправные альтернативы
            k = k - 1
            equal_alt.append(A[i])
            #res.pop(k) # Удаляем последнюю альтернативу, чтобы заменить её списком равноправных
            #res[k]=[0] * len(equal_alt)
            res[k] = equal_alt
            #print(res)
            #print()
        else:
            res[k]=A[i] # Добавляем альтернативу в начало
            equal_alt = []
        mx1 = mx # Сохраняем число на случай, если есть равнопранвые альтернативы
        equal_alt.append(res[k])
        alt.pop(i) # Удаляем этот элемент
        A.pop(i)
    
    # Итог - групповая ранжировка
    for row in res:
        #print(row)
        if (type(row) != type([])): # Если это просто числа, то выводим их в столбик
            print(row)
        else: # Если есть равноправные, выводим их рядом
            for elem in row:
                if (elem!=0 and type(elem)!=type([])):
                    print(elem, end = ' ')
            print()

# Функция для подсчета альтернатив в каждом столбце
def Borda_N(N, el, lenRow): # Входные параметры: N - предпочтения n-ого выборщика, el - альтернатива, lenRow - предполагаемая длина столбца (то есть какая она должна быть, если нет равноправных альтернатив для выборщика)
    i = 0
    res = 0
    while (not(el in N[i])): # Идём по списку, пока не найдём нужный элемент
        i = i + 1 #
    # Когда нашли нужный элемент, смотрим, стоит он один или нет (len - 1, т.к. с 0 индексация)
    # От полного размера (len(A)) вычитаем 1 (т.к. индексация с 0), i (т.к. нам надо ниже нужного элемента) и длину (чтобы не учитывать те элементы, которые стоят вместе с этим)
    #res = res + (lenRow - 1 - i - (len(N[i])-1))
    i = i + 1
    # Пока не конец столбца и элемент не пустой прибавляем длину элемента, стоящего ниже
    while (i < lenRow and N[i] != ''): 
        res = res + len(N[i])
        i = i + 1
    #print(el,res)
    return res 
#-------------------------------------------------------------------------------

print("Введите количество выборщиков")
n = int(input()) # Количество выборщиков
#n = 3
print("Введите количество альтернатив")
m = int(input()) # Количество альтернатив
#m = 3
Alt = [0] * m # Список альтернатив
print("Введите альтернативы")
for i in range (0, m):
    Alt[i] = input()
    #Alt[i] = str(i + 1)
#Alt=['a','b','c']
    
electors = [] # Выборщики
electors.append([0] * n)
electors = electors[0]
print("Введите выборщиков")
for i in range (0, n):
    electors[i] = input()
    #electors.append(i + 1)

M = [] # Матрица для будущего транспонирования
Matr = []# Матрица для альтернатив для каждого выборщика
Flag = True # Для выбора ввода вручную или случайным образом
for i in range(m):
    Matr.append([0] * n)
for i in range(n):
    M.append([0] * m)

# Будет производиться ввод группового профиля вручную или рандомно
print("Если вы будете вводить групповой профиль вручную, нажмите 1, если рандомно, введите 0")
Flag = int(input())

if (Flag == 0):
    print("Вы выбрали случайное заполнение")
    start1 = time.time() ## точка отсчета времени
    # Составление группового профиля (в случае рандома)
    for i in range (0, n):
        M[i] = random.sample(Alt, len(Alt))
    # Транспонируем матрицу
    for a in range(len(M)):
        for b in range(len(M[0])):
            Matr[b][a] = M[a][b]
    end1 = time.time() - start1 
else:
    print("Вы выбрали ручной ввод")
    # Составление группового профиля (в случае ручного ввода)
    for i in range (0, n):
        print("Введите выбор %s выборщика" %electors[i])
        for j in range (0, m):
            Matr[j][i] = input()
        
Matr.insert(0, electors) # Добавляем на первую строку выборщиков
# Случай, когда есть лучшие (нет равноправных) в выборе
#Matr[0]=[1,2,3]
#Matr[1]=['c','a','a']
#Matr[2]=['b','b','c']
#Matr[3]=['a','c','b']
# Случай, когда 2 (a и c) равноправны в выборе
#Matr[0]=[1,2,3]
#Matr[1]=['b','b','a']
#Matr[2]=['c','c','b']
#Matr[3]=['a','a','c']
# Случай, когда все (a, b и c) равноправны в выборе
#Matr[0]=[1,2,3]
#Matr[1]=['c','b','a']
#Matr[2]=['b','a','c']
#Matr[3]=['a','c','b'] 
# Случай, когда всего две альтернативы
#Alt=['a','b']
#Matr[0]=[1,2,3]
#Matr[1]=['b','a','a']
#Matr[2]=['a','b','b']
# Случай, когда 2 (a и c) равноправны в выборе, причем в групповом профиле есть равноправные
#Matr[0]=[1,2,3]
#Matr[1]=['c','b','a']
#Matr[2]=['b','a','cb']
#Matr[3]=['a','c','']
# Парадокс Кондорсе
#Matr[0]=[1,2,3]
#Matr[1]=['a','c','b']
#Matr[2]=['b','a','c']
#Matr[3]=['c','b','a']
#Matr[0]=[1,2,3,4,5,6]
#Matr[1]=['a','c','b','a','c','b']
#Matr[2]=['b','a','c','b','a','c']
#Matr[3]=['c','b','a','c','b','a']

start2 = time.time() ## точка отсчета времени
print("Альтернативы: ")
for elem in Alt:
    print(elem, end = ' ')
print()
print()
print("Групповой профиль: ")
printMatr = tabulate.tabulate(Matr)
print(printMatr)
#for row in Matr:
#    for elem in row:
#        print(elem, end = ' ')
#    print()
print()

print("Групповая ранжировка по правилу Кондорсе: ")    
Kondorse(Matr, Alt)
print()
print("Групповая ранжировка по правилу Борда: ") 
Borda(Matr, Alt)
end2 = time.time() - start2
#print("Выполнение работы программы заняло ", (end1+end2), " секунд")
