#The purpose of this project is to setup a program that keeps track of purchased items and produces a receipt.
#Items and prices
lovely_loveseat_desc: str = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
lovely_loveseat_price: float = 254.00
stylish_settee_desc: str = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
stylish_settee_price: float = 180.50
luxurious_lamp_desc: str = 'Luxurious Lamp. Glass and iron. 3 inches tall. Brown with cream shade.'
luxurious_lamp_price: float = 52.15

#Create the receipt and track items purchased
sales_tax: float = .088
customer_one_item_tot: float = round(254.00 + 52.15, 2)
customer_one_items: str = 'Lovely LoveSeat, Luxurious Lamp '
customer_one_tax: float = round(sales_tax * customer_one_item_tot, 2)
customer_one_purchase_tot: float = round(customer_one_tax + customer_one_item_tot, 2)

#Printing out the receipt
print('Customer Receipt')
print('Items: ', customer_one_items)
print('Item Total: $', customer_one_item_tot)
print('Sales Tax: $', customer_one_tax)
print('Total: $', customer_one_purchase_tot)