import numpy as np									
import pylab										
import scipy.stats as stats	#scipy是专门的机器学习的数据处理包

data = np.mat([[1,200,105,3,False],[2,165,80,2,False],
               [3,184.5,120,2,False],[4,116,70.8,1,False],[5,270,150,4,True]])	  

col1 = []						#价格合集
for row in data:										
    col1.append( row[0,1] )

stats.probplot(col1,plot=pylab)	#probplot计算了coll数据集中数据在正态分布下的偏离程度
pylab.show()			
