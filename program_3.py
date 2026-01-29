def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    item1 = float(input('Please scan item:'))
    item2 = float(input('Please scan item:'))
    item3 = float(input('Please scan item:'))
    item4 = float(input('Please scan item:'))
    item5 = float(input('Please scan item:'))

    result = item1 + item2 + item3 + item4 + item5
    print('Your total before tax is', result)

    print('sales tax is 7%')
    tax = result*0.07
    print('tax:', tax)

    total = tax + result
    print(f'your total is ${total:.2f}')


calculate_total_purchase()