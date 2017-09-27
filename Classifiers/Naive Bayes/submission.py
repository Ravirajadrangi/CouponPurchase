import numpy as np
import pandas as pd
import csv

probability_csv = pd.read_csv('probability.csv')
print "Finished reading the csv file ..."
coupon_list = list(probability_csv['Coupons'])


temp_list = list(probability_csv)
temp_list.pop(0)
user_list = temp_list
j = 1 


with open('../../../Submission_Files/submission_Naive_bayes.csv', 'wb') as f:

	writer = csv.writer(f)
	writer.writerow(['USER_ID_hash','PURCHASED_COUPONS'])

	for users in user_list:

		print "Computing Sugggestions for User Index",j
		j +=1  

		main_list = list(probability_csv[users]) 
		temp_list = list(probability_csv[users]) 
	 
		temp_list.sort()
		temp_list = temp_list[len(temp_list)-10:len(temp_list)]
	
		string = ""

		for values in temp_list:	

			if string == "":
				string = coupon_list[main_list.index(values)] 
			else:
				string = string+" "+coupon_list[main_list.index(values)]
			
 
		writer.writerow([users,string])

