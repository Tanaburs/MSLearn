cont = input('Would you like to continue? ')

if cont == 'no' or cont == 'n':
    print('Exiting')
elif cont == 'yes' or cont == 'y':
    print('Continuing...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no')