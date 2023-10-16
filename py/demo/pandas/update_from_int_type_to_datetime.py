import pandas as pd
from datetime import datetime, timedelta

current_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d' + ' 23:59:59')
followers_count = 300
data_to_insert = pd.DataFrame([(0,4,'followers_count',followers_count,0)])
data_to_insert.columns = ['metric_datetime', 'account_id', 'metric_name', 'metric_value', 'received_at']
data_to_insert = data_to_insert.assign(metric_datetime=yesterday, received_at=current_time)
print(data_to_insert.columns)
