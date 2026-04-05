def collatz(number):
    if number % 2 == 0:
        res = number // 2
        print(res)
        return res
    
    else:
        res = 3 * number + 1
        print(res)
        return res




def myFunction(num):
    response = collatz(num)
    while response != 1:
        response = collatz(response)


print(myFunction(55))