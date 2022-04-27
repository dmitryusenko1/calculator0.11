
entered_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", entered_list)

num_list = list(map(int, entered_list))
print("Список чисел: ", num_list)
print("Сумма списка:", sum(num_list))

if 0 in entered_list:
    try:
        1 / 0
    except ZeroDivisionError:
        print("You cannot divide by zero!")

