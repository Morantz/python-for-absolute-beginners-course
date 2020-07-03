import random

def show_header():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")

    print("Guess the number of M&Ms and you get lunch on the house!")
    print()

def get_guess():
    guess_t = input("How many M&Ms do you think are in the jar? ")
    return int(guess_t)

def test_guess(test):
    if test == mm_count:
        print('****  Your lunch is free!!  ****')
        return 1
    elif test < mm_count:
        print("     Sorry, that's too LOW!")
        return 0
    else:
        print("     Sorry, that's too HIGH!")
        return 0

def main():
    global mm_count                     # Needs to be visible to other functions!
    mm_count = random.randint(1, 100)

    attempt_limit = 5
    attempts = 0

    show_header()                       # Show the pretty header!

    while attempts < attempt_limit:
        guess = get_guess()
        attempts += 1

        if test_guess(guess):           # If guess was correct, then will return a 1 and break.
            break

    print(f"Bye, you're done in {attempts} attempts!")

if __name__ == '__main__':
    main()