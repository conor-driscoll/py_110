# Problems w/ program:
#   - return statement isn't necessary
#   - counter isn't successfully reassigned with the function
#   - function doesn't need argument


def decrease():
    global counter
    counter -= 1

counter = 10

for _ in range(10):
    print(counter)
    decrease()

print('LAUNCH!')