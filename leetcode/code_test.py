import numpy as np
Data_S2=[_ for _ in range(0,140)]
Labels_te=Data_S2[20:]
Xval=Data_S2[0:20]
for re in range(1,len(Labels_te)+1):
    if np.mod(re,10)==0 : print('Running testing trial={:1.0f}'.format(re))
    #testing trial
    Xte=Data_S2[20+(re-1):20+(re)]
    Xval=np.hstack((Xval,Xte))
    print(Xte)
    print(Xval)
