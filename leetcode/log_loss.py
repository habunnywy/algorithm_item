from sklearn.metrics import log_loss
import numpy as np
def my_log_loss_sample(y_true_s,y_pred_s):
    loss=0
    for i,c in enumerate(y_true_s):
        loss-=c*np.log(y_pred_s[i])
    return loss

def my_log_loss(y_true,y_pred):
    loss=0
    for i,sample in enumerate(y_true):
        loss+=my_log_loss_sample(sample,y_pred[i])
    return loss/len(y_true)

y_true = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
y_pred_1 = [[0.3, 0.3, 0.4], [0.3, 0.4, 0.3], [0.1, 0.2, 0.7]]
y_pred_2 = [[0.1, 0.2, 0.7], [0.1, 0.7, 0.2], [0.3, 0.4, 0.3]]
print(log_loss(y_true, y_pred_1))
print(my_log_loss(y_true, y_pred_1))

print(log_loss(y_true, y_pred_2))
print(my_log_loss(y_true, y_pred_2))