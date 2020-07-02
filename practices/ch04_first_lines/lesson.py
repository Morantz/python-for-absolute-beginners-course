import datetime

myage = 51

datenow = datetime.datetime.now()
year = datenow.year

print(f"The year is now : {year}")

name = input('What is your name? ')
age_t = input('How old are you? ')

age = int(age_t)

if age < myage:             # I am the eldest
    print(f'I am {myage - age} years older than you {name}!')
elif age == myage:          # We are same age
    print(f'Well {name}, we are the same age of {age}!')
else:                       # I am the youngest!
    print(f'I am {age - myage} years younger than you {name}!')

print("Isn't Python is great!!!")