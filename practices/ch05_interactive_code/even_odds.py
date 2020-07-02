# Lesson Chapter 5
#
# Ask user for a number and then print whether it is Even or Odd
#
# Entry of a Zero ends the game!

while 1:
    num_t = input('Enter a number : ')

    num = int(num_t)

    if num == 0:
        break

    rem = num % 2

    if rem:
        print(f'{num} is an ODD number!')
    else:
        print(f'{num} is an EVEN number!')

print('Thanks for playing!!!')
