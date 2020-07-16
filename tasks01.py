#перерешать ! 


#arr[col_len-1][row_len]+arr[col_len+1][row_len]+arr[col_len][row_len-1]+arr[col_len][row_len+1]
col_len=0
row_len=1
md=""
arr=[]
a0,b0,an,bn=0,0,0,0
# формируем матрицу
while row_len>0: # бесконечный цикл
    md=input().split() # разбиваем строку на элементы для добавления в список
    if "end" in md:
        row_len-=1
        break # если в строке попалось END, закрываем список
    else:
        if row_len==1:
            col_len=len(md)
        row_len+=1 # счетчик
        arr.append(md) # добавляем элементы строки в двухмерный список
# формируем нулевую матрицу
arr_sum = [[0 for j in range(col_len)] for i in range(row_len)]
# определяем в матрице элементы из суммы смежных
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i-1<0: a0=row_len-1
        else: a0=i-1
        if j-1<0: b0=col_len-1
        else: b0=j-1
        if i+1>row_len-1: an=0
        else: an=i+1
        if j+1>col_len-1: bn=0
        else: bn=j+1
        arr_sum[i][j]= int(arr[a0][j])+int(arr[an][j])+int(arr[i][b0])+int(arr[i][bn])
# выводим новую матрицу на экран
for row in arr_sum:
    for elem in row:
        print(elem, end=' ')
    print()
print(arr[1][2])