n = 51
while n > 20 :
    n = int(input("Введи натуральне число (не більше 20): "))

for x in range(n+1) :
    for p in range(n - x) :
        print(" ", end = "")
    for h in range(x) :
        print("#", end = "")
    print()
print(f"Кількість побудованих сходинок: {n}")