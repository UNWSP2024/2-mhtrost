
def average_age():
    # Get User Input
    age1 = float(input('what is your age?'))
    age2 = float(input('what is your age?'))
    age3 = float(input('what is your age?'))
    age4 = float(input('what is your age?'))
    
    # Sum ages
    result = age1 + age2 +age3 + age4
    print('Total age is', result)
    # Average the ages
    average_age = result/4
    # Print the results
    print('Your average age is', average_age)
# Line which calls the above function.
average_age()