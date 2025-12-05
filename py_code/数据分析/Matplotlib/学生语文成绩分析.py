import matplotlib.pyplot as plt
from requests_oauthlib.compliance_fixes import facebook_compliance_fix

score=[52, 93, 15, 72, 61, 21, 83, 87, 75, 75,
       88, 24, 36, 11, 5, 88, 26, 49, 93, 23,
       86, 95, 97, 8, 14, 44, 68, 6, 65, 13, 78,
       31, 29, 7, 47, 9, 69, 2, 94, 98, 63, 17,
       43, 41, 48, 86, 60, 58, 1, 8, 4, 12, 82,
       59, 100, 33, 73, 39, 27, 64, 32, 56, 79,
       16, 19, 30, 22, 76, 18, 53, 57, 91, 45,
       35, 74, 20, 85, 55, 37, 90, 67, 46, 92,
       89, 51, 77, 50, 34, 80, 96, 66, 25, 40,
       38, 81, 54, 28, 71, 99, 42]

plt.rcParams['font.sans-serif']=['SimHei']
plt.xlabel('分数')
plt.ylabel('学生数量')
plt.title('语文成绩分布直方图')

plt.hist(score,
         bins=range(0,100,5),
         facecolor='red',
         edgecolor='green')
plt.show()