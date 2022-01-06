# a = list(map(int, input("a:").split()))
# b = list(map(int, input("b:").split()))
# for k in range(0, len(a)):
#     k1 = a[k]
#     k2 = b[k]
#     c = float((k1**2 + k2**2)**0.5)
#     s = float((k1 * k2) / 2)
#     print(f"Треугольник{k+1} с катетами {k1} и {k2} имеет площадь {s} и гипотенузу {c}")

a = list(map(int, input("a, b:").split()))
for k in range(0, len(a), 2):
#     if k == 0 or k % 2 == 0:
        k1 = a[k]
        k2 = a[k+1]
        c = float((k1**2 + k2**2)**0.5)
        s = float((k1 * k2) / 2)
        print(f"Треугольник{k+1} с катетами {k1} и {k2} имеет площадь {s} и гипотенузу {c}")