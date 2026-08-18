cart=[]
one=(input("Enter your first item to the  cart:"))
cart.append(one)
two=(input("Enter your secound item to the cart:"))
cart.append(two)
three=(input("Enter your third item to the cart:"))
cart.append(three)
four=(input("Enter your forth item to the cart:"))
cart.append(four)
five=(input("Enter your fifth item to the cart:"))
cart.append(five)
print(f"Your cart list:{cart}")
print(f"YOUR first item:{cart[0]}")
print(f"Your last item{cart[-1]}")
print(f"your number of items:{len(cart)}")
if(input(f'Do you want to add one more item(y/n)'))=='y':
    add_item=input("Enter the item you want to add:")
    cart.append(add_item)
    print(f"item{add_item}addded successfully:")
    print(f"Your updated cart items are:{cart}")
else:
    print(f"Your final cart items are:{cart}")
if(input("Do you want to remove anthing from the cart(y/n):"))=='y':
    rmv=input("which item do you want to remove:")
    cart.remove(rmv)
    print(f"Your updated cart is:{cart}")
    print("=====Item removed sucessfully======")
    print(f"your final cart items are{cart}")
    print("Thank you for shopping with us")

else:
    print("Thank you for shopping with us")
print("=========================================")


