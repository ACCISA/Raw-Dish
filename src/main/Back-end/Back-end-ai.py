import numpy as np
import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

# gets the files
filename = "dataset.csv"
output = pandas.read_csv("output.csv")
output['result'] = np.NaN

# imports the table
dlearn = pandas.read_csv(filename)

# divides the big table into 2, the one to learn (dlearn) and the one to test (dlearn_submit)
dlearn_submit = dlearn[dlearn['result'].isna()]

# creates X variable for both tables
X = dlearn

# creates the X and Y variables for the learning part
Y1 = X['result']
X1 = X.iloc[:, :-1]

# implements the classifier, trains de AI and prints the f1 score for funsies
neighbors = KNeighborsClassifier(2)
neighbors.fit(X1, Y1)
y_pred = neighbors.predict(X1)
print(f1_score(Y1, y_pred, average='macro'))

Y2 = output['result']
X2 = output.iloc[:, :-1]

# does the testing and casts to int
Y2 = neighbors.predict(X2)
Y2 = Y2.astype(int)

output['result'] = Y2
print(output)

# exports the file as a zipzip in case we need it
compression_opts = dict(method='zip', archive_name='out.csv')
dlearn_submit.to_csv('out.zip', index=False, compression=compression_opts)
