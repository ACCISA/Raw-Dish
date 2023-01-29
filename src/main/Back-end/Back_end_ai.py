import numpy as np
import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

# gets the files
filename = "dataset.csv"
output = pandas.read_csv("output.csv")
output['result'] = np.NaN
neighbors = KNeighborsClassifier(2)
dlearn = pandas.read_csv(filename)
dlearn_submit = dlearn[dlearn['result'].isna()]

def AITrain():
        # imports the table

    # divides the big table into 2, the one to learn (dlearn) and the one to test (dlearn_submit)

    # creates X variable for both tables
    X = dlearn

    # creates the X and Y variables for the learning part
    Y1 = X['result']
    X1 = X.iloc[:, :-1]

    # implements the classifier, trains de AI and prints the f1 score for funsies
    neighbors.fit(X1, Y1)
    y_pred = neighbors.predict(X1)
    print(f1_score(Y1, y_pred, average='macro'))


def AIReturn():

    Y2 = output['result']
    X2 = output.iloc[:, :-1]

    # does the testing and casts to int
    Y2 = neighbors.predict(X2)
    Y2 = Y2.astype(int)

    # puts everything back together
    output['result'] = Y2

    return Y2
