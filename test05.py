x = [int(input()) for i in range(int(input()))]
dict = {x:f(x) for x in set(x)}
print(*dict[i] for i in x, sep = '\n')



# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.

x = [int(input()) for i in range(int(input()))]
dict = {x:f(x) for x in set(x)}
print(dict)
print("x=",x)
for i in x:
    print(dict[i])
print(sep='\n')
print([dict[i] for i in x], sep = '\n')


