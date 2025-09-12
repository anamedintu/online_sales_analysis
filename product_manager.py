
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []  

    def add_product(self, product):
        """Add a product to the list"""
        self.products.append(product)
        print(f"Product '{product.name}' has been added.")

    def display_all_products(self):
        """Display information about all the products."""
        if not self.products:
            print("There are no available products")
        else:
            print("List of available products:")
            for product in self.products:
                product.display_info()
                print("-" * 30)

    def total_value(self):
        """Calculate the total value of all products."""
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of all products: {total:.2f} RON")