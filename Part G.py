import math
list = {'ipad':int(519.00), 'Macbook':int(700.00), 'iphone':int(600.00), 'Samsung':int(400.000)}
print(list)

def student (x):
    student_price = x * 0.15
    student_price
    return student_price

def sales_tax_studentprice(x):
    sales_tax = x * 0.13
    return sales_tax

def sales_tax(x):
    sales = x * 0.13 
    return sales


menu = input('''
List of Items:
             
ipad
             
Macbook
             
iphone
             
Samsung
             
enter the name of an item: ''')

print('The cost of the item is', list[menu])

x = list[menu]

STD = input('Do you have a student price card?: ').lower

if STD == 'y' or 'yes':
    student(x)
    sales_tax_studentprice(x)
    total_cost_studentprice = student(x) + sales_tax_studentprice(x)
    print(menu, '$',x)
    print('Student Price', '$', student(x))
    print('Sales Tax', '$', sales_tax_studentprice)
    print('Total Cost', '$', total_cost_studentprice)

if STD == 'n' or 'no':
    sales_tax
    total_cost = sales_tax(x) + x 
    print(menu, '$',x)
    print('Sales Tax', '$', sales_tax(x))
    print('Total Cost', '$', total_cost)
