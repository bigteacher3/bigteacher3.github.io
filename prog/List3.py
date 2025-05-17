items = ["Зошит в клітинку", "Лінійка", "Ручка кулькова", "Папка-органайзер"]
prices = [3.55, 4.30, 2.49, 59.74]

print("Список товарів:")
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")

choice = int(input("Введіть номер товару: "))

index = choice - 1

print(f"Ціна обраного товару: {prices[index]}")

print(items[index], prices[index])