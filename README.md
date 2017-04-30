FortuneDog股票量化程序
=====================

股票交易需要一定的纪律，纪律之下赚钱的概率大于盲目的操作，程序是纪律最好的执行者。


----------


股票源数据获取说明
------------------------------

凤凰财经获取月，周，日级别数据：
月数据： http://api.finance.ifeng.com/akmonthly/?code=sz000002&type=last 
周数据： http://api.finance.ifeng.com/akweekly/?code=sz000002&type=last 
日数据： http://api.finance.ifeng.com/akdaily/?code=sz000002&type=last 

>**url格式如下**：

> - akmonthly表示月数据
> - akweekly表示周数据
> - akdaily表示日数据
> - code是根据上证或者深证来的，上证前面加sh，深证前面加sz（包括创业板），例如中国石油（601857）的日线数据的url为：http://api.finance.ifeng.com/akdaily/?code=sh601857&type=last

>**数据格式**

> - 获取的数据格式依次说明：
   'date',    日期 
    'open',    开盘价 
    'high',    最高价 
    'close',   收盘价 
    'low',     最低价 
    'volume',  成交量 
    'chg',     涨跌额 
    'pchg',    涨跌幅 
    'ma5',     5日均价 
    'ma10',    10日均价 
    'ma20',    20日均价 
    'vma5',    5日均量 
    'vma10',   10日均量 
    'vma20',   20日均量 
    'turnover' 换手率 


分钟数据获取说明：
60分钟：http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=sh600707,m60,,640&_var=m60_today&r=0.8528988508953326 
30分钟：http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=sh600707,m30,,640&_var=m30_today&r=0.5691769460276088 
15分钟：http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=sh600707,m15,,640&_var=m15_today&r=0.9443892357069260 
5分钟：http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=sh600707,m5,,640&_var=m5_today&r=0.2933857481055513 

> - 获取的数据格式依次说明：
   'hour',    时间 
    'open',    开盘价 
    'close',    收盘价 
    'high',   最高价 
    'low',     最低价 
    'volume',  成交量 