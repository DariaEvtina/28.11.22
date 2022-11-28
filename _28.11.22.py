 Цепочки писем
 
Использовано 0,35 ГБ из 15 ГБ.
Условия использования · Конфиденциальность · Правила программы
Последние действия в аккаунте: 0 минут назад
Открыто в другом месте · Подробные сведения

###Задача  1
###Пользователь вводит число, программа определяет знак числа(положительное оно или отрицательное),
###если число положительное, то проверяет его на  четность и
###нечетность.
#from math import *

#print("Sisesta number")
#a=input("")
#if a.isalpha():
#    print("see on tekst")
#elif a.isdigit():
#     a=int(a)
#     if a>0:
#         if a%2==0:
#             print(f"{a} paaris")
#         else:
#            print(f"{a} paaritu")
#     else:
#        print(f"{a}ei soobi")
#else:
#    print(f"{a} segatud")

##Задача  2

##Спросить у пользователя 3 числа, если они окажуться положительными, 
##то проверить могут ли они быть углами одного треугольника(сумма углов 180) и 
##уточнить какого именно треугольника(равносторонний,
##равнобедренный или разносторонний).
#from math import *


#a,b,c=input("kusi 3 num").split()
#a=int(a)
#b=int(b)
#c=int(c)
#if a>0 and b>0 and c>0:
#   if a+b+c==180: 
#      if a==b and b==c:
#          tuup="vorkulgsed"
#      elif a==b and b==c and c==a:
#           tuup="vordhaarne"
#      else:
#         tuup="mitmekugne"
#   else:  
#       tuup="ei ole kolmnurk"
#else:
#     tuup="555"
#print(tuup)

##Задача  3

##Выяснить у пользователя желание расшифровать порядковый номер дня недели в название.
##Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами), 
##спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.
#from math import *

#a=input("Kas taha teada sama mis paev tana on ?")
#if a.lower()=="jah" or "ei":
#    a=input("mis number?")
#    if a=="1":
#        print("Esmaspaev")
#if a=="2":
#            print("Teisipaev")
#if a=="3":
#                print("Kolmapaev")
#if a=="4":
#                    print("Neljapaev")
#if a=="5":
#                        print("Reede")
#if a=="6":
#                            print("Laupaev")
#if a=="7":
#                                print("Puhapaev")
#if a>="8":
#             print("Viga!")

##Задача  4

##Определить по дню и месяцу рождения пользователя кто он по гороскопу. Проверять введенные 
##данные(тип данных и промежуток значений), иначе выводить сообветствующее сообщение

#from math import *
#d=input("mis paev sa oled sunditud? ") 
#m=input("mis kuu sa oled sunditud?")
#if d.isalpha() or m.isalpha():
#    print("tundmatu sumbol")
#elif d.isdigit or m.isdigit():
#    d=int(d)
#    m=int(m)
#    if d>0 and d<32 and m<13:
#        if (d>19 and m==2) or (d<21 and m==3):
#         print("Kalad")
#        elif (d>20 and m==1) or(d<20 and m==2):
#             print("Veevalaja")
#        elif (d>22 and m==12) or (d<21 and m==1):
#             print("Kaljukits")
#        elif (d>22 and m==11) or (d<23 and m==12):
#            print("Ambur")
#        elif (d>23 and m==10) or (d<23 and m==11):
#            print("Skorpion")
#        elif (d>23 and m==9) or (d<24 and m==10):
#            print("Kaalud")
#        elif (d>21 and m==8) or (d<24 and m==9):
#            print("Neitsi")
#        elif (d>22 and m==7) or (d<22 and m==8):
#            print("Lev")
#        elif(d>21 and m==6) or (d<23 and m==7):
#            print("Vahk")
#        elif(d>21 and m==5) or (d<22 and m==6):
#            print("Kaksikud")
#        elif(d>20 and m==4) or (d<22 and m==5 ):
#            print("Sonn")
#        elif(d>20 and m==3) or (d<20 and m==4):
#            print("Jaar")
#    else:
#           print("Seda sodiaagimärki pole olemas")

##Задача (самостоятельно)

##Проверить введенное пользователем число, отпределить его тип и если число целое,
##то найти от него 50%, если число дробное, то найти от него 70%, если это текст, то
##вывести его на экран. Для решения можно использовать: is_integer(), isalpha(), isdigit(),
##int(), float(), //, %.

#from math import *

#a=input("sisesta num")
#if a.isalpha():
#    print("see on tekst")
#elif a.isdigit():
#    a=int(a)
#    if a>0:
#        if a%1==0:
#            print(f"{a} taisarv")
#            a=a/2
#            print("50 protsenti sellest arvust =",a)
#else:
#    a=float(a)
#    if a>0:
#        if a%1!=1:
#            print(f"{a} murdarv")
#            a=a/100*70
#            print("70 protsenti sellest arvust =",a) 

##Задача  (самостоятельно)
##Написать программу для решения квадратного уравнения a*x**2+b*x+c=0.
##Спросить надо 3 значания: a, b, c.
##Найти D: D=b**2-4ac.
##Если D>0, то 2 решения,
##если D=0, то 1 решение,
#если D<0, то решений нет.

#import math

#print("sisesta koefitsendi")
#print("a*x**2+b*x+c=0")
#a=float(input("a="))
#b=float(input("b="))
#c=float(input("c="))

#discr=-b**2-4*a*c
#print("Disctriminant D=%2f" % discr)

#if discr>0:
#    x1=(-b+math.sqrt(discr))/(2*a)
#    x2=(-b-math.sqrt(discr))/(2*a)
#elif discr==0:
#    x = -b/(2*a)
#    print("x=%.2f" %x)
#else:
#    print("ei ole ruut")



#программа оенки
#from math import *

#hinne=int(input("mis hinne ?"))
#if hinne>=1 and hinne<=5:
#    if hinne==1 or hinne==2:
#             print("vaga halb")
#    if hinne==3:
#            print("rahuldav")
#    if hinne==4:
#            print("hea")
#    if hinne==5:
#            print("vaga hea")
#else:
#        print("viga")
