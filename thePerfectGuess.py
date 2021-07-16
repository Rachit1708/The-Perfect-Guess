import random

random_number=random.randint(1,100)
print(random_number)

a=None
guesses=0

while a!=random_number:

    a=int(input("Enter a random number between 1 & 100: "))

    if a==random_number:

        print("You guessed it right!")

    else:

        print("Oops! You guessed it wrong")

        if a>random_number:

            print("The number is smaller than the number you entered")

        else:

            print("The number is greater than the number you entered")

        guesses+=1

print(f"Total number  of guesses : {int(guesses)+1}")

with open("highscore.txt","rt") as file:

    attempts=int(file.read())

if guesses<attempts:

    with open("highscore.txt","wt") as file:

        file.write(str(guesses+1))