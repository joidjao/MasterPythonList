class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_name_list = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet"]
product_price_list = [1200, 800, 150, 300, 600]

print("Product Data:")
for i in range(len(product_name_list)):
    print(f"Product Name: {product_name_list[i]}, Price: ${product_price_list[i]}")
