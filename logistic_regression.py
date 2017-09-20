import numpy as np
import pandas as pd
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle


train_df = pd.read_csv('../processed_data/train.csv')
test_df = pd.read_csv('../processed_data/test.csv')

train_df = train_df.drop(train_df.columns[0], axis=1)
test_df = test_df.drop(test_df.columns[0], axis=1)

train_df = train_df.drop(['Sex_ID','ITEM_COUNT','PURCHASEID_hash','AGE'], axis = 1)



lr = LogisticRegression()





'''
train_column = set(train_df.columns.tolist())
test_column = set(test_df.columns.tolist())
print(train_column,test_column)

# Saving the classifier
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

# Loading the classifier
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)

'''
