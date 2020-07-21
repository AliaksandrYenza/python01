def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    else:
        if 2*key in d:
            d[2*key].append(value)
        elif 2*key not in d and d.get(2*key) == None:
            d[2*key] = []
            d[2*key].append(value)
    print(d)

d = {1: [1,11,111], 2:[21,22,23], 3:[31,23]}
key = int(input("Введи ключ = "))
value = input("введи значение = ")
update_dictionary(d,key,value)