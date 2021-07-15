#####імпортуєму графічну біблотеку tkinter
_import tkinter as tkt_
_import math_
***
####присвоюємо значеня і назви кнопкам
_def calc(oper):
    global goo
    if oper == 'C':
        goo = '0'
    elif oper == '=':
        goo = str(eval(goo))
    elif oper == 'sin':
        goo = str(math.sin(float(goo)))
    elif oper == 'cos':
        goo = str(math.cos(float(goo)))
    elif oper == 'tan':
        goo = str(math.tan(float(goo)))
    elif oper == 'ctg':
        goo = str(math.log1p(float(goo)))
    elif oper == 'log':
        goo = str(math.log10(float(goo)))
    elif oper == 'ln':
        goo = str(math.log(float(goo)))
    elif oper == 'Bin':
        goo = str(bin(int(goo)))
    else:
        if goo == '0':
            goo = ''
        goo += oper
    label_txt.configure(text=goo)_
***
####задаємо розміри калькулятора та назви кнопок
__
***
####задання формату для кнопок
__
***
####Результати:
![image](https://user-images.githubusercontent.com/86964958/125848079-f38dd747-8916-4076-96ee-273336c94786.png)
![image](https://user-images.githubusercontent.com/86964958/125848190-24053429-e03d-4423-b4e6-d5f4bd97a232.png)
