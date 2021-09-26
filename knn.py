#-------------------------------------------------------------------------
# AUTHOR: Nishara Hysmith
# FILENAME: knn.py
# SPECIFICATION: This program iterates through 10 data points and uses each point as a test instance and finds its 1NN, single nearest neighbor. 
#Using the nearest neighbor's class, the instance is classified. 
#The number of incorrect classifications are divided by the total number of classifications to find the error rate. Finally the error rate is displayed.

# FOR: CS 4210- Assignment #2
# TIME SPENT: 1hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('CS_4210_HW_2/binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

numIncorrect = 0
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):
    #print(instance)
    #print(i)

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    # X =
    X = []
    testInstance = db[i]
    testClassLabel = 0
    temp = ['', '']
    for j in db:
        if j != testInstance:
            temp = j[0:2]
            tempFloat = [float(i) for i in temp]
            #print(temp)
            X.append(tempFloat)
    #print('X: ', X)

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    # Y =
    Y = []
    for j in db:
        if j != db[i]:
            #print(j[2])
            if j[2] == '+':
                Y.append(float(1))
            else:Y.append(float(2))  
        else: 
            if j[2] == '+':
                testClassLabel = float(1)
            else:
                testClassLabel = float(2)
    #print('Y: ', Y)


    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =
    tempTestSample = testInstance[0:2]
    testSample = [float(i) for i in tempTestSample]
    #print('Sample: ',testSample)
    #print('Class: ',testClassLabel)

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]
    #print(class_predicted)

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    
    if class_predicted != testClassLabel:
        numIncorrect += 1
    
    
#print the error rate
#--> add your Python code here
#print(numIncorrect)

errorRate = numIncorrect/10

print('Error rate: ',errorRate)




