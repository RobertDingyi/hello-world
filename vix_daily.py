# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:34:07 2019

@author: ding1
"""

import pandas as pd 
import numpy as np
from datetime import datetime

ETF_daily_data=pd.read_csv('ETF_daily_data.csv',parse_dates=['trading_date'])
option_daily_data=pd.read_csv('option_daily_data.csv',parse_dates=['trading_date'])
option_information=pd.read_csv('option_information.csv',parse_dates=['start_date','end_date','actual_start_date','actual_end_date'])


begd='2019-06-27'
endd='2019-06-27'

begd=datetime.strptime(begd,'%Y-%m-%d')
endd=datetime.strptime(endd,'%Y-%m-%d')

trading_date_list=ETF_daily_data.loc[(ETF_daily_data.trading_date>=begd)&(ETF_daily_data.trading_date<=endd),'trading_date']
vix_results=pd.DataFrame(np.ones(len(trading_date_list)),columns=['vix'],index=trading_date_list)
vix_results.index.name='trading_date'

from function_option_vix_skew import  vix

for d in vix_results.index:
    ivx=vix(d,ETF_daily_data,option_information,option_daily_data)
    vix_results.loc[d,'vix']=ivx
    print(str(d)+' calculation done!')

vix_saved=pd.read_csv('vix_510050.csv',index_col=0,parse_dates=['trading_date'])
vix_saved=vix_saved.append(vix_results)


vix_saved.plot()
vix_saved.to_csv('vix_510050.csv',index_label='trading_date')