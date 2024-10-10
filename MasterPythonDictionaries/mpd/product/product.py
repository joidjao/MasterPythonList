products = [
    {"product_name": "Laptop", "price": 1000},
    {"product_name": "Smartphone", "price": 800},
    {"product_name": "Tablet", "price": 500},
    {"product_name": "Headphones", "price": 150},
    {"product_name": "Monitor", "price": 300}
]

def print_products():
    print("Products:")
    for product in products:
        print(f"Product Name: {product.get('product_name')}, Price: ${product.get('price')}")
