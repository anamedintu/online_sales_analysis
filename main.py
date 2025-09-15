from product import Product
from product_manager import ProductManager

def main():
    # Cream instanta ProductManager
    manager = ProductManager()

    # Adaugam produse
    product1 = Product("Smartphone", 4500.0, 3)
    product2 = Product("Casti wireless", 150.0, 10)
    product3 = Product("Monitor LED", 800.0, 7)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

if __name__ == "__main__":
    main()