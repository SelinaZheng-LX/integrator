def integrate():
    function = input("Input function: ")
    a = float(input("Input a value: "))
    b = float(input("Input b value: "))
    n = int(input("Input n value: "))
    sub = float(b - a)
    delta_x = float(sub/n)
    sum = 0
    choose = input("type l for Aleft and r for Aright: ")
    while not choose == "l" and not choose =="r":
                print("That is not an option, please choose again: ")
                choose = input("type l for Aleft and r for Aright: ")
    if choose == "l":
        for i in range(0,n+1,1):
            f = lambda x: eval(function)
            y = f(a + delta_x * i)
            sum = sum + y * delta_x
    else:
        for i in range(0,n,1):
            f = lambda x: eval(function)
            y = f(a + delta_x * i)
            sum = sum + y * delta_x    
    print ("The answer is:", sum)
    print("You have integrated!")
if __name__ == "__main__":
    integrate()
