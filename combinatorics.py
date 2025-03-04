import itertools
# combinations сочетания  
# arrangements размещения
# permutations перестановки

def generate_combinations():
    # Генерируем список чисел от 1 до n
    n = int(input("n-set size: "))
    k = int(input("k-combination size: "))
    numbers = list(range(1, n + 1))
    # Используем itertools.combinations для генерации всех сочетаний
    combinations = list(itertools.combinations(numbers, k))
    for comb in combinations:
        print(comb)

def generate_arrangements():
    # Генерируем список чисел от 1 до n
    n = int(input("n-set size: "))
    k = int(input("k-combination size: "))
    numbers = list(range(1, n + 1))
    # Используем itertools.permutations для генерации всех размещений
    arrangements = list(itertools.permutations(numbers, k))
    for arr in arrangements:
        print(arr)

def generate_permutations():
    n = int(input("n-set size: "))
    # Генерируем список чисел от 1 до n
    numbers = list(range(1, n + 1))
    # Используем itertools.permutations для генерации всех перестановок
    permutations = list(itertools.permutations(numbers))
    for perm in permutations:
        print(perm)

while True:
    print("Available features:")
    print("(C)ombinations")
    print("(A)rrangements")
    print("(P)ermutations")
    print("(Q)uit")
    choice = input("Make your choice: ").strip().lower()

    if choice == "c":
        generate_combinations()
    elif choice == "a":
        generate_arrangements()
    elif choice == "p":
        generate_permutations()
    elif choice == "q":
        break
