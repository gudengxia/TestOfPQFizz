# 按照题目顺序读如文件，得到上述四个统计量之后，存储csv文件
import pandas as pd 
import numpy as np
import os

delays = ['1']
kexs = ['ntru509']
sigs = ['dilithium2', 'falcon512']

algs = []
for kex in kexs:
    for sig in sigs:
        algs.append(kex + '_' + sig)
print(algs)

for delay in delays:
    for alg in algs:
        path = './TestData/AUTH/' + alg +'_'+ delay
        path_list = os.listdir(path)
        path_list.remove('tm.avg')
        #path_list.sort(key=lambda x: int(x.split('.')[0]+x.split('.')[1])) 
        path_list.sort(key=lambda x: int(x.split('.')[0]) )
       
        dic = dict()     
        for filename in path_list:
            with open(os.path.join(path,filename)) as f:
                result = [int(x) for x in f]
                result_sorted = sorted(result)
                dic[filename] = result_sorted[0:4995]
            
        dataframe = pd.DataFrame.from_dict(dic)
        
        #dataframe = pd.DataFrame({'per5':per5list,'median':medianlist,'per95':per95list,'mean':meanlist})
        f = './TestResult/AUTH/CD/' + alg + '_' + delay +'.csv'
        dataframe.to_csv(f,index=False,sep=',')
