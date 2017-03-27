import numpy as npy
from MultiplePackP03 import *
from TestComplete01Pack import *

def MixPack(cost,value,amount,capacity,mode):
    [amount, ThingList, cost, value] = reRangePack(cost, value, amount) #利用log优化方法将多重背包物件转化为01背包问题物件
    lenamount=len(amount)
    lencost=len(cost)
    completecost=[]
    completevalue=[]
    completeThingList=[]
    tempcost=[]
    tempValue=[]
    tempThinglist=[]
    for i in range(lenamount):
        if amount[i]<0:
            completecost.append(cost[i])
            completevalue.append(value[i])
            completeThingList.append(i)
        else:
            tempcost.append(cost[i])
            tempValue.append(value[i])
            tempThinglist.append(ThingList[i])
    for i in range(lenamount,lencost):
        tempcost.append(cost[i])
        tempValue.append(value[i])
        tempThinglist.append(ThingList[i])

    [ListTemp,tempMaxValue, packlist]=simpleZeroOne(tempcost, tempValue, capacity, mode) #调用前01背包问题将多重背包问题解决
    if mode==0:
        mode=30
    elif mode==1:
        mode=31
    [listStep,tempMaxValue, packlist]=complete01Pack(completecost, completevalue, capacity, mode, ListTemp)
    maxvalue=tempMaxValue
    answerlist = npy.array(listStep)
    tempvalue = list(reversed(list(range(lencost))))
    thinglist=[]
    costlist=[]
    valuelist=[]
    if mode==1:
        maxvalue = answerlist[-1][-1]
        tempmax = maxvalue
        if tempMaxValue < 0:
            print("无此方案")
            return ([], [], [],[],[])
        else:
            pos = capacity
            for i in tempvalue:
                if maxvalue == 0 and i != 0:
                    break
                if lencost - i <= len(completecost):
                    if maxvalue != answerlist[i - 1][pos]:
                        while maxvalue == answerlist[i][pos - completecost[i - lencost]] + completevalue[i - lencost]:
                            maxvalue = maxvalue - completevalue[i - lencost]
                            pos = pos - completecost[i - lencost]
                            thinglist.append(completeThingList[i - lencost])
                            costlist.append(completecost[i - lencost])
                            valuelist.append(completevalue[i - lencost])
                else:
                    if maxvalue != answerlist[i - 1][pos]:
                        thinglist.append(tempThinglist[i])
                        costlist.append(tempcost[i])
                        valuelist.append(tempValue[i])
                        pos = pos - tempcost[i]
                        maxvalue = answerlist[i - 1][pos]
                    if maxvalue == answerlist[0][pos] and i == 0:
                        thinglist.append(tempThinglist[0])
                        costlist.append(tempcost[0])
                        valuelist.append(tempValue[0])
            return (tempmax, thinglist, costlist, valuelist)


    for i in tempvalue:
        if maxvalue==0 and i!=0:
            break
        if lencost-i<=len(completecost):
            if i==tempvalue[0]:
                tempmax=maxvalue
                pos = npy.where(answerlist[i] == tempmax)[0][0]
            if maxvalue!=answerlist[i-1][pos]:
                while maxvalue==answerlist[i][pos-completecost[i-lencost]]+completevalue[i-lencost]:
                    maxvalue=maxvalue-completevalue[i-lencost]
                    pos=pos-completecost[i-lencost]
                    thinglist.append(completeThingList[i-lencost])
                    costlist.append(completecost[i-lencost])
                    valuelist.append(completevalue[i-lencost])
        else:
            if maxvalue != answerlist[i - 1][pos]:
                thinglist.append(tempThinglist[i])
                costlist.append(tempcost[i])
                valuelist.append(tempValue[i])
                pos = pos - tempcost[i]
                maxvalue = answerlist[i - 1][pos]
            if maxvalue == answerlist[0][pos] and i==0:
                thinglist.append(tempThinglist[0])
                costlist.append(tempcost[0])
                valuelist.append(tempValue[0])
    return(tempmax,thinglist,costlist,valuelist)



if __name__=='__main__':
    cost=[2,3,4,6,7,5]
    value=[6,5,5,4,6,6]
    amount=[1,3,-1,4,5,-1]  #-1 代表此件物品的数量是不受限制的
    capacity=15
    [maxvalue,thinglist,costlist,valuelist]=MixPack(cost, value, amount, capacity,0)
    if len(costlist) > 0:
        print("背包容量：", capacity)
        print("最大价值：", maxvalue)
        print("物品序号：",thinglist )
        print("物品开销", costlist)
        print("物品价值", valuelist)