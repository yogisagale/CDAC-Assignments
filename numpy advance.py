#1.	Write a NumPy program to reverse an array (first element becomes last).
import numpy as np
arr=np.array([2,3,6,5,6,46])
print(arr)
rever=arr[::-1]
print('reverse array')
print(rever)

#2.	Write a NumPy program to extract all odd numbers from an array.
import numpy as np
arr=np. array(range(1,100))
print("odd number ", arr[arr%2!=0])

#3.	Write a NumPy program to create a 2d array with 1 on the border and 0 inside.
import numpy as np
x = np.ones((5,5))
print("Given array:")
print(x)
print("on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)

#4.	Write a NumPy program to append values to the end of an array.
import numpy as np
x = [1, 2, 3]
print(x)
x = np.append(x, [[4, 5, 6], [7, 8, 9]])
print("After append values to the end of the array:")
print(x)

#5.	Write a NumPy program to compute the median of flattened given array.
import numpy as np
x = np.arange(10).reshape((2, 5))
print(x)
r1 =  np.median(x)
print("\nMedian of array:")
print(r1)

#6.	Write a NumPy program to find the most frequent value in an array.
import numpy as np
x = np.random.randint(0, 5, 20)
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())

#7.	Write a NumPy program to check two random arrays are equal or not
import numpy as np
x = np.random.randint(0,2,6)
print("First array:")
print(x)
y = np.random.randint(0,2,6)
print("Second array:")
print(y)
print("two random arrays are equal or not")
array_equal = np.allclose(x, y)
print(array_equal)


#8.	Write a NumPy program to get the powers of an array values element-wise.
import numpy as np
x = np.arange(7)
print(x)
print("powers of an array values element-wise:")
print(np.power(x, 3))


#9.	Write a NumPy program to add, subtract, multiply, divide arguments element-wise
import numpy as np
print("Add:")
print(np.add(1.0, 4.0))
print("Subtract:")
print(np.subtract(1.0, 4.0))
print("Multiply:")
print(np.multiply(1.0, 4.0))
print("Divide:")
print(np.divide(1.0, 4.0))

#10.Write a NumPy program to compute the multiplication of two given matrixes.
import numpy as np
p = [[1, 2], [3, 4]]
q = [[5, 6], [7, 8]]
result1 = np.dot(p, q)
print(result1)


#11.Write a NumPy program to Replace all odd numbers in arr with -1

import numpy as np
arr=np.arange(1,11)
print('The array is:',arr)
print('The array with odd numbers replaced with -1: ')
print(np.where(np.mod(arr,2)!=0,-1,arr))



#12.Replace all odd numbers in arr with -1 without changing arr

import numpy as np
arr1=np.arange(1,11)
print('The array is:',arr1)
arr2=np.where(np.mod(arr1,2)!=0,-1,arr1)
print('The new array with odd numbers replaced with -1: ',arr2)


#13.Convert a 1D array to a 2D array with 2 rows

import numpy as np
arr_1d=np.arange(8)
print("The dimension of array is:",arr_1d.ndim)
print("Array is:\n",arr_1d)
arr_2d=arr_1d.reshape(2,4)
print("The converted array is:\n",arr_2d)
print("The dimensions of the converted array:",arr_2d.ndim)


#14.Write a numpy program to swap two columns in a 2d numpy array?

import numpy as np
arr=np.arange(1,10).reshape(3,3)
print('The array is:')
print(arr)
arr[:,[1,2]]=arr[:,[2,1]]
print('The new array with swapped columns is:')
print(arr)


#15.Write a numpy program to swap two rows in a 2d numpy array?

import numpy as np
arr=np.arange(1,10).reshape(3,3)
print('The array is:')
print(arr)
arr[[1,2],:]=arr[[2,1],:]
print('The new array with swapped rows is:')
print(arr)

#16.Write a numpy program to reverse the rows of a 2D array?

import numpy as np
arr=np.arange(1,10).reshape(3,3)
print('The array is:')
print(arr)
arr[:]=arr[3::-1]
print('The array with reversed rows is:')
print(arr)

#17.Write a numpy program to reverse the columns of a 2D array?

import numpy as np
arr=np.arange(1,10).reshape(3,3)
print('The array is:')
print(arr)
arr[:,[0,2]]=arr[:,[2,0]]
print('The array with reversed columns is:')
print(arr)