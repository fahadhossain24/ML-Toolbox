import numpy as np

 # copy
arr = np.array([20, 30, 40, 50, 60, 80])

# print(arr)

cpArr = arr.copy()

cpArr[1] = 50

arr[1] = 60
# print(arr)
# print(cpArr)

 # view
arr1 = np.array([20, 30, 40, 50, 60, 80])

# print(arr1)

vwArr = arr1.view()

vwArr[1] = 50
# print(arr1)


arr1[1] = 60
# print(vwArr)



# check by base attribute
a = arr.copy()
b = arr.view()

print(a.base)
print(b.base)