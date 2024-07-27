#어쨌든 굴러가죠?
a=input()
b=input()
c=input()
if a.isnumeric():
    target=int(a)+3
    if target%3==0:
        if target%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif target%5==0:
        if target%3==0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(target)
elif b.isnumeric():
    target=int(b)+2
    if target%3==0:
        if target%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif target%5==0:
        if target%3==0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(target)
elif c.isnumeric():
    target=int(c)+1
    if target%3==0:
        if target%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif target%5==0:
        if target%3==0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(target)