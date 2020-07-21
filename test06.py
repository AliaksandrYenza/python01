def read_str_file(file_path):
    with open(file_path) as inf:
        str = inf.read().strip()
    return str

def app():
    s_list = []
    c_list = []
    str = read_str_file('dataset_3363_2.txt') #need name ! 
    i = 0
    while i < len(str):
        buf = ''
        if str[i] > 'A': #char
            s_list.append(str[i])
        elif str[i] < 'A': #digit
            j = i
            while str[j] <'A' and j <= len(str): #<=
                buf += str[j]
                if j+1 <len(str): j += 1
                else: break
            c_list.append(buf)
            if str[j-2] < 'A' and str[j-1] < 'A' and i+1 < len(str): i += 1
        
        i += 1
    string = ''
    for o in range(len(s_list)):
        string += (s_list[o] * int(c_list[o]))
    write_to_file(s_list, string)            
    
def write_to_file(s_list, str):
    with open('reply_3363_2.txt', 'w') as ouf:
        ouf.write(str)

app()

#0 1 2 3 4 5 6 7 8 9 10
#a 3 b 4 c 2 e 1 0 b 1