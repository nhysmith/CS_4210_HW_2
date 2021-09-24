#-------------------------------------------------------------------------
# AUTHOR: Nishara Hysmth
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB

db = []

#reading the training data
#--> add your Python code here
with open('CS_4210_HW_2/weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#print(db)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
X = []
temp = [0]*5
for data in db:
    for j in range(5):
        if data[j] == 'Sunny' or data[j] == 'Hot' or data[j] == 'High' or data[j] == 'Strong':
            temp[j] = 1
        elif data[j] == 'Overcast' or data[j] == 'Mild' or data[j] == 'Normal' or data[j] == 'Weak':
            temp[j] = 2
        elif data[j] == 'Rain' or data[j] == 'Cool':
            temp[j] = 3
        else:
            #print(data[j])
            temp[j] = '?'
    #print(temp[1:5])    
    X.append(temp[1:5])
#print(X)
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
Y = []
for i in db:
    if i[5] == 'Yes':
        Y.append(1)
    elif i[5] == 'No':
        Y.append(2)
    else:
        print(i[5])
#print(Y)
    

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

dbTest = []
#reading the data in a csv file
#--> add your Python code here
with open('CS_4210_HW_2/weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTest.append (row)
#print(dbTest)

testData = []
temp = ['']*5
displayData = []
for data in dbTest:
    displayData.append(data[0:5])
    for j in range(5):
        if data[j] == 'Sunny' or data[j] == 'Hot' or data[j] == 'High' or data[j] == 'Strong':
            temp[j] = 1
        elif data[j] == 'Overcast' or data[j] == 'Mild' or data[j] == 'Normal' or data[j] == 'Weak':
            temp[j] = 2
        elif data[j] == 'Rain' or data[j] == 'Cool':
            temp[j] = 3
    #print(temp[1:5])
    #print(temp)
    testData.append(temp[1:5])
#print(displayData)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for (data, display) in zip(testData, displayData):
    #print(data)
    predicted = clf.predict_proba([data])[0]
    if predicted[0] >= .75:
        print(display, 'Yes'.ljust(15),predicted[0])
    elif predicted[1] >= .75:
        print(display,'No'.ljust(15),predicted[1])

        
    

