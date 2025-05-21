friday_schedule = ["Математика", "Англійська мова", "Історія", "Фізика", "Інформатика"]
k = len(friday_schedule)
print("Розклад (по одному уроку):")
for lesson, n in zip(friday_schedule, range(k)):
    print(f"{n+1}) {lesson}")
print(f"Всього {k} уроків")
