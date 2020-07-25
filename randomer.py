import random


num = random.randint(1,100)

print("угадай число ", num) #!
t_list = [0]

print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ УГАДАЙ ЧИСЛО!\nЯ загадал число от 1 до 100\nЕсли Ваша отгадка дальше чем на 10 от моего числа, то я скажу вам ХОЛОДНО\nЕсли Ваша отгадка ближе чем на 10 от моего числа, то я скажу вам ТЕПЛО\nЕсли Ваша отгадка дальше чем предыдущая отгадка, то я скажу вам ХОЛОДНЕЕ\nЕсли Ваша отгадка ближе чем предыдущая отгадка, то я скажу вам ТЕПЛЕЕ")
print("НАЧНЁМ ИГРУ!")


while True:
    t = int(input("Твоё число = "))

    if 1> t or t > 100:
        t = int(input("Вне диапазона! \nТвоё число = "))
    elif t == num:
        print("DAAAAAAAAAA ты пробовал сделать это за {a} попитки".format(a = len(t_list)))
        break

    t_list.append(t)

    if t_list[-2] == 0:
        if abs(num - t) < 10:
            print("Тепло")
            continue
        elif abs(num - t) > 10:
            print("Холодно")
            continue

    else:
        if abs(num-t) < abs(num - t_list[-2]):
            print("Теплее")
            continue
        else:
            print("Холоднее")
            continue