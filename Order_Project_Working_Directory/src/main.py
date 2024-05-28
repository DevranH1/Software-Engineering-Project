from ui.Order_mgt_UI import Order_mgt_UI
from ui.All_Products_UI import All_Products_UI

all_products = All_Products_UI()
all_products.input_a_product()
all_products.input_a_product()

is_updated =all_products.update_a_product()
print(is_updated)




'''
o_ui=Order_mgt_UI():
for order in o_ui.orders:
    print(str(order))
'''




         
#Remove an item
#order.remove_item(item1)
#order.display_order()

'''
password = input("Enter your password ")

password_len =len(password)

index=0
invalid = False

if password_len>2:
    while  (index < password_len) and not invalid:
        a= password[index]
        if index % 3 ==0:
            if a not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                invalid=True
        elif index % 3 == 1:
            if a not in "0123456789":
                invalid=True
        elif index % 3 == 2:
            if a not in "#_@-!":
                invalid =True
        index = index + 1
        if invalid:
            print ("Invalid password")
    if index==password_len and not invalid:
        print ("Valid password")
else:
    print ("Invalid password")   

'''