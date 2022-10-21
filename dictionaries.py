menus = {'Breakfast': ['eggs', 'sandwich', 'coffee'],
         'Lunch': ['rice and beans', 'rice and eggs', 'potatoes with salad'],
         'Dinner': ['soup', 'salad', 'taco']}

print('Breakfast Menu:\t', menus.get('Breakfast'))
print('Lunch Menu:\t', menus.get('Lunch'))
print('Dinner Menu:\t', menus.get('Dinner'))
print("")

for menu in menus:
    print(menu)

print("")

for menu, item in menus.items():
    print(menu, ':', item)

