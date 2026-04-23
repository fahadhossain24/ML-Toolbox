import numpy as np

# print(np.__version__)

arr = np.array([2, 4, 5, 6, 7, 8])

# print(arr)

# print(type(arr))

lst = [2, 4, 5, 6, 7, 8, 6]
tpl = (20, 30, 35, 50, 70, 30)
st = {3, 5, 7, 9, 11}
dic = {'1': 60, '2': 80, '3': 75, '4': 90}

lstToNdarr = np.array(lst)
tplToNdarr = np.array(tpl)
stToNdarr = np.array(st)
dicToNdarr = np.array(dic)
dicKeysToNdarr = np.array(dic.keys())
dicValuesToNdarr = np.array(dic.values())

# print(lstToNdarr)
# print(tplToNdarr)
# print(stToNdarr)
# print(dicToNdarr)
# print(dicKeysToNdarr)
# print(dicValuesToNdarr)

# print(type(lstToNdarr))
# print(type(tplToNdarr))
# print(type(stToNdarr))
# print(type(stToNdarr))


# 0-D Array
arr1 = np.array(40)
# print(arr1)


# 1-D Array - An array that has 0-D arrays as its element is called 1-D array
arr2 = np.array([2, 4, 5, 6, 7, 8])
# print(arr2)


# 2-D Array - An array that has 1-D arrays as its elements is called a 2-D array. ------ 2nd order tensor or Matrix
arr3 = np.array([
                [2, 4, 5], 
                [4, 5, 6], 
                [6, 7, 8]
])
# print(arr3)


# 2-D Array - An array that has 2-D arrays as its elements is called a 3-D array. ----- 3rd order tensor
arr4 = np.array([
                [
                [2, 4, 5], 
                [4, 5, 6], 
                [6, 7, 8]
                ],
                
                [
                [2, 4, 5], 
                [4, 5, 6], 
                [6, 7, 8]
                ],
                
                [
                [2, 4, 5], 
                [4, 5, 6], 
                [6, 7, 8]
                ]
])
# print(arr4)


# Number of array dimensions
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)
# print(arr4.ndim)


# Higher dimensional array

a = np.array([2, 4, 5, 6, 6, 0, 8], ndmin=5)

print(a)
print("number of dimension", a.ndim)


