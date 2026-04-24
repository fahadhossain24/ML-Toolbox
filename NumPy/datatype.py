import numpy as np

arr = np.array([20, 30, 40, 50, 60, 80])

# print(arr.dtype)


fruits_arr = np.array(['apple', 'banana', 'cherry'])

# print(fruits_arr.dtype)


arr1 = np.array([20, 30, 40, 50, 60, 80], dtype='S')
arr2 = np.array([20, 30, 40, 50, 60, 80], dtype='U')
# print(arr1)
# print(arr1.dtype)
# print(arr2)
# print(arr2.dtype)


# define size
a = np.array([1, 2, 3, 4], dtype='i4')

# print(a)
# print(a.dtype)

# up casting
b = np.array([1, 2, 3, True, '34', 20])

# print(b)
# print(b.dtype)


# Type conversion uisng astype
c = np.array([1.2, 45.3, 10.4, 3.4, 0.0, 8.3])

print(c)
print(c.dtype)

cvtToInt = c.astype('i')
cvtToStr = c.astype('U')
cvtTofloat = arr.astype(float)
cvtToBool = c.astype(bool)

print(cvtToInt)
print(cvtToInt.dtype)
print(cvtToStr)
print(cvtToStr.dtype)
print(cvtTofloat)
print(cvtTofloat.dtype)
print(cvtToBool)
print(cvtToBool.dtype)




