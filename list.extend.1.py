products_list = ["galaxy a1", "galaxy a2", "note 8 pro", "galaxy a3"]

while(True):
    new_product = input("Enter new product: f to finish")
    if new_product == "f":
        break
    products_list.append(new_product)

print("product list is : ")
for product in products_list:
    print(product)
