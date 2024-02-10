class Product:
    def __init__(self, prod_name, prod_price, prod_category):
        self.name = prod_name
        self.price = prod_price
        self.category = prod_category
    
    #updates the product price, increases by percentage of is_increase is true and vice versa
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)

        return self

    def print_info(self):
        print(f"Product Details\nName: {self.name}\nPrice: {self.price}\nCategory: {self.category}")