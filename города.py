#БИБЛИОТЕКИ
from datetime import *
from tkinter import *
from tkinter import messagebox

#САМЫЕ КРУПНЫЕ ГОРОДА РОССИИ (92)
utc2_list = ['калининград']
utc3_list = ['москва','санкт петербург','нижний новгород','казань','ростов на дону','воронеж','краснодар','саратов','ярославль','махачкала','рязань','набережные челны','пенза','липецк','киров','чебоксары','тула','курск','ставрополь','сочи','тверь','иваново','брянск','белгород','владимир','архангельск','калуга','смоленск','череповец','саранск','орёл','вологда','владикавказ','грозный','мурманск','тамбов','петрозаводск','кострома','новороссийск','йошкар ола','таганрог','сыктывкар','нальчик','нижнекамск','шахты','дзержинск','старый оскол','великий новгород','псков','минеральные воды','севастопль','симферопль']
utc4_list = ['самара','волгоград','тольятти','ижевск','ульяновск','астрахань']
utc5_list = ['екатеринбург','челябинск','уфа','пермь','тюмень','оренбург','магнитогорск','сургут','нижний тагил','курган','стерлитамак','нижневартовск','орск']
utc6_list = ['омск']
utc7_list = ['новосибирск','красноярск','барнаул','томск','кемерово','новокузнецк','бийск','прокопьевск','норильск']
utc8_list = ['иркутск','улан удэ','братск','ангарск']
utc9_list = ['чита','якутск','благовещенск']
utc10_list = ['хабаровск','владивосток','комсомольск на амуре']

#ФУНКЦИЯ ПОИСКА СРЕДИ СПИСКОВ
def show():
    #ВРЕМЯ
    time = str(datetime.now())
    hours = time[11:13]
    mins = time[14:16]

    #ФУНКЦИЯ
    city = city_field.get()
    re_city = ''
    
    for letter in city:
        if letter == '-':
            re_city = str(re_city) + ' '
        else:
            re_city = str(re_city) + str(letter)
    
    re_city = re_city.lower()
    head = re_city.capitalize() #ВОССТАНОВИТЬ БОЛЬШУЮ БУКВУ
    
    if re_city in utc2_list:
        hours = int(hours)-1
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
        
    elif re_city in utc3_list:
        hours = int(hours)
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
        
    elif re_city in utc4_list:
        hours = int(hours)+1
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
        
    elif re_city in utc5_list:
        hours = int(hours)+2
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
    
    elif re_city in utc6_list:
        hours = int(hours)+3
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
        
    elif re_city in utc7_list:
        hours = int(hours)+4
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
        
    elif re_city in utc8_list:
        hours = int(hours)+5
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
        
    elif re_city in utc9_list:
        hours = int(hours)+6
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
    
    elif re_city in utc10_list:
        hours = int(hours)+7
        messagebox.showinfo(head, '    '+str(hours)+':'+str(mins)+'    ')
        
    else:
        messagebox.showerror('Ошибка','Вашего города нет в списке. Либо он не существует!')
    
    #ЗАПИСЬ В ФАЙЛ
    with open('Change_Log.txt', 'a') as file:
        file.write(head+' - '+str(hours)+':'+str(mins)+'\n')

def help():
    messagebox.showinfo('Справка', 'В программе реализована функция выбора среди самых крупных городов России. Полный список можно посмотреть в файле README.'+'\n\n'+'Регистр не влияет на работу программы!')
    #ЗАПИСЬ В ФАЙЛ
    with open('Change_Log.txt', 'a') as file:
        file.write('Пользователь открыл Справку'+'\n')

#ИНТЕРФЕЙС
root = Tk()
root.title("Время в городах")
root.configure(background = '#5490de')
root.geometry("300x110")
root.resizable(height = 0, width = 0)

label = Label(root, text = 'Введите город: ',bg = "#5490de")
label.grid(row = 0, column = 0, padx = 5)

city_field = Entry(root, font = "lucida 10")
city_field.grid(row = 0, column = 1, pady = 8)

button = Button(root,text = "Ввод",bg = "#afdafc",command = show)
button.grid(row = 2, column = 1, pady = 8)

button_q = Button(root,text = "Справка",bg = "light blue",command = help)
button_q.grid(row = 3, column = 0, sticky = W, padx = 5)

root.mainloop()