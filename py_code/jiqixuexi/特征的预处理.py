from sklearn.preprocessing import MinMaxScaler,StandardScaler


#归一化
x_train=[[90,2,10,40],[60,4,15,45],[75,3,13,46]]

# transfer=MinMaxScaler()
#参数：feature_range：指定归一化的范围，默认为(0,1)
transfer=MinMaxScaler(feature_range=(0,1))

#对原数据集进行归一化操作
x_train_transfer=transfer.fit_transform(x_train)
print("归一化后的数据为：\n")
print(x_train_transfer)



#标准化
transfer_standard=StandardScaler()
x_train_standard=transfer_standard.fit_transform(x_train)
print("标准化后的数据为：\n")
print(x_train_standard)
print("均值为：\n")
print(transfer_standard.mean_)
print("方差为：\n")   #方差计算公式：该列的每个值减去该列的均值，再平方，求和，再除以该列的元素个数
print(transfer_standard.var_)
print("数据集的标准差：\n") #标准差计算公式：方差开平方根
print(transfer_standard.scale_)