# module to implement class Analytics


from data import *

# create a dictionary to store generated analytics data for quick re-retrival
Analytics_Cache = {}



class Analytics:
    ''' for a given date in format yyyy-mm-dd this class will 
        return a report that will contain the following metrics.
        >The total number of items sold on that day.
        >The total number of customers that made an order that day.
        >The total amount of discount given that day.
        >The average discount rate applied to the items sold that day.
        >The average order total for that day
        >The total amount of commissions generated that day.
        >The average amount of commissions per order for that day.
        >The total amount of commissions earned per promotion that day'''
    
    def __init__(self, date):
        self.analytics_date = date
        self.customers = 0
        self.total_discount_amount = 0.0
        self.items = 0
        self.order_total_average = 0.0
        self.discount_rate_avg = 0.0
        self.comm_total = 0.0
        self.comm_order_avg = 0.0
        self.commissions = {}
        self.promotions ={}
        self.output= {}
        
    
    def __repr__(self):
        # return a json string of the output dictionary
        return json.dumps(self.output , indent=4)
    
    def get_analytics(self):
        # check for and return data for a date already generated and stored.
        if self.analytics_date in Analytics_Cache:
            self.output = Analytics_Cache[self.analytics_date]
        else: # if not found then generate from data 
            self.generate_analytics()
            
    
    def generate_analytics(self):

        # The Dataframes used here are populated within data.py

        ## Filter Data ##
        #################
        
        # Filter orders for on analytics_date
        df_order_dt  = df_orders.loc[(df_orders['created_at']== self.analytics_date)] 
        
        # Filter commissions on analytics_date
        df_commissions_dt  = df_commissions.loc[(df_commissions['date']== self.analytics_date)] 
        
        # Filter promotions on analytics_date
        df_prod_promotions_dt  = df_product_promotions.loc[(df_product_promotions['date']== self.analytics_date)] 
        
        # If there are no orders on analytics_date. Exist to stop unnecessary processing.
        if df_order_dt.empty:
            return None


        ## Enrich Data ##
        #################
        
        # Enrich df_order_dt with commission rates from df_commissions_dt
        cols_to_merge = ['vendor_id','rate']
        df_order_dt = pd.merge(df_order_dt,df_commissions_dt[cols_to_merge],on='vendor_id', how='left')
        df_order_dt.rename(columns={"rate": "vendor_comm_rate", "id":"order_id"}, inplace=True)

        # Enrich df_order_dt with order_lines data from df_order_lines
        cols_to_merge = ['order_id','product_id','discount_rate','quantity','discounted_amount','total_amount']
        df_order_dt = pd.merge(df_order_dt,df_order_lines[cols_to_merge],on='order_id', how='left')

        # Enrich df_order_dt with the promotion id
        # Clean up Nan's and revert promotion_id back to int after Left Join
        df_order_dt = pd.merge(df_order_dt,df_prod_promotions_dt[['product_id','promotion_id']], on='product_id', how='left')
        df_order_dt[['promotion_id']]=df_order_dt[['promotion_id']].fillna(0).astype(int)

        # Add a calculate column called "vendor_comm" as: commission_rate * total_amount 
        df_order_dt['vendor_comm'] = df_order_dt['vendor_comm_rate'] * df_order_dt['total_amount'] 
        
        ## Compute the Required Analytics ##
        ####################################

        # The total number of customers that made an order that day. #
        self.customers = df_order_dt['customer_id'].nunique()

        # The total amount of discount given that day. # 
        self.total_discount_amount = round(df_order_dt['discounted_amount'].sum(),2)
        
        # The total number of items sold on that day. # 
        self.items = df_order_dt['quantity'].sum()

        # The average order total for that day. # 
        self.order_total_average = round(df_order_dt.groupby(['order_id']).sum()['total_amount'].mean(),2)
        
        # The average discount rate applied to the items sold that day. #
        self.discount_rate_avg = round(df_order_dt['discount_rate'].mean(),2)

        
        ## Compute the Commissions Data ##
        ##################################
              
        # The total amount of commissions earned per promotion that day
        comm_by_prom =df_order_dt.groupby(['promotion_id']).sum()['vendor_comm']

        # loop through comm_by_prom to build a dictionary of promotion_id:promotion_amt
        # ignoring where promotion_id is not greater than 0
        dict_comm_by_prom={}
        for promotion_id,commission_amt in comm_by_prom.items():
            if promotion_id !=0:
                dict_comm_by_prom[promotion_id] = round(commission_amt,2)
                
        # store the promotion_id:commission_amt key value pairs
        self.commissions['promotions'] = dict_comm_by_prom

        # The total amount of commissions generated that day. # 
        self.comm_total = round(df_order_dt['vendor_comm'].sum(),2)

        # store the commissions generated that day 
        self.commissions['total'] = self.comm_total
        
        # The average amount of commissions per order for that day #  
        self.comm_order_avg = round(df_order_dt.groupby(['order_id']).sum()['vendor_comm'].mean(),2)

        # store the average amount of commissions per order for that day
        self.commissions['order_average'] = self.comm_order_avg     


        # Populate self.output with all analytics data #
        ################################################

        self.output["customers"] = self.customers
        self.output["total_discount_amount"] = self.total_discount_amount
        self.output["items"] = int(self.items)
        self.output["order_total_average"] = self.order_total_average
        self.output["discount_rate_avg"] = self.discount_rate_avg
        self.output['commissions'] = self.commissions
        
        
        # Add generated analytics to cache for repeat retrieval#
        ########################################################
        
        Analytics_Cache[self.analytics_date] =  self.output
    