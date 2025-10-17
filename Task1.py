c = float(input('Введите температуру в цельсиях: '))
if c % 2 == 0:
    ch = 'четное' 
else:
    ch = 'нечетное'
if c > 0:
    opr = 'положительное'
elif c < 0:
    opr = 'отрицательное'
else:
    opr = '0'
if 10 <= c <= 50:
    diap = 'принадлежит диапозону [10; 50]'
else:
    diap = 'не принадлежит диапозону [10; 50]'
print(ch)
print(opr)
print(diap)
print('Температура в фаренгейтах:',round(((c * 9/5) + 32), 2))
print('Температура в кельвинах:',round((c + 273.15), 2))

from random import *
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb = ['!', '@', '#', '$', '%', '^', '&', '*']
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = sample(nums, 3)
b = sample(symb, 2)
c = sample(alp, 3)
print((a + b + c))

from collections import *
stroka = str(input('Введите символы: ').lower())
print('Количество символов:', Counter(stroka))
print('Самый частый символ:', list(Counter(stroka))[0]) 

num = int(input('Введите число: '))
for i in range(2, num + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and \
    i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and \
    i % 8 != 0 and i % 9 != 0:       
        print(i)
