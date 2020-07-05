mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat[1][1] = 'x'  # update an item

mat[2].append(10)  # to append an item to the row

del mat[0][1]    # to delete an item

mat.insert(2, [11, 22, 33])  # insert a row
print(mat)
print()

for row in mat:
    for col in row:
        print(col, end='\t')
    print()
