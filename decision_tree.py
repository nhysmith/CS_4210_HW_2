#-------------------------------------------------------------------------
# AUTHOR: Nishara Hysmith
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

#dataSets = ['CS_4210_HW_2/contact_lens_training_1.csv']
dataSets = ['CS_4210_HW_2/contact_lens_training_1.csv', 'CS_4210_HW_2/contact_lens_training_2.csv', 'CS_4210_HW_2/contact_lens_training_3.csv']

for ds in dataSets:
    #print('File name: ' + ds)
    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)
                

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    temp = ['0']*4
    for i in dbTraining:
        for j in range(4):
            if i[j] == 'Young' or i[j] == 'Myope' or i[j] == 'Yes' or i[j] == 'Normal':
            #print(i[j])
                temp[j] = '1'
            elif i[j] == 'Prepresbyopic' or i[j] == 'Hypermetrope' or i[j] == 'No' or i[j] == 'Reduced':
                temp[j] = '2'
            elif i[j] == 'Presbyopic' :
                temp[j] = '3'
            else:
                temp[j] = '?'
        #print(temp)
        X.append(temp[:])

            
    #print(X)
    
    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for i in dbTraining:
        if i[4] == 'Yes':
            Y.append('1')
        elif i[4] == 'No':
            Y.append('2')
        else:
            print(i[4])
    #print(Y)

    #loop your training and test tasks 10 times here
    accuracyList = []
    for i in range (10):
        print('Iteration: ',i)
        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =
        dbTest = []
        with open('CS_4210_HW_2/contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append (row)
                    #print(row)
        #print(dbTest)
        temp = [0]*4
        #print('temp length: ', len(temp))
        TN, TP, FN, FP = 0,0,0,0
        #accuracyList = [0]*10
        for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
            print('Data: ', data)
            for j in range(4):
                if data[j] == 'Young' or data[j] == 'Myope' or data[j] == 'Yes' or data[j] == 'Normal':
                    temp[j] = '1'
                elif data[j] == 'Prepresbyopic' or data[j] == 'Hypermetrope' or data[j] == 'No' or data[j] == 'Reduced':
                    temp[j] = '2'
                elif data[j] == 'Presbyopic' :
                    temp[j] = '3'
                else:
                    print(data[j])
                    temp[j] = '?'
            print('Numeric: ',temp)
            class_predicted = clf.predict([temp])[0]
            print('Class predicted: ',class_predicted)
            print('Actual Class: ',data[4])

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
            if class_predicted == '1':
                if data[4] == 'Yes':
                    print('True positive')
                    TP+=1
                else:
                    print('False positive')
                    FP+=1
            else:
                if data[4] == 'No':
                    print('True negative')
                    TN+=1
                else:
                    print('False negative')
                    FP+=1
        
        print('TP = ',TP)              
        print('TN = ',TN)  
        print('FP = ',FP)  
        print('FN = ',FN)  

        accuracy = (TP + TN)/(TP + TN + FP + FN)
        print('Accuracy = ',accuracy)

        accuracyList.append(accuracy)
        print('List: ',accuracyList)
        
        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
    #print(accuracyList)
    lowestAccuracy = min(accuracyList)
    #print(lowestAccuracy)
    
    #print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    
    print('final accuracy when training on ' + ds + ':', lowestAccuracy)

    



    

 

       
   
