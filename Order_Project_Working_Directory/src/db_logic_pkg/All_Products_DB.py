from db_logic_pkg.Product_DB import Product_DB  
import os

class All_Products_DB():
    def __init__(self):
        self.all_products = []
        self.file_path = Product_DB.file_path
        self.file_name = Product_DB.file_name

    def read_all_products(self):
        try:
            with open(self.file_path + self.file_name, "r") as f:
                for line in f:
                    name, unit_price, stock_quantity = line.strip().split(', ')
                    unit_price = float(unit_price)
                    stock_quantity = int(stock_quantity)
                    product = Product_DB(name, unit_price, stock_quantity)
                    self.all_products.append(product)
                    
        except Exception as e:
            print("Error: " + str(e))

    def save_all_products(self):
        try:
            with open(self.file_path + self.file_name, "w") as f:
                for product in self.all_products:
                    f.write(Product_DB.rec_template.format(product.name, product.unit_price, product.stock_quantity))
        except Exception as e:
            print("Error: " + str(e))
'''
# Example usage
all_products_db = All_Products_DB()

# Read all products from the file
all_products_db.read_all_products()

# Add new products
new_products = [Product_DB("Pencil", 5, 50), Product_DB("Marker", 7.5, 30)]
all_products_db.all_products.extend(new_products)

# Save all products to the file
all_products_db.save_all_products()

# Read all products again to verify
all_products_db.read_all_products()
for product in all_products_db.all_products:
    print(product.name, product.unit_price, product.stock_quantity)
'''