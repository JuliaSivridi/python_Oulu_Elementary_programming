import itertools
# combinations сочетания  
# arrangements размещения
# permutations перестановки

# COLORS = ["black", "grey", "pink", "blue", "green"]

def prompt_n_and_k(col):
    k = 0
    while True:
        try:
            n = int(input("n-set size: "))
            if col > 1:
                k = int(input("k-combination size: "))
        except ValueError:
            print("Value must be a plain number")
        else:
            break
    return n, k

def generate_combinations():
    n, k = prompt_n_and_k(2)
    # Генерируем список чисел от 1 до n
    numbers = list(range(n))
    # Используем itertools.combinations для генерации всех сочетаний
    combinations = list(itertools.combinations(numbers, k))
    return combinations

def generate_arrangements():
    n, k = prompt_n_and_k(2)
    # Генерируем список чисел от 1 до n
    numbers = list(range(n))
    # Используем itertools.permutations для генерации всех размещений
    arrangements = list(itertools.permutations(numbers, k))
    return arrangements

def generate_permutations():
    n, k = prompt_n_and_k(1)
    # Генерируем список чисел от 1 до n
    numbers = list(range(n))
    # Используем itertools.permutations для генерации всех перестановок
    permutations = list(itertools.permutations(numbers))
    return permutations

while True:
    print("")
    print("Available features:")
    print("(C)ombinations")
    print("(A)rrangements")
    print("(P)ermutations")
    print("(Q)uit")
    choice = input("Make your choice: ").strip().lower()

    if choice == "c":
        sets = generate_combinations()
    elif choice == "a":
        sets = generate_arrangements()
    elif choice == "p":
        sets = generate_permutations()
    elif choice == "q":
        break
    for set in sets:
        print(set)
        # color = ""
        # for _ in set:
            # color = color + COLORS[_] + " "
        # print (color)
