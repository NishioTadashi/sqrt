i = 1
pie = 0
while True:
    if i % 2 == 1:
        if i % 4 == 1:
            pie += 4 / i
        elif i % 4 == 3:
            pie -= 4 / i
    if i % 1000000 == 0:
        print(pie)
    i += 1
