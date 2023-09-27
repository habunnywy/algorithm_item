"""


"""
import sys

import numpy as np

input_line_num=0
map_size0=0
map_size1=0
map=[]
for line in sys.stdin:
    input_line_num+=1
    a = line.split()
    if input_line_num==1:
        map_size0=int(a[0])
        map=[[] for _ in range(map_size0)]
    else:
        for i in a:
            map[input_line_num-2].append(int(i))
        if input_line_num==map_size0+1:
            break

map_size1=0
for row in map:
    if len(row)>map_size1:
        map_size1=len(row)
for row in map:
    if len(row)<map_size1:
        row.extend([1]*(map_size1-len(row)))
map=np.asarray(map)

class map_point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.avaliable_action_dict=[False,False,False,False]
        if x==0:
            None


def exist_route(l1,l2,index1):
    "从l1的index1点，是否存在从l1->l2的路，若存在则返回位于l2的出口index,否则返回-1"
    "上下的可能性"
    if l2[index1]==0 and l1[index1]==0:
        return True
    else:
        return False

def left_right_route(l,index):
    if l[index]!=0:
        return False
    if index==0:
        if l[1]==0:
            return True