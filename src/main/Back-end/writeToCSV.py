import csv
import pandas

# with open("output.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     print(row)
def writeToOutput(fieldList):

    headers = ['gender','mood','dollarinos','last_meal','surprise','age','origin','romantic','result']
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for i in range(len(fieldList)):
            fieldList[i] = " " + str(fieldList[i])
        writer.writerow(fieldList)