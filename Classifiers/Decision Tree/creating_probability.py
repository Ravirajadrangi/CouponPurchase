import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
import pickle
import csv


# Reading of the training and testing dataset
train_df = pd.read_csv('../../../processed_data/train.csv')
train_df = train_df.drop(train_df.columns[0], axis=1)
train_df = train_df.drop(['ITEM_COUNT','COUPON_ID_hash'], axis = 1)       
test_df = pd.read_csv('../../../processed_data/test.csv')
test_df = test_df.drop(test_df.columns[0], axis=1)
Coupons = list(test_df['COUPON_ID_hash'])
test_df = test_df.drop('COUPON_ID_hash', axis = 1)

#---------------------------------------------------------------------------------------------------------
# Altering the training dataset

# Altering the large area name 
large_area_name = list(set(train_df['large_area_name']))
# Altering the small area name 
small_area_name = list(set(train_df['small_area_name']))
# Altering the ken area name 
ken_name = list(set(train_df['ken_name']))
# Altering the genre name 
genre_name = list(set(train_df['GENRE_NAME']))

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
#---------------------------------------------------------------------------------------------------------

print 'Finished with altering dataset...'
DT = pickle.load(open('../../../Trained_Classifiers/decision_tree.sav', 'rb'))
print "Classifier loaded...."

with open('probability.csv', 'wb') as f:    # created a csv file for storing the probability of a user buying the coupons
	
	writer = csv.writer(f)
	
	temp_list = list(DT.classes_) # the classes are the users 
	temp_list.insert(0,'Coupons')  # added the name "Coupons" to the list of classes so that we can make it as a header
	writer.writerow(temp_list)    # writting the header
	print 'Written the header...'
	probability = DT.predict_proba(test_df)
	i = 0
	for user_probability in probability:
		user_probability = list(user_probability)
		user_probability.insert(0,Coupons[i]) # list of coupon number with the corresponding user probability
		writer.writerow(user_probability) 
		print 'Finished writting the value for couponID: ',Coupons[i],', Coupon Index: ',i,' in File probability.csv'
		i += 1









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
