#导包
from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pdI
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  #分割训练集和测试集的
from sklearn.preprocessing import StandardScaler      #数据标准化的
from sklearn.neighbors import KNeighborsClassifier    #KNN算法分类对象
from sklearn.metrics import accuracy_score            #模型评估的，计算模型预测的准确率

from py_code.jiqixuexi.KNN import x_train, y_train


#查看数据集
def dm01_loadiris():
    #加载鸢尾花数据集
    iris_data = load_iris()
    #查看数据集
    print(f"数据集：{iris_data}")
    print(f'数据集的类型：{type(iris_data)}')
    #查看数据集的所有键
    print(f'数据集所有的键：{iris_data.keys()}')
    #查看数据集的键所对应的值
    print(f'具体的数据：{iris_data.data[:5]}')
    print(f'数据集的标签：{iris_data.target[:5]}')
    print(f'数据集的标签名称：{iris_data.target_names}')
    print(f'数据集的特征名称：{iris_data.feature_names}')
    #print(f'数据集的描述：{iris_data.DESCR}')
    # print(f'数据集的框架：{iris_data.frame}')
    # print(f'数据集的文件名：{iris_data.filename}')

def dem04():
    #获取数据集
    mydata=load_iris()
    #数据的基本处理
    x_train,x_test,y_train,y_test=train_test_split(mydata.data,mydata.target,test_size=2,random_state=23)
    #数据集的预处理-数据的标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    #让测试集的均值和方法，转换测试数据
    x_test=transfer.transform(x_test)
    #机器学习：模型训练
    estimator=KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)
    #模型评估
    myscore=estimator.score(x_test,y_test)
    print(f"myscore{myscore}")


    #模型预测
    print('通过模型查看分类类别->',estimator.classes_)
    mydata=[[4.5,5,6,0.6],
            [5,6,7,1.8]]
    mydata=transfer.transform(mydata)
    print(f'mydata:{mydata}')
    mypre=estimator.predict(mydata)
    print(f'mypre:{mypre}')
    mypre=estimator.predict_proba(mydata)
    print(f'mypre:{mypre}')





if __name__ == '__main__':
    #dm01_loadiris()
    dem04()