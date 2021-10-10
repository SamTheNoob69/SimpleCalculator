import time
first = (int(input("First number: ")))

while True:
    sym = input("Symbol:")
    signs = '-+*/'
    string = 'string*'
    if sym not in signs:
        print(f"{sym} is not a symbol.")
    else:
        break

second = (int(input("Second number: ")))

if sym == "-":
    a = first - second
    print(a)
elif sym == "+":
    b = first + second
    print(b)
elif sym == "*":
    c = first * second
    print(c)
elif sym == "/":
    d = first // second
    print(d)

time.sleep(5)
