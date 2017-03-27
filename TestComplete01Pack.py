# 完全01背包问题 可以寻找到全局最优解
import copy
import numpy as npy
def complete01Pack(cost,value,capacity,mode,prevalue):
    #mode: 1 须把背包全部装满 ；0 不一定把背包全部装满 ；31 给初始背包设置值prevalue且需装满 ；30 给初始背包设置值prevalue无需装满
    if mode==0:
        answer=list((npy.array(range(capacity+1))*0)) #并不一定装满背包
    elif mode==1:
        answer=list((npy.array(range(capacity+1))*0)+(-10000)) #必须恰好装满背包
        answer[0] = 0
    elif(mode==31):
        answer=copy.deepcopy(prevalue[-1])
        mode=1
    elif (mode == 30):
        answer = copy.deepcopy(prevalue[-1])
        mode = 0
    else:
        print("Mode Select Error")
        raise Exception
    prevalue=list(prevalue)
    lencost=len(cost)
    answerlist=[]
    for i in range(lencost):
        for ii in range(cost[i],capacity+1):
            answer[ii]=max(answer[ii],answer[ii-cost[i]]+value[i])
        answerlist.append(copy.deepcopy(answer))
        prevalue.append(copy.deepcopy(answer))
    answerlist=npy.array(answerlist)
    tempvalue=list(reversed(list(range(lencost))))
    packlist=[]

    if mode == 1:
        maxvalue = answerlist[-1][-1]
        tempMaxValue = maxvalue
        if tempMaxValue < 0:
            print("无此方案")
            return ([],[],[])
        else:
            pos = capacity
            for i in tempvalue:
                if maxvalue != answerlist[i - 1][pos] and i >= 1:
                    while maxvalue == answerlist[i][pos - cost[i]] + value[i]:
                        maxvalue = maxvalue - value[i]
                        pos = pos - cost[i]
                        packlist.append(i)
                if i == 0 and maxvalue != 0:
                    while maxvalue == answerlist[i][pos - cost[i]] + value[i]:
                        maxvalue = maxvalue - value[i]
                        pos = pos - cost[i]
                        packlist.append(i)
            return (tempvalue,tempMaxValue, packlist)

    for i in tempvalue:
        if i==lencost-1:
            maxvalue=max(answerlist[i])
            tempMaxValue=maxvalue
            pos=npy.where(answerlist[i]==maxvalue)[0][0]
        if maxvalue!=answerlist[i-1][pos] and i>=1:
            while maxvalue==answerlist[i][pos-cost[i]]+value[i]:
                maxvalue=maxvalue-value[i]
                pos=pos-cost[i]
                packlist.append(i)
        if i == 0 and maxvalue != 0:
            while maxvalue == answerlist[i][pos - cost[i]] + value[i]:
                maxvalue = maxvalue - value[i]
                pos = pos - cost[i]
                packlist.append(i)
    return(prevalue,tempMaxValue,packlist)

if __name__=='__main__':
    cost=[2,3,3,6,7,3]
    value=[2,6,7,5,4,6]
    capacity=17
    [prevalue,MaxValue,packlist]=complete01Pack(cost,value,capacity,1,[])
    if len(packlist) > 0:
        print("背包容量：", capacity)
        print("最大价值：", MaxValue)
        print("物品序号：", list(reversed(packlist)))
        print("物品开销", list(cost[i] for i in list(reversed(packlist))))
        print("物品价值", list(value[i] for i in list(reversed(packlist))))