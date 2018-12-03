pi = 0
n = input("Input Number: ")
n = int(n)
for i in range(0,n):
    pi += 4 * n / (i * i + n * n)
print(pi)