list=[1,2,3,4,5,6,7,8,9]
print(list[4:8])
print(list[4:9])
print(list[4:])
print(list[1::2])
print(list[0::3])


def mom(a,b):
    return (a+b)
a=10
b=20
c=mom(a,b)
print(c)


def mom(a,b):
    print(a+b)
a=10
b=20
c=mom(a,b)
print(c)

if True:
    print("valid")
else:
    print("invalid")

if False:
    print("valid")
else:
    print("invalid")

try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    result = a+b
    print("sum:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
except ValueError:
    print("Invalid input! please enter a number.")
    
except Exception as e:
    print("An error occured:",e)
finally:
    print("Execution finished")
 

try:
    num=int(input("Enter first number: "))

    result =10/num
    print("result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
except ValueError:
    print("Invalid input! please enter a number.")
    
except Exception as e:
    print("An error occured:",e)
finally:
    print("Execution finished")
 

















