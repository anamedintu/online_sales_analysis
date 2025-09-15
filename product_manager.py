
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

    def remove_product_by_name(self, name):
        """Remove all products that match the given name (case-insensitive)."""
        initial_count = len(self.products)
        self.products = [product for product in self.products if product.name.lower() != name.lower()]
        removed_count = initial_count - len(self.products)

        if removed_count > 0:
            print(f"{removed_count} product(s) named '{name}' have been removed.")
        else:
            print(f"No products named '{name}' were found.")
            
    def total_value(self):
        """Calculate the total value of all products."""
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of all products: {total:.2f} RON")