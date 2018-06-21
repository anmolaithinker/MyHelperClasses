from google.colab import files  
import zipfile

# Importing Modules
import numpy as np
import pandas as pd
import io
import os
import re
from keras.preprocessing import sequence
from keras.models import Sequential
import numpy as np
from keras.layers import Flatten,Masking
from keras.layers.recurrent import LSTM
from keras.layers.core import Activation
from keras.layers.wrappers import TimeDistributed 
from keras.preprocessing.sequence import pad_sequences
from keras.layers.embeddings import Embedding
from sklearn.cross_validation import train_test_split
from keras.layers import Merge ,  Bidirectional , Dense
from keras.backend import tf
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB




class GoogleColabHelper():

  def __init__(self):
    print 'Initializing Google Helper : '
    print 'Helper Functions That you can use : '
    print '---------------------------------------------------------------------'
    print 'To Upload Files from local system to colab : - UploadFilesFromLocal()'
    print '---------------------------------------------------------------------'
    print 'To Download Files                          : - downloadFile(path)'
    print '---------------------------------------------------------------------'
    print 'Getting Data From URL                      : - getDataFromUrl(url)'
    print '---------------------------------------------------------------------'
    print 'Unzip                                      : - Unzip(path , directory)'
    print '---------------------------------------------------------------------'
    print 'Download and Install Glove                 : - DownAndInstallGlove(directory)'
    print '---------------------------------------------------------------------'


  ## Uploading files from Local  
  def UploadFilesFromLocal(self):
    global files
    uploaded = files.upload()
    for fn in uploaded.keys():
      print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
    
  ## Downloading the file  
  def downloadFile(self,path):
    global files
    files.download(path)
  
  ## Getting data from URL
  def getDataFromUrl(self , url):
    print "Getting Data From Url"
    os.system('wget ' + str(url))
    print "Done !!"
    os.system('ls')
  
  ## Unzipping the file
  def Unzip(self , path , directory):
    zip_ref = zipfile.ZipFile(path, 'r')
    zip_ref.extractall(directory)
    zip_ref.close()  
    print('Done!!')
    os.system('ls')
    
  ## Download and Install Glove  
  def DownAndInstallGlove(self , directory):
    curr = !ls
    print("Current Directory : \n" + str(curr))
    print("---------------------------Downloading : ")
    !wget = 'http://nlp.stanford.edu/data/glove.6B.zip'
    print("---------------------------Extracting : ")
    zip_ref = zipfile.ZipFile('./glove.6B.zip', 'r')
    zip_ref.extractall(directory)
    zip_ref.close()
    print "Done !!!"
    os.system('ls')
    
