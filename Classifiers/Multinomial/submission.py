import numpy as np
import pandas as pd
import csv

probability_csv = pd.read_csv('probability.csv')
print "Finished reading the csv file ..."
coupon_list = list(probability_csv['Coupons'])
print(coupon_list[0])

temp_list = list(probability_csv)
temp_list.pop(0)
user_list = temp_list
j = 1 


with open('submission.csv', 'wb') as f:

	writer = csv.writer(f)
	writer.writerow(['USER_ID_hash','PURCHASED_COUPONS'])

	for users in user_list:

		print "Computing Sugggestions for User Index",j
		j +=1  
		main_list = list(probability_csv[users])  # list of probabilities of a user for different coupons
		max_value = main_list.index(max(main_list)) 
		writer.writerow([users,coupon_list[max_value]])

