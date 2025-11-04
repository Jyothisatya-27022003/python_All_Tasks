import random
secret_number = random.randint(1, 100)

attempts = 0  # To count number of attempts

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1
        if guess < 1 or guess > 100:
            print("⚠️ Please guess a number between 1 and 100.")
        if guess < secret_number:
            print("📉 Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("📈 Too high! Try a lower number.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

    except ValueError:
        print("⚠️ Invalid input! Please enter a number.\n")
