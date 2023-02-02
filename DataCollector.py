import tushare as ts

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# =========== tushare 数据格式 ==============
# ts_code        object   代码
# trade_date     object   交易时间
# open          float64   开盘价
# high          float64   最高价
# low           float64   最低价
# close         float64   收盘价
# pre_close     float64   昨收价
# change        float64   涨跌额
# pct_chg       float64   涨跌幅
# vol           float64   成交量（手）
# amount        float64   成交额（千元）
# ===========================================

tushare_token = '29337756e1240f9ec7c2cc102dc2d1bf23c18f76136760d1070bbf37'

start_date = '20220101'
end_date = '20221205'


print('get the data : ')

ts_code = '002514.SZ'
ts_code2 = '601318.SH'

tspro = ts.pro_api(tushare_token)
df = tspro.daily(ts_code=ts_code2, start_date=start_date, end_date=end_date)

print (' get data end')