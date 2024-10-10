from product import product_name_list, product_price_list
from employee import employee_name_list, employee_job_title_list
from book import book_title_list, book_author_list
from university import university_name_list, university_location_list
from restaurant import restaurant_name_list, restaurant_cuisine_type_list

print("Product Data:")
for i in range(len(product_name_list)):
    print(f"Product Name: {product_name_list[i]}, Price: ${product_price_list[i]}")

print("\nEmployee Data:")
for i in range(len(employee_name_list)):
    print(f"Name: {employee_name_list[i]}, Job Title: {employee_job_title_list[i]}")

print("\nBook Data:")
for i in range(len(book_title_list)):
    print(f"Title: {book_title_list[i]}, Author: {book_author_list[i]}")

print("\nUniversity Data:")
for i in range(len(university_name_list)):
    print(f"Name: {university_name_list[i]}, Location: {university_location_list[i]}")

print("\nRestaurant Data:")
for i in range(len(restaurant_name_list)):
    print(f"Name: {restaurant_name_list[i]}, Cuisine Type: {restaurant_cuisine_type_list[i]}")
