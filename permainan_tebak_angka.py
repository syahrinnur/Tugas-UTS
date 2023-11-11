import random

number = random.randint(1, 100)
guess = int(input("Guess the number (1-100): "))

if guess == number:
    print("Selamat...! Tebakan anda benar.")
else:
    print("Maaf tebakan anda salah...! Yang benar adalah", number)