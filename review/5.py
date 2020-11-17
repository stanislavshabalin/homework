a = float(input('Число км в первый день '))
b = float(input('Число км в последний день '))
n = 1
print(str(n) + "-й день - " + str(a) + " км")
for i in range(100):
    a = a + (a / 10)
    n = n + 1
    print(str(n) + "-й день - " + str(a) + " км")
    if a >= b:
        print('В ' + str(n) + ' день спортсмен достиг результата — не менее ' + str(b) + ' км.')
        break


5