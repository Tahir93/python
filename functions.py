#creating a parameter less function
num3 = 100
def add_1():    #parameter less function
    num1 = int(input("Enter first value "))
    num2 = int(input("Enter second value "))
    ans  = num1 + num2 + num3
    print(f"Answer = {ans}")

add_1()

#passing information as an argument
def add_2(number1, numbet2):  #number1/2 are funtion parameters
    print(number1 + numbet2)

#add_2(10,10)

