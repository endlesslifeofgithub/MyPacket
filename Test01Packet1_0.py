# 简单，01背包问题 可以寻找到全局最优解
import copy
import numpy as npy
cost=[2,2,6,5,4]
value=[6,3,5,4,6]
capacity=16
print("背包容量：",capacity)
answer=list((npy.array(range(capacity+1))*0))         #并不一定装满背包
#answer=list((npy.array(range(capacity+1))*0)+(-10000)) #必须恰好装满背包
answer[0]=0
lencost=len(cost)
temp=0
answerlist=[]
for i in range(lencost):
    tempvalue=list(reversed(list(range(cost[i],capacity+1))))
    for ii in tempvalue:
            answer[ii]=max(answer[ii],answer[ii-cost[i]]+value[i])
    answerlist.append(copy.deepcopy(answer))
answerlist=npy.array(answerlist)
tempvalue=list(reversed(list(range(lencost))))
packlist=[]
for i in tempvalue:
    if i==lencost-1:
        maxvalue=max(answerlist[i])
        print("最大价值：", maxvalue)
        pos=npy.where(answerlist[i]==maxvalue)[0][0]
    if maxvalue!=answerlist[i-1][pos]:
        packlist.append(i)
        pos=pos-cost[i]
        maxvalue=answerlist[i-1][pos]
if maxvalue==answerlist[0][pos]:
    packlist.append(0)
print("物品序号：", list(reversed(packlist)))
print("物品开销",list(cost[i] for i in list(reversed(packlist))))
print("物品价值",list(value[i] for i in list(reversed(packlist))))




