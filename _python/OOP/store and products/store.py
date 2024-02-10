class Store:
    def __init__(self, store_name):
        self.name = store_name
        self.products = []
    
    #Adds products to the store
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    #Sells product, indicated by removeing the product by providing products id (index in the list)
    def sell_product(self, id):
        sold_product = self.products.pop(id)
        sold_product.print_info()
        return self

    #make sure to not call these methods if the file is ran directly 
    if __name__ != "__main__":
        
        #increases products prices by the provided percentage
        def inflation(self, percent_increase):
            for product in self.products:
                product.update_price(percent_increase,True)
            return self
            
        #updates all the products matching the given category by reducing the price by the percent_discount 
        def set_clearance(self, category, percent_discount):
            for product in self.products:
                if product.category == category:
                    product.update_price(percent_discount, False)
            return self
        
        #prints store products
        def list_products(self):
            print(f"{self.name} Products:\n")
            for product in self.products:
                print(f"Name: {product.name}\t Price: {product.price}\t Category: {product.category}")