print("Input three numbers plz:")
number = input()
Fizz, Buzz, Shmuzz = list(map(int, number.split()))

for i in range(1, Shmuzz + 1):
    if i % Fizz == 0 and i % Buzz == 0:
        print('FB')
    elif i % Fizz == 0:
        print('F')
    elif i % Buzz == 0:
        print('B')
    else:
        print(i)