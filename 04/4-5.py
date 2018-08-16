import pandas as pd					#导入必要的模块
import matplotlib.pyplot as plot									
rocksVMines = pd.DataFrame([[1,200,105,3,False],[2,165,80,2,False],
               [3,184.5,120,2,False],[4,116,70.8,1,False],[5,270,150,4,True]])
                                        #创建 DataFrame 对象
dataRow1 = rocksVMines.iloc[1,0:3]		# iloc 按位置进行提取
dataRow2 = rocksVMines.iloc[2,0:3]								
plot.scatter(dataRow1, dataRow2, c='b',marker='*')	    # plot.scatter(X, Y) 绘制散点图，X,Y 的数据长度一样
plot.xlabel("Attribute1")				#设置X轴标签
plot.ylabel(("Attribute2"))			#设置Y轴标签
plot.show()								#显示所画的图

dataRow3 = rocksVMines.iloc[3,0:3] 							
plot.scatter(dataRow2, dataRow3, c='r',marker='x')
plot.xlabel("Attribute2")										
plot.ylabel("Attribute3")										
plot.show()	
