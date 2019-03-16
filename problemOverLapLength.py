#!/usr/bin/py

import sys

def main():

    inputData = sys.stdin.readlines()
    count = 0
    listPairHolder = []
    for x in inputData:
        if count == 0:
            pairAmount = int(x)
        if count >= 1:
            listPairHolder.append(x.splitlines())
        count = count + 1
    handlePairs(listPairHolder)

def handlePairs(listPairHolder):
    count = 0
    listSinglePair = []
    for x in listPairHolder:
        count = count + 1
        listSinglePair.append(x)
        if count != 0:
            if count % 2 == 0:
                handleSinglePair(listSinglePair)
                del listSinglePair[:]
            


def handleSinglePair(singlePairList):
    x = singlePairList.pop(0)
    y = singlePairList.pop(0)
    
    strX = " ".join(x)
    strY = " ".join(y)

    if len(strX) > len(strY):
        length = len(strX)
        count = 0
        overlapGreater = 0
        i = 0
        j = 0
        while count < length:
            count = count + 1
            if strX[i: i +1] == strY[j: j +1]:
                overlapGreater = overlapGreater + 1
                i = i + 1
                j = j + 1
            if strX[i: i+1] != strY[j:j+1]:
                i = i +1
            if strX[0:1] == strY[0:1]:
                if strX[len(strX)-1:] != strY[len(strY)-1:]: 
                    overlapGreater = 0
                    break
        print(strX, " and ", strY, " have a overlap length of: ", overlapGreater)

    if len(strX) < len(strY):
        length = len(strY)
        count = 0
        overlapLess = 0
        i = 0
        j = 0
        while count < length:
            count = count + 1
            if strX[i: i +1] == strY[j: j +1]:
                overlapLess = overlapLess + 1
                i = i + 1
                j = j + 1
            if strX[i: i+1] != strY[j:j+1]:
                j = j + 1
            if strX[0:1] == strY[0:1]:
                if strX[len(strX)-1:] != strY[len(strY)-1:]:
                    overlapLess = 0
                    break
        print(strX, " and ", strY, " have a overlap length of: ", overlapLess)

    if len(strX) == len(strY):
        length = len(strX)
        count = 0
        overlapEqual = 0
        i = 0
        j = 0
        while count < length:
            count = count + 1
            if strX[i: i +1] == strY[j: j +1]:
                overlapEqual = overlapEqual + 1
                i = i + 1
                j = j + 1
            if strX[i: i+1] != strY[j:j+1]:
                    i = i +1
            if strX[0:1] == strY[0:1]:
                if strX[len(strX)-1:] != strY[len(strY)-1:]:
                    overlapEqual = 0
                    break
        print(strX, " and ", strY, " have a overlap length of: ", overlapEqual)
    return 

if __name__ == "__main__":
    main()




