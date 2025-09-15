from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        """Adauga o singura unitate din produs in cos."""
        single_item = Product(product.name, product.price, 1)
        self.cart_items.append(single_item)
        print(f"1 unit of '{product.name}' has been added to the cart.")

    def calculate_total(self):
        """Calculeaza valoarea totală a cosului."""
        total = sum(item.price * item.quantity for item in self.cart_items)
        print(f"Total cart value: {total:.2f} RON")
        return total

    def display_cart(self):
        """Afiseaza continutul cosului."""
        if not self.cart_items:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for item in self.cart_items:
                item.display_info()
                print("-" * 30)