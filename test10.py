def write_to_file(st):
    with open(r"test10.txt", 'a', encoding='utf-8') as ouf:
        ouf.write((st))


lines = []
with open(r"dataset_3363_4.txt", "rt", encoding="utf-8") as inf:
    for line in map(str.strip, inf):
        line = tuple(map(int, line.split(";")[1:]))
        write_to_file(str(sum(line) / len(line))) #just avg (each - toany)
        write_to_file('\n')
        lines.append(line)
count = len(lines)
for value in (sum(_) / count for _ in zip(*lines)):
    write_to_file(str(value) + " ")


    