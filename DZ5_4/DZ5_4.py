def summary():
    try:
        with open('file_sum.txt', 'w+') as file_obj:
            line = input('Нужно ввести цифры через пробел \n')
            file_obj.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except IOError:
        print('В файле ошибка')
    except ValueError:
        print('В файле ошибка может есть буква')
summary()