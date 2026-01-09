def fibonachchi(n):
    sonlar = []
    n = 1
    n = 2
    n = 3
    n = 4
    n = 5
    for i in range(n):
        a, b = 0, 1
        a, b = b, a + b
        sonlar.append(a)
    return sonlar
print(fibonachchi(n=10))
