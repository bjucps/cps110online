import random

colors = []
print("Enter 3 of your favorite colors:")
for i in range(3):
    color = input(f'Color #{i+1}:')
    colors.append(color)

if 'red' in colors:
    print('\nWow! I love red!')
else:
    num = random.randrange(len(colors))
    favcolor = colors[num]

    print(f'\nMy favorite is: {favcolor}')
