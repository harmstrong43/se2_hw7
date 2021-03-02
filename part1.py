def fizz(x):
    if(x % 3 == 0):
        return "Fizz"
    else:
        return str(x)
def buzz(x):
    if(x % 5 == 0):
        return "Buzz"
    else:
        return str(x)
def fizzbuzz(x):
    if((x % 3 == 0) and (x % 5 == 0)):
        return "FizzBuzz"
    else:
        return str(x)
def printer():
    for x in range(1,100):
        if(fizzbuzz(x) == str(x)):
            if(buzz == str(x)):
                print(fizz(x))
            else:
                print(buzz(x))
        else:
            print(fizzbuzz(x))
