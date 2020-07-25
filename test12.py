def compare(*args):
    flag = True
    for each in args:
        if each % 2 == 0:
            flag = True
        elif each % 2 > 0:
            flag = False
            break
    if flag == True:
        return min(args)
    else:
        return max(args) 
        

print(compare(10,10,32,32432423,30,1321312))



'''
def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

'''