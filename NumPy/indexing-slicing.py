import numpy as np

arr = np.array([3, 4, 23, 4, 23])

# print(arr[1])
# print(arr[1], arr[3])
# print(arr[1] + arr[3])


arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print(arr1[1, 4])


arr2 = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[1,2,3,4,5], [6,7,8,9,10]], [[1,2,3,20,5], [6,7,8,9,10]]])

# print(arr2)
# print(arr2[2, 0, 3])


# Negetive indexing

arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr1)
# print(arr1[0, -4])


# Slicing..............
a = np.array([1, 2, 3, 4, 5, 6, 7])

# print(a[2: 5])
# print(a[3: ])
# print(a[: 4])
# print(a[2:: 2])
# print(a[-5 : -1])


b = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print(b[0, 2:])
# print(b[0:2, 4])
# print(b[0:2, :4])

c = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[1,2,3,4,5], [6,7,8,9,10]], [[1,2,3,20,5], [6,7,8,9,10]]])

print(c[0:3, 1:, 1:3])
print(c[0:3, 0:, 1:4])
print(c[0:3, 0:, 3])
print(c[0:3, : , :])



