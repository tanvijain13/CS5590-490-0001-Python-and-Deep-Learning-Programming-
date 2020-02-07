import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
result=np.amax(a,axis=1,keepdims=True)

c=np.where(a==result,0,a)
print(c)





