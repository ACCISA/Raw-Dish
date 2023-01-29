
def convertData(dataList):
    returnData = []
    for i in range(len(dataList)):
        if i == 0: # how has your day been today
            if dataList[i] == "Man":
                returnData[i] = 0
                continue
            if dataList[i] == "Woman":
                returnData[i] = 1
                continue
        if i == 1:
            if dataList[i] == "Good":
                returnData[i] = 0
                continue
            if dataList[i] == "Bad":
                returnData[i] = 1
                continue
        if i == 2:
            if dataList[i] == "Under 20$/person":
                returnData[i] = 0
                continue
            if dataList[i] == "Over 20$":
                returnData[i] = 1
                continue
        if i == 3:
            if dataList[i] == "Very":
                returnData[i] = 0
                continue
            if dataList[i] == "A little":
                returnData[i] = 1
                continue
        if i == 4 or i == 6:
            if dataList[i] == "Yes":
                returnData[i] = 0
                continue
            if dataList[i] == "No":
                returnData[i] = 1
                continue
        if i == 5:
            if dataList[i] == "35 or under":
                returnData[i] = 0
                continue
            if dataList[i] == "Over 35":
                returnData[i] = 1
                continue

        if i == 7:
            if dataList[i] == "Alone":
                returnData[i] = 0
                continue
            if dataList[i] == "Friends":
                returnData[i] = 1
                continue
            if dataList[i] == "Family":
                returnData[i] = 2
                continue
            if dataList[i] == "Lover":
                returnData[i] = 3
                continue
    return returnData

            
