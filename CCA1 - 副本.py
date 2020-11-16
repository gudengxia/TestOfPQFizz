# 按照题目顺序读如文件，得到上述四个统计量之后，存储csv文件
import pandas as pd 
import numpy as np
import os

kexs = ['kyber768', 'saber', 'ntru677']
sigs = ['dilithium4']

algs = []
for kex in kexs:
    for sig in sigs:
        algs.append('p384_' + kex + '-' + 'p384_' + sig)

print(algs)


for alg in algs:
    path = './TestData/NIST3/' + alg +'_'+ delay
    path_list = os.listdir(path)
    path_list.remove('tm.avg')
    path_list.sort(key=lambda x: int(x.split('.')[0]+x.split('.')[1])) 
    per5list = []
    medianlist = []
    per95list =[]
    meanlist = []
            
    for filename in path_list:
        with open(os.path.join(path,filename)) as f:
            result = [int(x) for x in f]
            result_sorted = sorted(result)

    #5%分位数
    per5 = np.percentile(result_sorted,5)
    per5list.append(per5)

    #中位数
    median = np.median(result_sorted) 
    medianlist.append(median)

    #95%分位数
    per95 = np.percentile(result_sorted,95)
    per95list.append(per95)

    #5% 到 95% 平均数
    mean = np.mean(result)
    meanlist.append(mean)
   
    dataframe = pd.DataFrame({'per5':per5list,'median':medianlist,'per95':per95list,'mean':meanlist})
    f = './TestResult/NIST3/' + alg +'.csv'
    dataframe.to_csv(f,index=False,sep=',')
