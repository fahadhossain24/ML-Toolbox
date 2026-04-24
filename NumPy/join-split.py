import numpy as np

a = np.array([3, 4, 54, 2, 7])
b = np.array([9, 5, 59, 2, 8])

con_arr = np.concatenate((a, b))
# print(con_arr)


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

# print(arr)

# Joing using stack
stk_join = np.stack((a, b), axis=1)
stk_join1 = np.hstack((a, b)) # stacking along row called horizontal stack
stk_join2 = np.vstack((a, b)) # stacking along column called vartical stack
stk_join3 = np.dstack((a, b)) # stacking along depth
# print(stk_join3)


# Spliting

my_arr = np.array([2, 3, 4, 6, 3, 7, 8, 8, 80])
new_arr = np.array_split(my_arr, 3)
# print(new_arr)

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
threeDarr = np.array([[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]])

newarr = np.array_split(x, 3)
newarr1 = np.array_split(x, 3, axis=1)
newarr2 = np.hsplit(x, 2)
newarr3 = np.vsplit(x, 2)
newarr4 = np.dsplit(threeDarr, 2)

print(newarr)
print(newarr1)
print(newarr2)
print("column split or vertical split ", newarr3)
print("depth split ", newarr4)