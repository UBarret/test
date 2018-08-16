import pandas as pd											
import matplotlib.pyplot as plot									
filePath = ("c://dataTest.csv")     #读取文件路径，注：先将文件放进C盘根目录
dataFile = pd.read_csv(filePath,header=None, prefix="V")				
                                      #使用 pandas 自带的 read_csv 读取 csv 格式文件
dataRow1 = dataFile.iloc[100,1:300]	    #用 iloc 提取第 100 行中前 300 个数据
dataRow2 = dataFile.iloc[101,1:300]		#用 iloc 提取第 101 行中前 300 个数据
plot.scatter(dataRow1, dataRow2)		#绘制散点图
plot.xlabel("Attribute1")				#横纵轴为两个属性
plot.ylabel("Attribute2")										
plot.show()	

#数据在（0，0）的位置由较大的集合，表明属性再次的偏离程度较少，而几个特定点是偏离程度较大的点