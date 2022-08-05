print("Input a number:")
number = int(input())
number = abs(number)

#digits
count = 1
number //= 10

while number > 0:
    number //= 10
    count += 1

print("Number of digits:", count)

#mulipliers
def multipliers(number: int):
    result = []
    string_number = str(number)
    for index, element in enumerate(string_number):
        result.append(f'{element}*10^{len(string_number) - index - 1}')
    return f'{string_number} = ' + (' + '.join(result))

print("\nInput a number:")
number = int(input())
print(multipliers(number))





