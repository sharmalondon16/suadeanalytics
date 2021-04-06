# module to load csv data into pandas dataframes

import pandas as pd
import datetime

# load data from csv files
df_orders = pd.read_csv('.\source\\orders.csv',  delimiter =',')  
df_commissions = pd.read_csv('.\source\\commissions.csv',  delimiter =',')  
df_order_lines = pd.read_csv('.\source\\order_lines.csv',  delimiter =',')  
df_product_promotions = pd.read_csv('.\source\\product_promotions.csv',  delimiter =',')  
df_promotions = pd.read_csv('.\source\\promotions.csv',  delimiter =',')  
df_products = pd.read_csv('.\source\\products.csv',  delimiter =',')  

#data cleaning
df_orders['created_at'] =[datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d') for x in df_orders['created_at']]
cols=['discounted_amount','vat_amount','total_amount','discount_rate'] 
df_order_lines[cols] = df_order_lines[cols].round(2)

