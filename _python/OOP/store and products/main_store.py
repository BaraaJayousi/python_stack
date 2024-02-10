from product import Product
from store import Store

main_store = Store("SwiftMart")

# Instantiate four products
product1 = Product("Laptop", 999.99, "Electronics")
product2 = Product("T-shirt", 19.99, "Clothing")
product3 = Product("Headphones", 79.99, "Electronics")
product4 = Product("Book", 15.99, "Books")

#add new products to the store
main_store.add_product(product1)
main_store.add_product(product2)
main_store.add_product(product3)
main_store.add_product(product4)

#show store's products
main_store.list_products()

#increaseing prices by 50%
main_store.inflation(.50)

main_store.list_products()

#decreasing products prices by 50% for electronics category
main_store.set_clearance("Electronics",0.60)

main_store.list_products()

#sold a product of id/index (1)
main_store.sell_product(1)

main_store.list_products()


