import math

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math as m

array = range(1, 11, 1)
func_array = []
for x in array:
    func = (np.sqrt(1+pow(np.e, np.sqrt(x))+np.cos(pow(x, 2))))/(np.abs(1-pow(np.sin(x), 3))) + np.log(2*x)
    func_array.append(func)
print(array)
print(func_array)

#[5.798917496411, 9.89559082992602, 4.194572274398421, 3.9811767763428825, 4.092729058690511, 5.938653149530014,
# 8.115700200778333, 138.24401824876855, 7.917984524440516, 7.3440502300859265]

#Process finished with exit code 0
