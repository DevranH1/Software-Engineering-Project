import os

class Product_DB:
    file_path = "." + os.sep + 'data_files' + os.sep
    file_name = 'products.txt'
    rec_template = '{:50}, {:10.2f}, {:5d}\n'
    rec_length = 68  # Adjusted length for the fixed record format

    def __init__(self, name, unit_price, stock_quantity):
        self._name = name
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def save(self):
        try:
            if not os.path.exists(Product_DB.file_path):
                os.makedirs(Product_DB.file_path)
                
            if not os.path.isfile(Product_DB.file_path + Product_DB.file_name):
                with open(Product_DB.file_path + Product_DB.file_name, 'x') as f:
                    pass
            
            with open(Product_DB.file_path + Product_DB.file_name, "a") as f:
                f.write(Product_DB.rec_template.format(self.name, self.unit_price, self.stock_quantity))
                
        except Exception as e:
            print("Error: " + str(e))
    
    @staticmethod
    def read_product(offset: int, bytes: int):
        try:
            with open(Product_DB.file_path + Product_DB.file_name, "r") as f:
                f.seek(offset)
                record = f.read(bytes)
                if not record:
                    return None
                
                name, unit_price, stock_quantity = record.split(', ')
                unit_price = float(unit_price)
                stock_quantity = int(stock_quantity)
                return Product_DB(name.strip(), unit_price, stock_quantity)
                
        except Exception as e:
            print("Error: " + str(e))
            return None

    def update_this_product_in_file(self) -> bool:
        try:
            offset = 0
            file_size = os.path.getsize(Product_DB.file_path + Product_DB.file_name)
            
            with open(Product_DB.file_path + Product_DB.file_name, "r+") as f:
                while offset < file_size:
                    f.seek(offset)
                    record = f.read(Product_DB.rec_length)
                    if not record:
                        break
                    
                    name, _, _ = record.split(', ')
                    if name.strip() == self.name:
                        f.seek(offset)
                        f.write(Product_DB.rec_template.format(self.name, self.unit_price, self.stock_quantity))
                        return True
                    
                    offset += Product_DB.rec_length
                    
        except Exception as e:
            print("Error: " + str(e))
        
        return False

    def __str__(self):
        return f'{self.name:20}, {self.unit_price:5.2f}, {self.stock_quantity:5d}\n'

# Example usage
products = [Product_DB("Pen", 10, 100), Product_DB("Eraser", 5.6787, 10)]
for a_product in products:
    a_product.save()

# Reading the first product from the file
a_product = Product_DB.read_product(offset=0, bytes=Product_DB.rec_length)
if a_product:
    print(a_product.name)  # should print Pen
    print(a_product.unit_price)  # should print 10
    print(a_product.stock_quantity)  # should print 100

# Update the product
a_product.unit_price = 12.34
a_product.stock_quantity = 120
a_product.update_this_product_in_file()

# Reading the updated product from the file
updated_product = Product_DB.read_product(offset=0, bytes=Product_DB.rec_length)
if updated_product:
    print(updated_product.name)  # should print Pen
    print(updated_product.unit_price)  # should print 12.34
    print(updated_product.stock_quantity)  # should print 120
