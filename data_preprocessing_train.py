import pandas as pd
import numpy as np

# Reading the csv files for extracting features
coupon_detail_train = pd.read_csv("../dataset/coupon_detail_train.csv")
coupon_list_train = pd.read_csv('../dataset/coupon_list_train.csv')
user_list = pd.read_csv("../dataset/user_list.csv")


# Altering Coupon Detail Train
# --------------------------------------------------------------------------------------------------------
print('\n\n\nALTERING COUPON DETAIL TRAIN FILE --------------------------------')
coupon_detail_train = coupon_detail_train[['ITEM_COUNT','PURCHASEID_hash',
										   'USER_ID_hash','COUPON_ID_hash']]

# Checking for NAN values in each colums
print('Length of dataframe: ', len(coupon_detail_train))
print('ITEM_COUNT: ',len(coupon_detail_train['ITEM_COUNT'].dropna()))
print('PURCHASEID_hash: ',len(coupon_detail_train['PURCHASEID_hash'].dropna()))
print('USER_ID_hash: ',len(coupon_detail_train['USER_ID_hash'].dropna()))
print('COUPON_ID_hash: ',len(coupon_detail_train['COUPON_ID_hash'].dropna()))										   
# --------------------------------------------------------------------------------------------------------


# Altering Coupon List Test
# --------------------------------------------------------------------------------------------------------
print('\n\n\nALTERING COUPON LIST Test FILE --------------------------------')
coupon_list_train = coupon_list_train[['GENRE_NAME','PRICE_RATE','CATALOG_PRICE','DISCOUNT_PRICE',
										  'VALIDPERIOD','USABLE_DATE_MON', 'USABLE_DATE_TUE', 'USABLE_DATE_WED',
										  'USABLE_DATE_THU','USABLE_DATE_FRI', 'USABLE_DATE_SAT', 'USABLE_DATE_SUN',
										  'USABLE_DATE_HOLIDAY','USABLE_DATE_BEFORE_HOLIDAY', 'large_area_name',
										  'ken_name', 'small_area_name','COUPON_ID_hash']]

# Checking for NAN values in each colums
print('Length of dataframe: ', len(coupon_list_train))
print('GENRE_NAME: ',len(coupon_list_train['GENRE_NAME'].dropna()))
print('PRICE_RATE: ',len(coupon_list_train['PRICE_RATE'].dropna()))
print('CATALOG_PRICE: ',len(coupon_list_train['CATALOG_PRICE'].dropna()))
print('DISCOUNT_PRICE: ',len(coupon_list_train['DISCOUNT_PRICE'].dropna()))
print('VALIDPERIOD: ',len(coupon_list_train['VALIDPERIOD'].dropna()))
print('ken_name: ',len(coupon_list_train['ken_name'].dropna()))
print('small_area_name: ',len(coupon_list_train['small_area_name'].dropna()))
print('COUPON_ID_hash: ',len(coupon_list_train['COUPON_ID_hash'].dropna()))

# Removing NAN values in dataframe
coupon_list_train['USABLE_DATE_MON'] = coupon_list_train['USABLE_DATE_MON'].fillna(value=1)
coupon_list_train['USABLE_DATE_TUE'] = coupon_list_train['USABLE_DATE_TUE'].fillna(value=1)
coupon_list_train['USABLE_DATE_WED'] = coupon_list_train['USABLE_DATE_WED'].fillna(value=1)
coupon_list_train['USABLE_DATE_THU'] = coupon_list_train['USABLE_DATE_THU'].fillna(value=1)
coupon_list_train['USABLE_DATE_FRI'] = coupon_list_train['USABLE_DATE_FRI'].fillna(value=1)
coupon_list_train['USABLE_DATE_SAT'] = coupon_list_train['USABLE_DATE_SAT'].fillna(value=1)
coupon_list_train['USABLE_DATE_SUN'] = coupon_list_train['USABLE_DATE_SUN'].fillna(value=1)
coupon_list_train['USABLE_DATE_BEFORE_HOLIDAY'] = coupon_list_train['USABLE_DATE_BEFORE_HOLIDAY'].fillna(value=0)
coupon_list_train['USABLE_DATE_HOLIDAY'] = coupon_list_train['USABLE_DATE_HOLIDAY'].fillna(value=0)
coupon_list_train['VALIDPERIOD'] = coupon_list_train['VALIDPERIOD'].fillna(value=coupon_list_train['VALIDPERIOD'].mean())
print('VALIDPERIOD after altering: ',len(coupon_list_train['VALIDPERIOD'].dropna()))

usability = []
for i in range(len(coupon_list_train)):
	s = (coupon_list_train['USABLE_DATE_MON'][i] + coupon_list_train['USABLE_DATE_TUE'][i] + coupon_list_train['USABLE_DATE_WED'][i]  
		+ coupon_list_train['USABLE_DATE_THU'][i] + coupon_list_train['USABLE_DATE_FRI'][i] + coupon_list_train['USABLE_DATE_SAT'][i]  
		+ coupon_list_train['USABLE_DATE_SUN'][i] + coupon_list_train['USABLE_DATE_BEFORE_HOLIDAY'][i] + coupon_list_train['USABLE_DATE_HOLIDAY'][i])
	usability.append(s)

coupon_list_train['Usability'] = usability


coupon_list_train = coupon_list_train[['GENRE_NAME','PRICE_RATE','CATALOG_PRICE','DISCOUNT_PRICE',
										  'VALIDPERIOD','Usability', 'large_area_name',
										  'ken_name', 'small_area_name','COUPON_ID_hash']]
# --------------------------------------------------------------------------------------------------------



# Altering User List
# --------------------------------------------------------------------------------------------------------
print('\n\n\nALTERING USER LIST FILE --------------------------------')
user_list = user_list[['SEX_ID','AGE','USER_ID_hash']]

# Checking for NAN values in each colums
print('Length of dataframe: ', len(user_list))
print('SEX_ID: ',len(user_list['SEX_ID'].dropna()))
print('AGE: ',len(user_list['AGE'].dropna()))
print('USER_ID_hash: ',len(user_list['USER_ID_hash'].dropna()),'\n\n')										   
# --------------------------------------------------------------------------------------------------------



purchased_coupons_train = coupon_detail_train.merge(coupon_list_train,
                                                 on='COUPON_ID_hash',
                                                 how='inner')

purchased_coupons_train = purchased_coupons_train.merge(user_list,
                                                on='USER_ID_hash',
                                                 how='inner')

purchased_coupons_train.to_csv('../processed_data/train.csv')

