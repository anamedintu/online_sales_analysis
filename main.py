from product import Product
from product_manager import ProductManager

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

if __name__ == "__main__":
    main()