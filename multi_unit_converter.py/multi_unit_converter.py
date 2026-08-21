def multiply_1000(num):
    num=float(num*1000)
    return num

def divide_1000(num):
    
    num=float(num/1000)
    return num

def m_cm(num):
    num=float(num*1000)
    return num

def cm_m(num):
    num=float(num/1000)
    return num

def c_f(num):
    num = float((num * 9/5) + 32)
    return num

def f_c(num):
    num = float((num - 32) * 5/9)
    return num

def c_k(num):
    num=float(num+273.15)
    return num

def k_c(num):
    num=float(num-273.15)
    return num

def kg_lb(num):
    num=float(num*2.20462)
    return num

def lb_kg(num):
    num=float(num/2.20462)
    return num 
while True : #loop 1
    
    print("=====Welcome to unit conveter======\n")
    print("Please select the unit you want to convert:")
    while True: #loop 2
        ch=int(input('\n1.Length\n2.Temperature\n3.Mass\nchoice:'))
        if(ch==1):
            print("Please select the option below:")
            option=int(input("""\n1.km ➡️   m  
2.m  ➡️   km
3.m  ➡️   cm
4.cm ➡️   m
choice:"""))

            num=float(input("Enter the lenght you want to convert:"))
            if(option==1):
                result=multiply_1000(num)
                print(f'{result:.2f} m')
                break #break loop 1
                
            elif(option==2):
                result=divide_1000(num)
                print(f"{result:.2f} Km")
                break
                
            elif(option==3):
                result=m_cm(num)
                print(f"{result:.2f} cm")
                break
                
            else:
                result=cm_m(num)
                print(f"{result:.2f} m")
                break

        elif(ch==2):
            num=float(input("Enter the Temperature you want to convert:"))
            print("Please select the option below:")
            option=int(input("""\n1.c  ➡️   f    
2.f  ➡️   c
3.c  ➡️   k
4.k  ➡️   c
choice:"""))
            if(option==1):
                result=c_f(num)
                print(f"{result:.2f} F")
                break
                
            elif(option==2):
                result=f_c(num)
                print(f"{result:.2f} C")
                break
                
            elif(option==3):
                result=c_k(num)
                print(f"{result:.2f} K")
                break
                
            else:
                result=k_c(num)
                print(f"{result:.2f} C")
                break

        elif(ch==3):
            num=float(input("Enter the Mass you want to convert:"))
            print("Please select the option below:")
            option=int(input("""\n1.kg ➡️   g   
2.g  ➡️   kg
3.kg ➡️   lb
4.lb ➡️   kg
choice:"""))
            
            if(option==1):
                result=multiply_1000(num)
                print(f"{result:.2f} kg")
                break
                
            elif(option==2):
                result=divide_1000(num)
                print(f"{result:.2f} km")
                break
                
            elif(option==3):
                result= kg_lb(num)
                print(f"{result:.2f} lb")
                break
                
            else:
                result=lb_kg(num)
                print(f"{result:.2f}")
                break


        else:
            print("Enter a vaild number from the option above!(1/2/3)\n")
            break
          
    again=input("\nDo you want to convert again?(y/n):")
    
    if(again=='y'):
        continue
    elif(again=='n'):
        break
    else:
        print("!Enter a vaild choice(y/n)")
        
print("\n====Thank you======")