import numpy as np

arr = np.array([20, 30, 40, 50, 60, 80])

# print(arr.shape)

arr1 = np.array([[20, 30, 40], [30, 40, 50], [40, 50, 60]])

# print(arr1.shape)

arr2 = np.array([20, 30, 40], ndmin=5)

# print(arr2.shape)


## Reshape

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

b = a.reshape(3, 4)
# print(b)

c = a.reshape(2, 2, 3)
d = a.reshape(2, 2, 3).base
# print(d)

unknownDim = a.reshape(2, 3, -1)
# print(unknownDim)

flatteningArr = arr1.reshape(-1) # base is view
flattenArr = arr1.flatten() # base is copy
print(flatteningArr)
print(flattenArr)