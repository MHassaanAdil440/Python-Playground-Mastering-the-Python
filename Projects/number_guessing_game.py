import random
n = random.randint(1,10)
guess = 0

while n != guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == n:
        print("You guessed it right!")
        break
    elif guess < n and guess > 0:
        print("Too low")
    elif guess > n and guess < 11:
        print("Too high")
    else:
        print("Invalid input")
print("N = {0}".format(n))
print("Booyeah!")





