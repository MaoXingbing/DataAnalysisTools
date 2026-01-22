from sklearn.linear_model import LinearRegression

x_train=[[160],[166],[172],[174],[180]]
y_train=[56.3,60.6,65.1,68.5,75]
x_test=[[176]]

estimat=LinearRegression()
estimat.fit(x_train,y_train)
print(f'权重:{estimat.coef_}')
print(f'偏置{estimat.intercept_}')
y_pre=estimat.predict(x_test)
print(y_pre)