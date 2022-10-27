from random import randint
a=int(input("1 - Ручной ввод, 2 - Случайный набор чисел: "))
maxl=0
A = []
if a ==1:
    b=int(input('Сколько элементов будет в множестве: '))
    for k in range(b):
        print("Введите ", k+1, " элемент A: ", end='')
        m=int(input())
        A+=[m]
        if len(str(m))>maxl: maxl=len(str(m))
    C = []
    B = []
    for k in range(len(A)):
        for l in range(len(A)):
            B += [[A[k], A[l]]]
    print(A, B, sep='\n')
    for k in range(len(B)):
        if B[k][1] == (2*B[k][0]) - 1:
            C += [B[k]]
    print()
elif a==2:
    b=int(input('Сколько элементов будет в множестве: '))
    for k in range(b):
        m=randint(10, 99)
        A+=[m]
        if len(str(m)) > maxl: maxl = len(str(m))
    A.sort()
    B = []
    C = []
    for k in range(len(A)):
        for l in range(len(A)):
            B += [[A[k], A[l]]]
    print(A)
    for k in range(len(B)):
        if B[k][1] == (2*B[k][0]) - 1:
            C += [B[k]]
    print()
else: print("Вы ошиблись вариантом")

print(' '*(maxl+1), end='')
for k in A:
    print(k, end=' ')
print()

for k in range(len(A)):
    print(A[k], end=' '* ((maxl+1)-len(str(A[k]))))
    for l in range(len(A)):
        if [A[k], A[l]] in C: print(1, end=' '*len(str(A[l])))
        else: print(0,  end=' '*len(str(A[l])))
    print()

lot = 1
for m in A:
    if [m, m] not in C:
        lot=0
if lot==0:
    print('Множество не рефлексивно')
if lot == 1:
    print('Моножество рефлексивно')

lot = 1
for m in C:
    if m[::-1] not in C:
        lot=0
if lot==0:
    print('Множество не симметрично')
if lot == 1:
    print('Моножество симметрично')

lot = 1
for m in C:
    for x in C:
        if m[1]==x[0] and [m[0], x[1]] not in C:
            lot=0
if lot==0:
    print('Множество не транзитивно')
if lot == 1:
    print('Моножество транзитивно')