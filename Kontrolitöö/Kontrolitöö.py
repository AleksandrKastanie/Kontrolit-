from random import *
###задание 1 Заяц 
#n = ""
#while type(n)!=int: ## Так и не понял как сделать вторую проверку внутри этой, простите :'( (У меня была мысль с While true и заставить писать пользователя пока 1 из 9 символов не совпадет, но я не понял как составить)
#    try:
#        n=int(input("Введите значение от 1 до 9: "))
#    except TypeError:
#        print("попробуйте снова!")
#for i in range(n):
#    print("(\_/) ", end=" ")
#print()
#for i in range(n):
#    print("(o o) " , end=" ")
#print()
#for i in range(n):
#    print("/ | \*", end=" ")
#print()
#_____________________________________
## Задание 2 посчитать числовой ряд 
#A=input("Введите число: ")
#while int(A)<=1:
#    try:
#        A=int(input("введите "+str(i+1)+" число"))
#    except:
#        TypeError
#summa=0
#for i in range(1,int(A)+1):
#    summa+=i
#print("Cумма числового ряда ", summa) 
#___________________________________________
## Задание 3 отгадать число от 0 до 100 
#print("Компьютер загадал число от 0 до 100. Всего 10 попыток, поехали!")
#A=randint(0,101)
#numb=1
#while numb <= 10:
#    B = int(input(str(numb) + "-я попытка: "))
#    if B > A:
#        print("Многовато")
#    elif B < A:
#        print("Маловато")
#    else:
#        print("Вы угадали с",  numb ,  "попытки")
#        break
#    numb += 1
#___________________________________________
## Задание 4 перевернуть число обратное по порядку входящих в него цифр
#A=int(input("число: "))
#B = 0 
#while A>0:
#    B = B*10 + A%10
#    A = A//10
#print("Перевернутое число: " , B)
## Задание 5 Найти сумму и произведение цифр, введенного целого числа. Например, если введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).
A = int(input("Введите пожалуйста число, которое программа будет умножать и складывать"))
B = 0 #Сумма  цифр, изначальна равно 0, но после выполнения операции измениться 
C = 1
while A>0: # так как операции с 0 производить бессмысленно, цикл будет выполнять действие пока не выйдет из него 
    B += A%10 #В переменную для суммы цифр добавлять последнюю цифру числа, извлеченную при нахождении остатка от деления на 10.
    C *= A%10 #Значение переменной для хранения произведения цифр умножить на последнюю цифру числа.
    A = A//10 #Избавиться от последней цифры числа, разделив его нацело на 10.
print("Сумма:", B)
print("Произведение:", C)
