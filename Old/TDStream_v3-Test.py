# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:51:37 2019

@author: LC
"""


#import datetime as dt
from Ameritrade_cfg import client_id, redirect_uri, account_id
from TDStream_v3 import TDStreamer  ##CSV Version
import pandas as pd

TDS = TDStreamer(client_id, redirect_uri, account_id)

TDS.start_streamer()

TDS.data_request_nasdaq_book(command = "SUBS", keys = 'SPY, AAPL, MELI, GOOG, AMZN, NFLX, TSLA, NVDA, SLB, ,C, FB, MSFT, KO, DIS', fields = '0,1,2,3')
TDS.data_request_chart_equity(command = "SUBS", keys = 'SPY, AAPL, MELI, GOOG, AMZN, NFLX, TSLA, NVDA, SLB, ,C, FB, MSFT, KO, DIS', fields = '0,1,2,3,4,5,6,7,8')
TDS.data_request_timesale_equity(command = "SUBS", keys = 'SPY, AAPL, MELI, GOOG, AMZN, NFLX, TSLA, NVDA, SLB, ,C, FB, MSFT, KO, DIS', fields = '0,1,2,3,4')      

TDS.QOS_request()
TDS.logout_request()

response = TDS.response
snapshot = TDS.snapshot
notify = TDS.notify

level2 = TDS.level2_nasdaq
timesales = TDS.time_sales_equity
account_act = TDS.acct_activity
chart = TDS.chart_equity
subs_data = TDS.subs_data
xtra_data = TDS.ext_subs



lvl2_df = pd.DataFrame(level2)
lvl2_df.rename(columns={0:'DateTime',1:'Ticker',2: '[Bid/Ask]',3:'Price',4:'Size',5:'Num_Orders',6:'Orders',7:'Message_Timestamp'}, inplace=True)
lvl2_df.set_index(['DateTime'], inplace=True)

TSales_df = pd.DataFrame(timesales)
TSales_df.rename(columns={0:'DateTime',1:'Ticker',2: 'Sequence',3:'Price',4:'Size',5:'LastSequence',6:'Message_Timestamp'}, inplace=True)
TSales_df.set_index(['DateTime'], inplace=True)

Chart_df = pd.DataFrame(chart)
Chart_df.rename(columns={0:'DateTime',1:'Ticker',2: 'Sequence',3:'open_price',4:'high',5:'low',6:'close_price',7:'volume',8:'LastSequence',9:'ChartDay'}, inplace=True)
Chart_df.set_index(['DateTime'], inplace=True)

TDS.connect()
TDS.last_message_time

TDS.ws.close()

TDS.data_request_account_activity(command = "SUBS", fields = '0,1,2,3')  
#TDS.data_request_account_activity(command = "UNSUBS", fields = '0,1,2,3')  

TDS.data_request_actives_nasdaq(command = "SUBS", keys = 'NASDAQ-60', fields = '0,1')
#TDS.data_request_actives_nasdaq(command = "UNSUBS", keys = 'NASDAQ-60', fields = '0,1')

TDS.data_request_actives_nyse(command = "SUBS", keys = 'NYSE-60', fields = '0,1')  
#TDS.data_request_actives_nyse(command = "UNSUBS", keys = 'NYSE-60', fields = '0,1')  
 
TDS.data_request_actives_otcbb(command = "SUBS", keys = 'OTCBB-60', fields = '0,1')
#TDS.data_request_actives_otcbb(command = "UNSUBS", keys = 'OTCBB-60', fields = '0,1')
        
TDS.data_request_actives_options(command = "SUBS", keys = 'OPTS-DESC-ALL', fields = '0,1')
#TDS.data_request_actives_options(command = "UNSUBS", keys = 'OPTS-DESC-ALL', fields = '0,1')
     
TDS.data_request_chart_equity(command = "SUBS", keys = 'SPY', fields = '0,1,2,3,4,5,6,7,8')
#TDS.data_request_chart_equity(command = "UNSUBS", keys = 'SPY', fields = '0,1,2,3,4,5,6,7,8')
        
TDS.data_request_chart_futures(command = "SUBS", keys = '/ES', fields = '0,1,2,3,4,5,6')
#TDS.data_request_chart_futures(command = "UNSUBS", keys = '/ES', fields = '0,1,2,3,4,5,6')

TDS.data_request_chart_options(command = "SUBS", keys = 'SPY_112219C300', fields = '0,1,2,3,4,5,6,7,8')
#TDS.data_request_chart_options(command = "UNSUBS", keys = 'SPY_111819C300', fields = '0,1,2,3,4,5,6')

TDS.data_request_quote(command = "SUBS", keys = 'AAPL', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52')       
#TDS.data_request_quote(command = "UNSUBS", keys = 'AAPL', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52')       
    
TDS.data_request_option(command = "SUBS", keys = 'SPY_112219C300', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,343,35,36,37,38,39,40,41')
#TDS.data_request_option(command = "UNSUBS", keys = 'SPY_111819C300', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,343,35,36,37,38,39,40,41')

TDS.data_request_listed_book(command = "SUBS", keys = 'SPY', fields = '0,1,2,3,4,5,6')
#TDS.data_request_listed_book(command = "UNSUBS", keys = 'SPY', fields = '0,1,2,3,4,5,6')     
   
TDS.data_request_nasdaq_book(command = "SUBS", keys = 'AAPL', fields = '0,1,2,3,4,5,6')
#TDS.data_request_nasdaq_book(command = "UNSUBS", keys = 'AAPL', fields = '0,1,2,3,4,5,6')
    
TDS.data_request_options_book(command = "SUBS", keys = 'SPY_112219C300', fields = '0,1,2,3,4,5,6')
#TDS.data_request_options_book(command = "UNSUBS", keys = 'SPY_111819C300', fields = '0,1,2,3,4,5,6')
       
TDS.data_request_levelone_futures(command = "SUBS", keys = '/ES', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35')
#TDS.data_request_levelone_futures(command = "UNSUBS", keys = '/ES', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35')
        
TDS.data_request_levelone_forex(command = "SUBS", keys = 'EUR/USD', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28')       
#TDS.data_request_levelone_forex(command = "UNSUBS", keys = 'EUR/USD', fields = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28')  
    
TDS.data_request_timesale_equity(command = "SUBS", keys = 'AAPL', fields = '0,1,2,3,4')       
#TDS.data_request_timesale_equity(command = "UNSUBS", keys = 'AAPL', fields = '0,1,2,3,4')   
        
TDS.data_request_timesale_futures(command = "SUBS", keys = '/ES', fields = '0,1,2,3,4')   
#TDS.data_request_timesale_futures(command = "UNSUBS", keys = '/ES', fields = '0,1,2,3,4')   

TDS.data_request_timesale_options(command = "SUBS", keys = 'SPY_112219C300', fields = '0,1,2,3,4')
#TDS.data_request_timesale_options(command = "UNSUBS", keys = 'SPY_111819C300', fields = '0,1,2,3,4')

TDS.data_request_news_headline(command = "SUBS", keys = 'SPY', fields = '0,1,2,3,4,5,6,7,8,9,10')        
#TDS.data_request_news_headline(command = "UNSUBS", keys = 'AAPL', fields = '0,1,2,3,4,5,6,7,8,9,10')    


TDS.data_request_news_headlinelist(keys = 'SPY')

TDS.data_request_news_story(keys = 'SN20191111010526')

TDS.data_request_chart_history_futures(symbol = '/ES', frequency = 'm5', period = 'd5', start_time = None, end_time = None)


