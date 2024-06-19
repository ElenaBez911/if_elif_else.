first=int(input('Введите число1: '))
second=int(input('Введите число2: '))
third=int(input('Введите число3: '))
if first == second == third:
    print(3)
elif first == second != third or first == third != second or second == third != first:
    print(0)
else:
    print(2)