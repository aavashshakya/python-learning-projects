def add(*add_list):
    total=0
    for i in add_list:
        total+=i
    return total

def sub(*add_list):
    total=0
    for i in add_list:
        total-=i
    return total
    
def multiply(*add_list):
    total=1
    for i in add_list:
        total*=i
    return total
    
def divide(*add_list):
    total=add_list[0]
    for i in add_list[1:]:
        total=float(total/i)
    return total

add_list=[]

while True:

    num=int(input("Enter a number you want to deal with:"))
    add_list.append(num)
    option=input("\nDo you want to more number(y/n):")

    if(option=='y'):
        continue

    elif(option=='n'):
        break

    else:
        print("Enter a valid option:")
    
while True:
    print(f"Your list of numbers:{add_list}")
    print("\n1.addition\n2.subtraction\n3.Multiplication\n4.Division\n")
    ch=int(input("what do you want to perform:"))

    if(ch==1):
        print("\n=====Welcome to the  Addition:======")
        total=add(*add_list)
        print(f"Your addition of {add_list}is:{total}") 
        break

    elif(ch==2):
        print("\n=====Welcome to the Subtraction:======")
        total=sub(*add_list)
        print(f"Your Subtraction of {add_list}is:{total}") 
        break
        

    elif(ch==3):
        print("\n=====Welcome to the Multiplication:======")
        total=multiply(*add_list)
        print(f"Your Multipliction of {add_list}is:{total}") 
        break

    elif(ch==4):
        print("\n=====Welcome to the  Divsion :======")
        total=divide(*add_list)
        print(f"Your Division of {add_list}is:{total:.2f}") 
        break

    else:
        print("Invalid! Enter the given option only(1/2/3/4)")
        continue


