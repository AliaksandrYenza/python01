def f(a):
    for i in range(1,len(a)):
        if a[i-1] == a[i] == 3:
            return True
        else:
            return False


print(f([30,3,13,4,3,32,5]))