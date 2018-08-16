import pandas as pd											
import matplotlib.pyplot as plot
filePath = ("c://dataTest.csv")     # 读取文件路径，注：先将文件放进C盘根目录
dataFile = pd.read_csv(filePath,header=None, prefix="V")
target = []													
for i in range(200):											
    if dataFile.iat[i,10] >= 7:	        # iat 按位置对行列进行选择
        target.append(1.0)	            # 将 ≥7 的数据填入第 1 行
    else:
        target.append(0.0)		        # 将 ＜7 的数据填入第 0 行
                                        # 将数据分成两个部分
dataRow = dataFile.iloc[0:200,10]		# 提取需要处理的数据(前 200 行的第 10 个属性)
plot.scatter(dataRow, target)									
plot.xlabel("Attribute")										
plot.ylabel("Target")											
plot.show()	
