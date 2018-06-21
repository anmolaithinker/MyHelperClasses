def is_categorical(array_like):
  return array_like.dtype.name == 'object'  

class MachineLearning():
  
  def __init__(self,dataset):
    self.dataset = dataset
    print ('Functions : ')
    print '----------------------------------------------------'
    print 'For taking the updated dataset        : getDataSet()'
    print '----------------------------------------------------'
    print 'For Checking Null Percentage          : checkCounts()'
    print '----------------------------------------------------'
    print 'For checking Null Values              : checkNull()'
    print '----------------------------------------------------'
    print 'For Getting Out Unique Values         : uniqueValues(column)'
    print '----------------------------------------------------'
    print 'For drawing bargraph distribution     : drawDistribution(column)'
    print '----------------------------------------------------'
    print 'Label Encoding                        : LabelEncoder(X)'
    print '----------------------------------------------------'
    print 'Filling Null Values without Imputer   : FillNA(cols , filling_data)'
    print '----------------------------------------------------'
    print 'Filling Null Values with Imputer      : FillNAImputer(strategy , X)'
    print '----------------------------------------------------'
    print 'Train and Test Splitting              : traintestSplit(X , y)'
    print '----------------------------------------------------'
    print 'XGBoost                               : XGBoost(X_train , y_train)'
    print '----------------------------------------------------'
    print 'SVM                                   : SVM(X_train , y_train)'
    print '----------------------------------------------------'
    print 'GaussianNB                            : GaussianNB(X_train,y_train)'
    print '----------------------------------------------------'
    print 'CheckAccuracy                         : CheckAccuracy(X_test , y_test)'
    print '----------------------------------------------------'
    print 'ConfusianMatrix                       : ConfusianMatrix(y_test , y_pred)'
    
    
  
  def getDataSet(self):
    return self.dataset
  
  def checkCounts(self): 
    for i in self.dataset.columns:
      if(is_categorical(self.dataset[i])):   
        print 'Info of Column : ' + str(i)
        counts_without_null = self.dataset[i].value_counts().sum()
        null_counts = self.dataset[i].isnull().sum()
        print 'Counts Without Null : '
        print self.dataset[i].value_counts()
        print 'Null Counts  : '
        print null_counts
        print 'Null Percentage : ' + str(float((float(null_counts)/float(null_counts + counts_without_null)) * 100))
        print '------------------------------------------------------------'
      
  
  
  def checkNull(self):
    print self.dataset.isnull().sum()
    
    
  def uniqueValues(self , cols):
    print 'Unique Values of Column ' + str(cols) + ' :'
    print set(self.dataset[cols].values)
    print '-------------------------------------------'
    
    
  def drawDistribution(self , cols):
    print 'Drawing Distribution of Column ' + str(cols) + ' :'
    print  self.dataset[cols].value_counts().plot.bar()
    print '---------------------------------------------'
    
  def LabelEncoder(self , X):
    print 'Label Encoding Starts :'
    le = preprocessing.LabelEncoder()
    tranformed_x = le.fit_transform(X)
    print 'Classes : '
    print le.classes_
    print '---------------------------------------------'
    return tranformed_x
   
  
  def FillNA(self , cols , filling_data):
    self.dataset[cols] = self.dataset[cols].fillna(filling_data)
    print 'Done !!'
  
  def FillNAImputer(self , strategy , X):
    imputer = preprocessing.Imputer(strategy = strategy)
    X = imputer.fit_transform(X)
    print 'Done !'
    return X   
  
  
  def traintestSplit(self,X,y,test_size = 0.2 ,rs = 0):
    print 'Test Size : ' + str(test_size) + ' Random State : ' + str(rs)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    print 'Done!!'
    return (X_train , X_test , y_train , y_test)
  
  
  def XGBoost(self , X_train , y_train , max_depth = 3 , n_estimators = 100):
    classifier = XGBClassifier(max_depth = max_depth , n_estimators = n_estimators)
    classifier.fit(X_train,y_train)
    self.classifier = classifier
    print 'Done!!'
    return classifier
  
  def SVM(self,X_train,y_train,kernel,rs):
    self.classifier = SVC(kernel = kernel ,random_state = rs)
    self.classifier.fit(X_train,y_train)
    print 'Done !!'
    return self.classifier        
        
  def GaussianNB(self,X_train,y_train):
    self.classifier = GaussianNB()
    self.classifier.fit(X_train,y_train)
    print 'Done !!'
    return self.classifier
  
  def ConfusionMatrix(self,y_test,y_pred):
    cm = confusion_matrix(y_test, y_pred)
    print ("Confusion Matrix : \n" + str(cm))
    total = cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1]
    accurate = cm[0][0] + cm[1][1]
    print ("Accuracy : " + str(int(float(accurate/float(total))*100)))  
  
  
  def CheckAccuracy(self , X_test , y_test):
    y_pred = self.classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print cm
    print 'Accuracy : '
    correct = cm[0][0] + cm[1][1]
    total = cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]
    print str(float((float(correct) / float(total)) * 100))
    print '--------------------------------------------------' 
    return y_pred
  
  
  def NeuralNetwork(self , X_Train , y_train ,X_Test,y_test, batch_size ,  epochs):
    n = NN()
    n.InputLayer(15 , 10 , 'relu')
    n.HiddenLayer(5 , 'relu')
    n.Output(1 , 'sigmoid')
    n.Compile('binary_crossentropy' , 'adam' , 'accuracy')
    n.modelSummary()
    print 'Batch Size : ' + str(batch_size) + ' Epochs : ' + str(epochs)
    n.FitTrain(X_train,y_train,batch_size,epochs)
    y_pred = n.Predictions(X_Test) > 0.5
    self.ConfusionMatrix(y_test , y_pred)
    return (n,y_pred)      