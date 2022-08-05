def fizzbuzz(fizz, buzz, schmuzz):
    L = []
    for i in range(1, schmuzz + 1):
        if not i % fizz and not i % buzz:
            L.append("FB")
        elif not i % fizz:
            L.append("F")
        elif not i % buzz:
            L.append("B")
        else:
            L.append(str(i))
    return " ".join(L) + "\n"


file1 = "FizzBuzz.txt"
file2 = "Results.txt"

f1 = open(file1)
f2 = open(file2, 'w')

for string in f1:
    f, b, s = map(int, string.split())
    f2.write(fizzbuzz(f, b, s))

f1.close()
f2.close()