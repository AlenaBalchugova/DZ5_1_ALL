One_Fore = {'One' : 'Один',
            'Two' : 'Два',
            'Three' : 'Три',
            'Four' : 'Четыре'}
new_file = []
with open('betwin1_4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(One_Fore[i[0]] + '  ' + i[1])
    print(new_file)

with open('betwin1_4_n.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)