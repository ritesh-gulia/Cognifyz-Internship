import random

print("=" * 40)
print("      NUMBER GUESSING GAME")
print("=" * 40)

print("Choose Difficulty:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-200)")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    max_number = 50
elif choice == "2":
    max_number = 100
elif choice == "3":
    max_number = 200
else:
    print("Invalid choice! Default difficulty is Medium.")
    max_number = 100

secret_number = random.randint(1, max_number)
attempts = 0

print(f"\nGuess the number between 1 and {max_number}")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!\n")

        elif guess > secret_number:
            print("Too High!\n")

        else:
            print("\nCongratulations!")
            print(f"You guessed the correct number: {secret_number}")
            print(f"Total Attempts: {attempts}")
            break

    except ValueError:
        print("Please enter a valid number.")