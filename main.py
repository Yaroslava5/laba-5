def p1():
    k = input("выберите число")
    k = int(k)
    l = [1,2,3,4,5,6]
    if k in l:
        print('поздравляю вы угадали!')
    else:
        print("нет такого числа")

def p2():

        list = ["1", "2", "3", "3", "5", "5", "6"]
        for i in range(len(list) - 1):
            if list[i] == list[i + 1]:
                print('Есть совпадение', list[i])


def p3():
    weeks = ("mond",'tued','wedd','thud','frid','sund','sutd')
    a =input('введите день: ')
    print('ваши выходные: ',weeks[7-int(a):])
    print("оставшие дни: ",weeks[:7-int(a)])

def p4():
    k = 0
    list = ["Юдина", " Капров", "Иванов", " студент1", "студент2", " студент3", " студент4", " студент5",
            "студент6", " студент7"]
    list1 = ["Юдина23", " Иванов", " Анисова", " студент0", "студент9", " студент77", " студент99", " студент66",
             "студент68", " студент87"]
    list2 = (list[0], list[1], list[0], list[8])
    print(list)
    print(list1)
    print(list2)