import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, confusion_matrix
import seaborn as sns



def confusion_table(true_labels,pre_labels,cls_name):
    """
    true_labels:真实标签,即ground_truth
    pre_labels:预测结果
    cls_name:各类名
    """
    assert len(pre_labels.shape) in [1,2]
    if len(pre_labels.shape)==2:
        predicted_probabilities=pre_labels
        pre_labels=np.argmax(pre_labels, axis=1)
    label_len=len(true_labels)
    assert label_len==len(pre_labels)
    true_cls=np.unique(true_labels)
    pre_cls=np.unique(pre_labels)
    for label in pre_cls:
        assert label in true_cls,f"{label} not found in true_labels"

    # 混淆矩阵计算与绘制
    con_table= confusion_matrix(true_labels, pre_labels)
    plt.figure(figsize=(8,8))
    ax=sns.heatmap(con_table,annot=True,cmap='Blues',fmt='g',xticklabels=cls_name,yticklabels=cls_name,\
                cbar=False,annot_kws={"fontsize":18}) #fmt设置数值的格式化形式
    ax.tick_params(axis='both',which='major',labelsize=14)
    #plt.xlabel('Predicted label')
    #plt.ylabel('True label')
    plt.title('Confusion matrix',fontsize=20)
    plt.show()

    # 绘制ROC
    if len(pre_labels.shape)==1:
        predicted_probabilities=np.zeros((label_len,len(true_cls)))
        for i,t_l in enumerate(true_cls):
            cls_index=np.where(pre_cls==t_l)[0][0]
            predicted_probabilities[i][cls_index]+=1

    fpr=dict()
    tpr=dict()
    roc_auc=dict()
    for i,cls in enumerate(true_cls):
        fpr[i],tpr[i],_=roc_curve(true_labels==cls,predicted_probabilities[:,i])
        roc_auc[i]=auc(fpr[i],tpr[i])
    plt.figure(figsize=(8,6))
    for i in range(len(true_cls)):
        plt.plot(fpr[i],tpr[i],label=cls_name[i]+' AUC:{:.2f}'.format(roc_auc[i]))
    plt.plot([0,1],[0,1],'k--',label='Chance level')
    plt.xlabel('FPR',fontsize=12)
    plt.ylabel('TPR',fontsize=12)
    plt.title('ROC curve ', fontsize=20)
    plt.legend(loc='lower right')
    plt.show()

    #kappa值和acc计算(acc即po)
    po,pe=0,0
    for i in range(len(true_cls)):
        po+=con_table[i][i]
        pe+=np.sum(con_table[i])*np.sum(con_table[:,i])
    po/=label_len
    pe/=(label_len*label_len)
    kappa=(po-pe)/(1-pe)

    return con_table,kappa


if __name__=='__main__':
    class_names = ['hands', 'shoulders', 'wrists']
    true_labels =      np.array([1, 0, 2, 0, 1, 2, 0, 1, 2, 1])
    predicted_labels = np.array([1, 0, 1, 0, 0, 2, 0, 1, 2, 1])

    con_tabl,kappa=confusion_table(true_labels,predicted_labels,class_names)
    print(con_tabl,kappa)



