import random
from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    # Cream instanta ProductManager
    manager = ProductManager()

    # Adaugam produse
    product1 = Product("Laptop", 4500.0, 3)
    product2 = Product("Mouse wireless", 150.0, 10)
    product3 = Product("Monitor LED", 800.0, 5)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Afisam toate produsele
    print("\n Current inventory:")
    manager.display_all_products()

    # Afisam valoarea totala a inventarului
    print("\n Total value calculation:")
    manager.total_value()
    
    # Creare instanata Cart
    cart = Cart()

    # Selecteaza 3 produse aleatoriu din inventar
    selected_products = random.sample(manager.products, 3)

    # Adauga produsele selectate in cos
    for product in selected_products:
        cart.add_to_cart(product)

    # Afiseaza continutul cosului
    print("\n--- Cart Contents ---")
    cart.display_cart()

    # Afiseaza valoarea totala de plata
    print("\n--- Cart Total ---")
    cart.calculate_total()    

if __name__ == "__main__":
    main()