#####__імпортуєму графічну біблотеку tkinter:__
_import tkinter as tkt_
_import math_
***
####__присвоюємо значеня і назви кнопкам:__
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
####__задаємо розміри калькулятора та назви кнопок:__
_wd =tkt.Tk()
wd.title('Калькулятор')
wd.geometry('500x650')
wd.configure(bg = 'pink')
buts= ['C','-', '+', '=',
       '1','2','3', '/','4','5','6','*',
       '7','8','9','0','sin','cos','tan',
       'ctg','log','ln','%','Bin',]
x = 18
y = 140_
***
####__задання формату для кнопок:__
_for button in buts:
    get_lbl = lambda x=button: calc(x)
    tkt.Button(text= button, bg = 'white', font=('Times New Roman', 20), command = get_lbl).place(x =x , y=y, width = 115, height = 80)
    x+= 120
    if x> 400:
        x= 20
        y+= 85
goo = '0'
label_txt= tkt.Label(text= goo, font = ('Times New Roman',35, 'bold'), bg = 'white',fg = 'black')
label_txt.place(x = 11, y = 50)
wd.mainloop()_
***
####__Результати:__
***
![image](https://user-images.githubusercontent.com/86964958/125848079-f38dd747-8916-4076-96ee-273336c94786.png)
![image](https://user-images.githubusercontent.com/86964958/125848190-24053429-e03d-4423-b4e6-d5f4bd97a232.png)
