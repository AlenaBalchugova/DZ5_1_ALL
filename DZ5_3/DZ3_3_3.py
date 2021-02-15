with open('zp.txt', 'r') as my_file:
    s = []
    n = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           n.append(i[0])
        s.append(i[1])
print(f'Оклад меньше 20.000тр {n}, оклад средний  {sum(map(int, s)) / len(s)}')