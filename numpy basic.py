#1)Write a NumPy program to get the numpy version and show numpy build configuration.
import numpy as np
print(np.__version__)
print(np.show_config())

#2)Write a NumPy program to get help on the add function.
import numpy as np
print(help(np.add))

#3)Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
arr=np.array([1,1,0])
print("test whether none of the elements of a given array is zero:",np.all(arr))

#4)Write a NumPy program to test if any of the elements of a given array is non-zero.
import numpy as np
arr=np.array([0,0,0])
print("test whether none of the elements of a given array is zero:",np.any(arr))

#5)Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a
#Number).
import numpy as np
arr_without_nan_or_inf=np.array([1,2,3,4,5,6])
arr_with_nan_or_inf=np.array([1,2,3,np.nan,np.inf])
print("array 1:",arr_without_nan_or_inf)
print("array 2:",arr_with_nan_or_inf)
print("fitsness array 1:",np.isfinite(arr_without_nan_or_inf))
print("fitsness array 2:",np.isfinite(arr_with_nan_or_inf))

#6) Write a NumPy program to test element-wise for positive or negative infinity
arr=np.array([-np.inf,np.inf,5,6])
print(np.isposinf(arr))
print(np.isneginf(arr))

#7)Write a NumPy program to test element-wise for NaN of a given array
arr=np.array([-np.inf,np.inf,5,6,np.nan])
print(np.isnan(arr))

#8)Write a NumPy program to test element-wise for complex number, real number of a given array
#Also test if a given number is a scalar type or not.
arr=np.array([-np.inf,np.inf,5,6,np.nan,2+6j,np.complex(2,3)])
print(np.iscomplex(arr))
print(np.isreal(arr))
print(np.isscalar(arr))

#9)Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and
#less_equal) (of two given arrays
a=np.array([1,2,3,7])
b=np.array([4,5,6,7])
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

#10)Write a NumPy program to create an array of 10 zeros, an array of 10 ones, and an array of 10
#fives.
print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)*5)

#11)Write a NumPy program to create an array of the integers from 30 to70
print(np.arange(30,71))

#12)Write a NumPy program to create an array of all the even integers from 30 to 70
print(np.arange(30,71,2))

#13)Write a NumPy program to create a 3x3 identity matrix.
mx=np.identity(3)
print("3*3 matrix:")
print(mx)

#14)Write a NumPy program to generate a random number between 0 and 1.
ran_num=np.random.rand(1)
print(ran_num)


#15)Write a NumPy program to generate an array of 15 random numbers from a standard normal
#distribution
a=np.random.randn(15)
print(a)



#16)Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values
#except the first and last.

arr_vec=np.arange(15,56)
print("vector with values ranging from 15 to 55:",arr_vec)
print("vector with values ranging from 15 to 55:",arr_vec[1:-1])


#17)Write a NumPy program to create a vector of length 10 with values evenly distributed between
#5 and 50
print("vector of length 10 with values evenly distributed between5 and 50:",np.linspace(5,50,10))


#18)Write a NumPy program to multiply the values of two given vectors
v1=np.array([1,2,3])
v2=np.array([4,5,6])
v=np.multiply(v1,v2)
print("multiply the values of two given vectors is :",v)


#19)Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
a=np.arange(10,22).reshape(3,4)
print("3x4 matrix filled with values from 10 to 21")
print(a)

#20)Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal
#to 1, 2, 3, 4, 5.
print(np.diag([1,2,3,4,5]))

#21)Write a NumPy program to compute sum of all elements, sum of each column and sum of each
#row of an given array.
a=np.arange(10,22).reshape(3,4)
print(a)
print("sum of all elements, sum of each column and sum of each row of an given array.",np.sum(a))
