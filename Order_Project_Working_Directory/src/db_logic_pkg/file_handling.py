import os

class FileHandler:
    def __init__(self, directory):
        self.directory = directory

    def read_file(self, filename):
        file_path = os.path.join(self.directory, filename)
        try:
            with open(file_path, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None

    def write_file(self, filename, data):
        file_path = os.path.join(self.directory, filename)
        try:
            with open(file_path, 'w') as file:
                file.write(data)
            print(f"Data has been written to '{filename}'.")
        except IOError:
            print(f"Error: Unable to write to '{filename}'.")

class ProductFileHandler(FileHandler):
    def __init__(self, directory):
        super().__init__(directory)

    def read_products(self):
        return self.read_file('Products.txt')

    def write_products(self, data):
        self.write_file('Products.txt', data)

class OrderFileHandler(FileHandler):
    def __init__(self, directory):
        super().__init__(directory)

    def read_orders(self):
        return self.read_file('Orders.txt')

    def write_orders(self, data):
        self.write_file('Orders.txt', data)

class OrderItemFileHandler(FileHandler):
    def __init__(self, directory):
        super().__init__(directory)

    def read_order_items(self):
        return self.read_file('Order_items.txt')

    def write_order_items(self, data):
        self.write_file('Order_items.txt', data)

class CustomerFileHandler(FileHandler):
    def __init__(self, directory):
        super().__init__(directory)

    def read_customers(self):
        return self.read_file('Customers.txt')

    def write_customers(self, data):
        self.write_file('Customers.txt', data)
