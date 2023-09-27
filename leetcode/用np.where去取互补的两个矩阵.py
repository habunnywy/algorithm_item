import numpy as np
b=np.where([[True,False], [True,True]],
			 [[1,2], [3,4]],
             [[9,8], [7,6]])
"""
[[T F],[T T]]和T的地方由[[1,2],[3,4]]对应位置填充
F的地方由[[9,8],[7,6]]填充

"""

