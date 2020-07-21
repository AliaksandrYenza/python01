#перерешать

import random

def step():
    row = int(input("X="))-1
    col = int(input("Y="))-1
    arr2[row][col] = arr[row][col]
    printArr(arr2)
    if arr2[row][col] == -1:
        print("BOOM!")
        return 1
    else:
        print("давай дальше...")
        return 0


def printArr(arr2):
    #frame
    for i in range(size):
        for j in range(size):
            print(arr2[i][j]," ", end='')
        print()

size = int(input("введите размер игры:"))
arr = [[0 for j in range(size)] for i in range(size)]

if size**2 > 5:
    for o in range(size ** 2 // 5):
        arr[random.randint(0, size-1)][random.randint(0, size-1)] = -1
else:
    arr[size//2][size//2] = -1

#пробегаемся по всем клентам
for i in range(size):
  for j in range(size):
    #если клетка 0, то нужно найти кол-во мин-соседей
    if arr[i][j] ==0:
      for di in range(-1,2):
        for dj in range(-1,2):
          ai= i+di
          aj= j+dj
          if 0<=ai<size and 0<=aj<size and arr[ai][aj]==-1:
            arr[i][j] +=1

arr2 = [["?" for j in range(size)]for i in range(size)]
for i in range(size):
    for j in range(size):
        print(arr2[i][j], end='')
    print()
print("Давай гадать. Вводи два значения через запятую(строка и столбец)")
while step() == 0:
    print()
