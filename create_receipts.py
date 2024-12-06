#The purpose of this project is to setup a program that keeps track of purchased items and produces a receipt.
#Items and prices
lovely_loveseat_desc = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
lovely_loveseat_price = 254.00
stylish_settee_desc = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
stylish_settee_price = 180.50
luxurious_lamp_desc = 'Luxurious Lamp. Glass and iron. 3 inches tall. Brown with cream shade.'
luxurious_lamp_price = 52.15

#Create the receipt and track items purchased
sales_tax = .088
customer_one_item_tot = round(254.00 + 52.15, 2)
customer_one_items = 'Lovely LoveSeat, Luxurious Lamp '
customer_one_tax = round(sales_tax * customer_one_item_tot, 2)
customer_one_purchase_tot = round(customer_one_tax + customer_one_item_tot, 2)

#Printing out the receipt
print('Customer Receipt')
print('Items: ', customer_one_items)
print('Item Total: $', customer_one_item_tot)
print('Sales Tax: $', customer_one_tax)
print('Total: $', customer_one_purchase_tot)