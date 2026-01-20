num=int(input("Enter no: "))

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)
x= fact(5)
print(f"factorial of {num} is {x}")