from db_logic_pkg.All_Products_DB import All_Products_DB 
from db_logic_pkg.Product_DB import Product_DB 

class All_Products_UI :
    

    def input_Product_Details(self):
        name = input("Enter Product name: ")
        unit_Price = float(input("How much is the price: "))
        quantity = int(input("How many would you like: "))



        
