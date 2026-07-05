def right_triangle(rows):
    print("\nRight Triangle Pattern\n")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def inverted_triangle(rows):
    print("\nInverted Triangle Pattern\n")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def pyramid(rows):
    print("\nNumber Pyramid\n")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def diamond(rows):
    print("\nDiamond Pattern\n")

    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


while True:

    print("\n========== Number Pattern Generator ==========")
    print("1. Right Triangle")
    print("2. Inverted Triangle")
    print("3. Number Pyramid")
    print("4. Diamond Pattern")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("\nThank you for using the program.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice!")
        continue

    try:
        rows = int(input("Enter number of rows: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == "1":
        right_triangle(rows)

    elif choice == "2":
        inverted_triangle(rows)

    elif choice == "3":
        pyramid(rows)

    elif choice == "4":
        diamond(rows)