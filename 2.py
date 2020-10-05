
amount = int(input("Кол-во элементов массива: "))
i = 0
my_list = []


while i < amount:
    my_list.append(input("Значение элемента: "))
    i = i + 1

n = 0

for element in range(len(my_list)):

    if len(my_list) % 2 == 0:
        while n < len(my_list):
            my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
            n += 2

    elif len(my_list) % 2 != 0:
        while n < (len(my_list) - 1):
            my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
            n += 2



print(my_list)

