#show user the items you have in your shop and let user decide how they want to filter that products
products = [
    {"name": "Laptop", "price": 65000, "category": "Electronics"},
    {"name": "Mouse", "price": 800, "category": "Electronics"},
    {"name": "Notebook", "price": 60, "category": "Stationery"},
    {"name": "Desk", "price": 5000, "category": "Furniture"},
]
print("======Welcome to the Aavash store=====")
print("\nThese are our prodeucts feel free to filter the product as you want")
print("""\n1. Show all products
2. Filter by max price
3. Sort by price
4. Search by name
5. Exit""")
choice=int(input("Enter the filter option you want:"))
if(choice==1):
    pass

elif(choice==2):
    max_price_user=int(input("Enter the max price you are looking for:"))
    result =filter(lambda x : x["price"] <= max_price_user, products)
    print(f'your sorted list is:\n{list(result)}')
    
    
elif(choice==3):
    result=sorted(products,key=lambda x: x["price"])
    print(f"your sorted list by price is:\n{result}")
    
    
elif(choice==4):
    name=input("\nEnter the name of the product:")
    name=name.capitalize()
    result=list(filter(lambda x:x['name']==name,products))
    
    if result:
        print(f"your sorted product {name} is:\n{result}")
    else:
        print("Item not found")
elif(choice==5):
    print("Thank you for your time")
else:
    print("Enter the vaild option")