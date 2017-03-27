# 多重背包问题 可以寻找到全局最优解
import copy
import numpy as npy
from Test01Packet1_0 import *

def reRangePack(cost,value,amount): #重新组织数据，将多重背包问题转化为01背包问题，采用log优化处理
    lenAmount=len(amount)
    ThingList=list(range(lenAmount))
    for i in range(lenAmount):
        costi=cost[i]
        valuei=value[i]
        amounti=amount[i]
        if amounti<=1:
            if amounti==1:
                amount[i]=0
            continue
        k=1             #消除原始数据的影响
        while amounti+1>pow(2,k):
            cost.append(costi*pow(2,k))
            value.append(valuei*pow(2,k))
            ThingList.append(i)
            k=k+1
        cost.pop()
        value.pop()
        ThingList.pop()
        cost.append(costi*(amount[i]-pow(2,k-1)+1))
        value.append(valuei*(amount[i]-pow(2,k-1)+1))
        ThingList.append(i)
        amount[i] = 0
    return(amount,ThingList,cost,value)

if __name__=='__main__':
    cost=[5,2,6,5,4]
    value=[6,3,8,4,6]
    amount=[1,1,2,1,1]
    capacity=14
    [amount,ThingList,cost,value]=reRangePack(cost,value,amount)
    [maxvalue,packlist]=simpleZeroOne(cost,value,capacity,1)
    if len(packlist) > 0:
        print("背包容量：", capacity)
        print("最大价值：", maxvalue)
        print("物品序号：", list(reversed(packlist)))
        print("物品开销", list(cost[i] for i in list(reversed(packlist))))
        print("物品价值", list(value[i] for i in list(reversed(packlist))))