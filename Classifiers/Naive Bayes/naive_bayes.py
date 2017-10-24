import numpy as np
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
import pickle
import time

start_time = time.time()


# Reading of the training and testing dataset
train_df = pd.read_csv('../../../processed_data/train.csv')
train_df = train_df.drop(train_df.columns[0], axis=1)
train_df = train_df.drop(['ITEM_COUNT','COUPON_ID_hash'], axis = 1)       
test_df = pd.read_csv('../../../processed_data/test.csv')
test_df = test_df.drop(test_df.columns[0], axis=1)
test_df = test_df.drop('COUPON_ID_hash', axis = 1)

#---------------------------------------------------------------------------------------------------------
# Altering the training dataset

# Altering the large area name 
large_area_name = list(set(train_df['large_area_name']))
for area_name in large_area_name:
	train_df = train_df.replace(to_replace = area_name, value = large_area_name.index(area_name))

# Altering the small area name 
small_area_name = list(set(train_df['small_area_name']))
for area_name in small_area_name:
	train_df = train_df.replace(to_replace = area_name, value = small_area_name.index(area_name))

 # Altering the ken area name 
ken_name = list(set(train_df['ken_name']))
for area_name in ken_name:
	train_df = train_df.replace(to_replace = area_name, value = ken_name.index(area_name))


# Altering the genre name 
genre_name = list(set(train_df['GENRE_NAME']))
for name in genre_name:
	train_df = train_df.replace(to_replace = name, value = genre_name.index(name))


X = train_df.drop('USER_ID_hash', axis = 1)
Y = train_df['USER_ID_hash']

print 'altering of training data done ...'
#---------------------------------------------------------------------------------------------------------
# Altering the testing dataset

# Altering the large area name
for area_name in large_area_name:
	test_df = test_df.replace(to_replace = area_name, value = large_area_name.index(area_name))

# Altering the small area name
for area_name in small_area_name:
	test_df = test_df.replace(to_replace = area_name, value = small_area_name.index(area_name))

# Altering the ken area name
for area_name in ken_name:
	test_df = test_df.replace(to_replace = area_name, value = ken_name.index(area_name))

# Altering the genre name 
for name in genre_name:
	test_df = test_df.replace(to_replace = name, value = genre_name.index(name))

print 'altering of testing data done ...'	
#---------------------------------------------------------------------------------------------------------


NB = BernoulliNB()
print "fitting the classifier"
NB.fit(X,Y)
filename = '../../../Trained_Classifiers/naive_bayes.sav'
pickle.dump(NB, open(filename, 'wb'))



print 'Program Finished in: ',time.time() - start_time







'''
train_column = set(train_df.columns.tolist())
test_column = set(test_df.columns.tolist())
print(train_column,test_column)

# Saving the classifier


# Loading the classifier
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)

'''
