list = input().lower().split()
uniq_set = set(list)
for i in uniq_set:
    print("{} {}".format(i, list.count(i)))