import pandas as pd
import numpy as np

# Reading the csv files for extracting features
coupon_list_test = pd.read_csv('../../dataset/coupon_list_test.csv')

# Altering Coupon List Test
# --------------------------------------------------------------------------------------------------------
print('\n\n\nALTERING COUPON LIST Test FILE --------------------------------')
coupon_list_test = coupon_list_test[['GENRE_NAME','PRICE_RATE','CATALOG_PRICE','DISCOUNT_PRICE',
										  'VALIDPERIOD','USABLE_DATE_MON', 'USABLE_DATE_TUE', 'USABLE_DATE_WED',
										  'USABLE_DATE_THU','USABLE_DATE_FRI', 'USABLE_DATE_SAT', 'USABLE_DATE_SUN',
										  'USABLE_DATE_HOLIDAY','USABLE_DATE_BEFORE_HOLIDAY', 'large_area_name',
										  'ken_name', 'small_area_name','COUPON_ID_hash']]

# Checking for NAN values in each colums
print('Length of dataframe: ', len(coupon_list_test))
print('GENRE_NAME: ',len(coupon_list_test['GENRE_NAME'].dropna()))
print('PRICE_RATE: ',len(coupon_list_test['PRICE_RATE'].dropna()))
print('CATALOG_PRICE: ',len(coupon_list_test['CATALOG_PRICE'].dropna()))
print('DISCOUNT_PRICE: ',len(coupon_list_test['DISCOUNT_PRICE'].dropna()))
print('VALIDPERIOD: ',len(coupon_list_test['VALIDPERIOD'].dropna()))
print('ken_name: ',len(coupon_list_test['ken_name'].dropna()))
print('small_area_name: ',len(coupon_list_test['small_area_name'].dropna()))
print('COUPON_ID_hash: ',len(coupon_list_test['COUPON_ID_hash'].dropna()),'\n\n')

# Removing NAN values in dataframe
coupon_list_test['USABLE_DATE_MON'] = coupon_list_test['USABLE_DATE_MON'].fillna(value=1)
coupon_list_test['USABLE_DATE_TUE'] = coupon_list_test['USABLE_DATE_TUE'].fillna(value=1)
coupon_list_test['USABLE_DATE_WED'] = coupon_list_test['USABLE_DATE_WED'].fillna(value=1)
coupon_list_test['USABLE_DATE_THU'] = coupon_list_test['USABLE_DATE_THU'].fillna(value=1)
coupon_list_test['USABLE_DATE_FRI'] = coupon_list_test['USABLE_DATE_FRI'].fillna(value=1)
coupon_list_test['USABLE_DATE_SAT'] = coupon_list_test['USABLE_DATE_SAT'].fillna(value=1)
coupon_list_test['USABLE_DATE_SUN'] = coupon_list_test['USABLE_DATE_SUN'].fillna(value=1)
coupon_list_test['USABLE_DATE_BEFORE_HOLIDAY'] = coupon_list_test['USABLE_DATE_BEFORE_HOLIDAY'].fillna(value=0)
coupon_list_test['USABLE_DATE_HOLIDAY'] = coupon_list_test['USABLE_DATE_HOLIDAY'].fillna(value=0)
coupon_list_test['VALIDPERIOD'] = coupon_list_test['VALIDPERIOD'].fillna(value=coupon_list_test['VALIDPERIOD'].mean())
print('VALIDPERIOD after altering: ',len(coupon_list_test['VALIDPERIOD'].dropna()))

usability = []
for i in range(len(coupon_list_test)):
	s = (coupon_list_test['USABLE_DATE_MON'][i] + coupon_list_test['USABLE_DATE_TUE'][i] + coupon_list_test['USABLE_DATE_WED'][i]  
		+ coupon_list_test['USABLE_DATE_THU'][i] + coupon_list_test['USABLE_DATE_FRI'][i] + coupon_list_test['USABLE_DATE_SAT'][i]  
		+ coupon_list_test['USABLE_DATE_SUN'][i] + coupon_list_test['USABLE_DATE_BEFORE_HOLIDAY'][i] + coupon_list_test['USABLE_DATE_HOLIDAY'][i])
	usability.append(s)

coupon_list_test['Usability'] = usability


coupon_list_test = coupon_list_test[['GENRE_NAME','PRICE_RATE','CATALOG_PRICE','DISCOUNT_PRICE',
										  'VALIDPERIOD','Usability', 'large_area_name',
										  'ken_name', 'small_area_name','COUPON_ID_hash']]
# --------------------------------------------------------------------------------------------------------



coupon_list_test.to_csv('../../Processed_data/test.csv')

