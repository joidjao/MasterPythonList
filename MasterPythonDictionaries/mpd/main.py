from product.product import print_products
from employee.employee import print_employees
from books.books import print_books
from university.university import print_universities
from restaurant.restaurant import print_restaurants

def main():
    print_products()
    print()
    print_employees()
    print()
    print_books()
    print()
    print_universities()
    print()
    print_restaurants()

if __name__ == "__main__":
    main()