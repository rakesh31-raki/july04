# delete by value

items = [2.2, 'pam', 3, 4, 'pam', 5, 'pam', 'pam', 'pam', 'pam', .98]

item = 'pam'

while item in items:  # check for a element in list, membership test operator
    items.remove(item)
    print(items)

