print("Потрібна допомога із числами? Введи два цілих числа і я підкажу яке більше, а яке менше")
a = int(input("Давай перше: "))
b = int(input("Давай друге: "))
if a > b:
    print(a, '>', b)
if a < b:
    print(a, '<', b)
if a == b:
    print(a, '=', b)


