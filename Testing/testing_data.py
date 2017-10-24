import numpy as np 
import pandas as pd 

detail_df = pd.read_csv('../../dataset/coupon_detail_train.csv')
visit_df = pd.read_csv('../../dataset/coupon_visit_train.csv')
user_df = pd.read_csv('../../dataset/user_list.csv')


print len(detail_df)
print len(detail_df.drop_duplicates())

print len(list(set(user_df['USER_ID_hash'])))
print len(list(set(visit_df['USER_ID_hash'])))
print len(list(set(detail_df['USER_ID_hash'])))



'''
detail_df = detail_df[['COUPON_ID_hash','USER_ID_hash']]
visit_df = visit_df[['VIEW_COUPON_ID_hash','USER_ID_hash','PURCHASEID_hash']]
visit_df = visit_df.dropna()
visit_df = visit_df[['VIEW_COUPON_ID_hash','USER_ID_hash']]

print('DETAIL DF: ',len(detail_df))
print('DETAIL DF WITHOUT DUPLICATES: ',len(detail_df.drop_duplicates()))

print('VISIT DF: ',len(visit_df))
print('VISIT DF WITHOUT DUPLICATES: ',len(visit_df.drop_duplicates()))

frames = [detail_df, visit_df]
combined_frames = pd.concat(frames)
print (list(combined_frames))
print('COMBINED DF: ',len(combined_frames))
print('COMBINED DF WITHOUT DUPLICATES: ',len(combined_frames.drop_duplicates()))
'''