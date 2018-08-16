import numpy as np									
data = np.mat([[1,200,105,3,False],[2,165,80,2,False],
               [3,184.5,120,2,False],[4,116,70.8,1,False],[5,270,150,4,True]])	  

col1 = []					#coll生成了一个空的数据集
for row in data:			#采用for循环遍历data
    col1.append( row[0,1] ) #将data中的0行1列（即price）填充到coll中

print( np.sum(col1) )       #求和
print( np.mean(col1) )      #求均值
print( np.std(col1) )       #求标准差
print( np.var(col1) )       #求方差
