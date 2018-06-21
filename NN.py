class NN:
    def __init__(self):
      print 'Model Initialized :)' 
      self.model = Sequential()

    #input_dim: This is the size of the vocabulary in the text data. For example, if your data is integer encoded to values between 0-10, then the size of the vocabulary would be 11 words.
    #output_dim: This is the size of the vector space in which words will be embedded. It defines the size of the output vectors from this layer for each word. For example, it could be 32 or 100 or even larger. Test different values for your problem.
    #input_length: This is the length of input sequences, as you would define for any input layer of a Keras model. For example, if all of your input documents are comprised of 1000 words, this would be 1000.
    def EmbeddingLayer(self,input_dim,emb_dim,input_len = None):
        print('Input Dimension : ' + str(input_dim))
        print('Embedding Dimension : ' + str(emb_dim))
        print('Input Length : ' + str(input_len))
        self.model.add(Embedding(input_dim,emb_dim,input_length=input_len))
        print('Embedd Success')
        
    def Conv1D(self,n_filters,kernel,padding = 'valid'):
      self.model.add(Convolution1D(n_filters,kernel,padding = padding))
        
    # Flattening
    def Flatten(self):
      self.model.add(Flatten())
        
    # Input Layer
    def InputLayer(self,input_dim,output,activation):
      self.model.add(Dense(output, input_dim=input_dim,activation=activation,kernel_initializer='normal'))
      
      
    # Hidden Layer    
    def HiddenLayer(self,output,activation):
        self.model.add(Dense(output,activation=activation,kernel_initializer='normal'))
                    
    # Output Layer                   
    def Output(self,output,activation):
        self.model.add(Dense(output,activation=activation,kernel_initializer='normal'))
    
    def Compile(self,loss,opt,metr):
        self.model.compile(loss = loss , optimizer = opt , metrics = [metr]) 
        print("Successfully Compiled")
                        
    def modelSummary(self):
        print("Model Summary \n")
        print(self.model.summary())   
        
    def FitTrain(self , x_train , y_train , batch_size , epochs):
        self.model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs)
        
    def Predictions(self,x_test):
        return self.model.predict(x_test)
    
    def LSTM(self,output,return_sequences = False , drop_out = None):
        self.model.add(LSTM(output ,return_sequences = return_sequences , dropout = drop_out))
        
    def Tokenizer(self , max_features ,data,split = ' '):
        self.tokenizer = Tokenizer(num_words=max_features, split=split)
        self.tokenizer.fit_on_texts(data)
    
    def PadSequences(self,data):
        X = self.tokenizer.texts_to_sequences(data)
        #print ("Pad Seq. X : " + str(X))
        X = pad_sequences(X)
        return X    
