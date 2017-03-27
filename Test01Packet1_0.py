# 简单，01背包问题 可以寻找到全局最优解
import copy
import numpy as npy

def simpleZeroOne(cost,value,capacity,mode):
    if mode==0:
        answer=list((npy.array(range(capacity+1))*0)) #并不一定装满背包
    elif mode==1:
        answer=list((npy.array(range(capacity+1))*0)+(-10000)) #必须恰好装满背包
    else:
        print("Mode Select Error")
        raise Exception
    answer[0]=0
    lencost=len(cost)
    temp=0
    answerlist=[]
    for i in range(lencost):
        tempvalue=list(reversed(list(range(cost[i],capacity+1))))
        for ii in tempvalue:
                answer[ii]=max(answer[ii],answer[ii-cost[i]]+value[i])
        answerlist.append(copy.deepcopy(answer))
        #print(answer)
    answerlist=npy.array(answerlist)
    tempvalue = list(reversed(list(range(lencost))))
    packlist = []
    if mode==1:
        maxvalue=answerlist[-1][-1]
        tempMaxValue=maxvalue
        if tempMaxValue<0:
            print("无此方案")
            return([],[],[])
        else:
            pos=capacity
            for i in tempvalue:
                if maxvalue != answerlist[i - 1][pos]:
                    packlist.append(i)
                    pos = pos - cost[i]
                    maxvalue = answerlist[i - 1][pos]
            if maxvalue == answerlist[0][pos] and maxvalue>0:
                packlist.append(0)
            return (answerlist,tempMaxValue, packlist)
    for i in tempvalue:
        if i==lencost-1:
            maxvalue=max(answerlist[i])
            tempMaxValue=maxvalue
            pos=npy.where(answerlist[i]==maxvalue)[0][0]
        if maxvalue!=answerlist[i-1][pos]:
            packlist.append(i)
            pos=pos-cost[i]
            maxvalue=answerlist[i-1][pos]
    if maxvalue==answerlist[0][pos] and i==0:
        packlist.append(0)
    return(answerlist,tempMaxValue,packlist)

if __name__=='__main__':
    cost=[1,2,3,6,7,3]
    value=[2,6,7,5,4,6]
    capacity=17
    [lastIt,maxvalue,packlist]=simpleZeroOne(cost,value,capacity,0)
    if len(packlist)>0:
        print("背包容量：",capacity)
        print("最大价值：", maxvalue)
        print("物品序号：", list(reversed(packlist)))
        print("物品开销",list(cost[i] for i in list(reversed(packlist))))
        print("物品价值",list(value[i] for i in list(reversed(packlist))))