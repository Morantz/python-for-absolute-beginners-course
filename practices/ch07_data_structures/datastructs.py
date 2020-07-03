def show_header():
    print("---------------------------")
    print("    Dictionary Lesson")
    print("---------------------------")

def setup():
    global d
    d = {
        'Sam':      7,
        'rolls':    ['rock', 'paper', 'sicissors'],
        'done':     True
    }

# d = create d using core concepts above.
def tests():
    print(d["Sam"])          # outputs 7
    print(d['rolls'])        # outputs ['rock', 'paper', 'scissors']
    print(d.get('Sarah'))    # outputs None
    print(d.get('Jeff', -1)) # outputs -1
    print(d['done'])         # outputs True

def main():
    show_header()
    setup()
    tests()

if __name__ == '__main__':
    main()
