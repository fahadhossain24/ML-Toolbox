import numpy as np
arr = np.array([20, 30, 40, 50, 60, 80])

# for i in arr:
#     print(i)

twoDarr = np.array([[2, 4, 5], [6, 7, 9]])

# for i in twoDarr:
#     for j in i:
#         print(j)

threeDarr = np.array([[[1, 3, 2], [3, 4, 2]], [[2, 4, 5], [6, 7, 9]]])

# for i in threeDarr:
#     for j in i:
#         for k in j:
#             print(k)

# for i in np.nditer(threeDarr):
#     print(i)


# for i in np.nditer(threeDarr, flags=['buffered'], op_dtypes='S'):
#     print(i)

# for i in np.nditer(twoDarr[:, ::2]):
#     print(i)

for idx, i in np.ndenumerate(threeDarr):
    print(idx, i)
    
    