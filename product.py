# product.py

class Product:
    def __init__(self, name, price, quantity):
        self.name = name              
        self.price = price            
        self.quantity = quantity      

    def display_info(self):
        """Displays product information."""
        print(f"Product: {self.name}")
        print(f"Price: {self.price} RON")
        print(f"Available quantity: {self.quantity}")

    def update_quantity(self, amount):
        """
        Updates the product quantity.
        May add or subtract from stock.
        """
        self.quantity += amount
        print(f"Updated quantity: {self.quantity}")