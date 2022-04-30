from ctb import place

for x in range(10):
    place(x, 0, 0)
    place(x, 0, 10)
    place(x, 10, 10)
    place(x, 10, 0)

for z in range(10):
    place(0, 0, z)
    place(10, 0, z)
    place(10, 10, z)
    place(0, 10, z)

for y in range(11):
    place(0, y, 0)
    place(10, y, 10)
    place(0, y, 10)
    place(10, y, 0)
