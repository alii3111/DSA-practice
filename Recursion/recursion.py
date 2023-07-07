def recursion(number):
    if number <=0:
        print("DONE!")
    else:
        print(number)
        recursion(number - 1)
recursion(10)