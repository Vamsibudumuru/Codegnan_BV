import random
attempts = 0
num = random.randint(1, 10)
while attempts < 3:
    guess = int(input("Enter number (1-10): "))
    if guess == num:
        print("Correct, You won the game")
        attempts = 4
    else:
        attempts+= 1
        print(f"Wrong, you have {3-attempts} attempts left")
if attempts == 3:
    print(f"You lost the game and the number is {num}")
