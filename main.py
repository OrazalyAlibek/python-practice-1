customer_name = input("Enter customer name : ")
product_name = input("Enter product name : ")
price = float(input("Enter price per unit (KZT) : "))
quantity = int(input("Enter quantity : "))

subtotal = price * quantity
if subtotal > 5000:
    discount = subtotal * 0.1
else:
    discount = 0

total = subtotal - discount

print("="*30)
print("SHOP RECEIPT".center(30))
print("="*30)
print("Customer : ", customer_name)
print("Product : ", product_name)
print("Price : ", price, " KZT")
print("Quantity : ", quantity)
print("-"*30)
print("Subtotal : ", subtotal, " KZT")
print("Discount : ", discount, " KZT")
print("Total : ", total, " KZT")
print("="*30)

print("Discount applied : ", subtotal > 5000)
print("Paid more than 3000: ", total > 3000)
print("="*30)

