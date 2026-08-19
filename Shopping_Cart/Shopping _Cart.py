print("======Welcome to the Aavash Mart=====\n")
print("Here is your cart 🛒\n")
cart=[]
while True:
    ch=input("DO you want to add items in the cart(y/n):")
    ch=ch.lower()
    if(ch=='y'):
        item=input("\nEnter the name of item you want to add:")
        cart.append(item)
        print(f"=={item} Added Sucessfully===\n")
        print(f"Your cart contains{cart}\n")
        continue
    elif(ch=='n'):
        break
    else:
        print("Invalid choice,Enter either(y/n)")
        continue 
while True:
    if(len(cart)>0):
        ch=input("Do you want to remove anthing from the cart(y/n):")
        ch=ch.lower()
        if(ch=='y'):
            rmv=input("\nWhich item do you want to remove:")
            if (cart.count(rmv)>0):
                cart.remove(rmv)
                print(f"====={rmv} removed sucessfully======\n")
                print(f"Your updated cart is:{cart}")
                continue
            else:
                print("There is no such items in the cart!\n")
                print(f"Plz check the cart again and select what you want to remove:\n{cart}\n")
                continue
        elif(ch=='n'):
            print(f"Your final cart contains:{cart}\n")
            print(f"YOUR first item:{cart[0]}")
            print(f"Your last item:{cart[-1]}")
            print(f"Your number of items:{len(cart)}\n")
            break
        else:
            print("Invalid choice! Enter either(y/n)")
            continue
    else:
        break
print("\n\n====Thank you for shopping with us======\n")
            
            