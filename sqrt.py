before = 0
delta = 0.000000000000001
while True:
    n = input("Please Input Number: ")
    n = float(n)
    if(n >= 0):
        break
ans = n
while True:
    if(ans == 0):
        break
    before = ans
    ans = ans - ((ans) * (ans) - n) / (2 * (ans))
    if(ans - before < delta and before - ans < delta ):
        break
print(ans)