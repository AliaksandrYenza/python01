import fileinput
from collections import Counter
  
c = Counter(word for line in fileinput.input(files=('dataset_3363_3.txt')) for word in line.casefold().split())
max_count = max(c.values())
f1 = open("1.txt", "w+")
print(*min(p for p in c.items() if p[1] == max_count), file = f1)