# Demonstrates string processing

full_name = input('Enter your first and last name:')

if full_name == '':
    print('You did not enter a name!')
else:
    space_pos = full_name.find(' ')
    if space_pos == -1:
        print('You did not enter your first and last name!')
    else:
        first_name = full_name[0:space_pos]
        print('Hello,' , first_name)

        last_name = full_name[space_pos + 1:len(full_name)]
        print('Or should I call you Mr.', last_name)


