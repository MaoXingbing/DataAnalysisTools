'''
KNN算法，分类问题思路如下：
    1.计算测试集和每个训练的样本之间的距离.
    2.基于距离进行升序排列.
    3．找到最近的K个样本.
    4.K个样本进行投票.
    5．票数多的结果，作为最终的预测结果.
代码实现思路：
    1.导包.
    2.准备数据集(测试集和训练集)
    3.创建(KNN分类模型)模型对象.
    4.模型训练.
    5．模型预测.
'''


#导包
from sklearn.neighbors import  KNeighborsClassifier

#准备数据集（测试集和训练集）
x_train=[[0],[2],[3],[1]]  #训练集
y_train=[1,0,3,4]
x_test=[[5]]  #测试集

#创建（KNN分类模型）模型对象
estimator=KNeighborsClassifier(n_neighbors=3)

#模型训练
estimator.fit(x_train,y_train)

#模型预测
y_pre=estimator.predict(x_test)

#输出预测
print(y_pre)