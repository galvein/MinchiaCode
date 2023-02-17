"""Print employees in ascending order."""
# define employees data
employees = [
    [10, "Roberto", "Fiore", 1, 0.1, 2022],
    [2, "Gianna", "Naninni", 2, 2000, 2022],
    [30, "Il", "Principe", 2, 3000, 2022],
    [4, "Julius", "Cesar", 4, 4000, 2022],
    [50, "Adriano", "Celentano", 5, 4000, 2021],
    [6, "Reinhold", "Messner", 6, 4000, 2019]
]

# sort employees list by id
employees = sorted(employees, key=lambda x: x[0])

# print employees list
for i in range(len(employees)):
    for j in range(len(employees[i])):
        print(employees[i][j], end=" ")
    print()
