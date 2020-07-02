import random

print("------------------------------")
print("     M&M guessing game!")
print("------------------------------")

print("Guess the number of M&Ms and you get lunch on the house!")
print()

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

def get_guess():
    guess_t = input("How many M&Ms are in the jar? ")
    return int(guess_t)

def test_guess(test):
    if test == mm_count:
        print('Your lunch is free!!')
        return 1
    elif test < mm_count:
        print("Sorry, that's too LOW!")
        return 0
    else:
        print("Sorry, that's too HIGH!")
        return 0

while attempts < attempt_limit:
    guess = get_guess()
    attempts += 1

    if test_guess(guess):
        break

print(f"Bye, you're done in {attempts} attempts!")
