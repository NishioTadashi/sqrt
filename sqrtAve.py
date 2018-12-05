before = 0
delta = 1e-300
while True:
    n = input("Please Input Number: ")
    n = float(n)
    if(n >= 0):
        break
ans = n
while True:
    if ans == 0:
        break
    before = ans
    ans = (ans + n / ans) / 2
    if ans - before < delta and before - ans < delta:
        break
print(ans)