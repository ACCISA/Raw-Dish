
def convertData(dataList):

    print(dataList[0])
    for i in range(len(dataList)):
        if i == 0: # how has your day been today
            if dataList[i] == "Man":
                dataList[i] = 0
                continue
            elif dataList[i] == "Woman":
                dataList[i] = 1
                continue
        if i == 1:
            if dataList[i] == "Good":
                dataList[i] = 0
                continue
            if dataList[i] == "Bad":
                dataList[i] = 1
                continue
        if i == 2:
            if dataList[i] == "Under 20$/person":
                dataList[i] = 0
                continue
            if dataList[i] == "Over 20$":
                dataList[i] = 1
                continue
        if i == 3:
            if dataList[i] == "Very":
                dataList[i] = 0
                continue
            if dataList[i] == "A little":
                dataList[i] = 1
                continue
        if i == 4 or i == 6:
            if dataList[i] == "Yes":
                dataList[i] = 0
                continue
            if dataList[i] == "No":
                dataList[i] = 1
                continue
        if i == 5:
            if dataList[i] == "35 or under":
                dataList[i] = 0
                continue
            if dataList[i] == "Over 35":
                dataList[i] = 1
                continue

        if i == 7:
            if dataList[i] == "Alone":
                dataList[i] = 0
                continue
            if dataList[i] == "Friends":
                dataList[i] = 1
                continue
            if dataList[i] == "Family":
                dataList[i] = 2
                continue
            if dataList[i] == "Lover":
                dataList[i] = 3
                continue
    return dataList

            
