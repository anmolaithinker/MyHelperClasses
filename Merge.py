import pandas as pd

# Merge row wise
def mergeRow_wise(all_files):
    df = pd.read_csv(all_files[0])
    for file in range(1,len(all_files)):
        dataframe = pd.read_csv(all_files[file])
        df.append(dataframe)
    print 'Shape : ' + str(df.shape)
    print df.head(3)

def mergeCol_wise(all_files):
    

import glob
all_files = glob.glob('./Valid/*')
mergeRow_wise(all_files)
