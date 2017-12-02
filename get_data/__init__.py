import pandas as pd
from get_data.db import engine
from get_data.db import TABLE_STOCK
from utils.cache import cache

@cache(use_mem=True)
def all_codes():
    '''
    获取不重复的股票代码
    :return:
    '''
    try:
        r = pd.read_sql("select distinct code from %s" % TABLE_STOCK, engine)
        codes = r['code']
        return codes
    except:
        print("stock表不存在，请先获取stock相关数据再执行此操作")
