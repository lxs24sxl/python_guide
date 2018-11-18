# import requests

# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# # 将数据写入文件
# with open('btc_close_2017_request.json', 'w') as f:
#   f.write(req.text)
# file_requests = req.json()


import json
# 将数据加载到一个列表中
filename = 'btc_close_2017_request.json'

dates, months, weeks, weekdays, close = [], [], [], [] ,[]

with open(filename) as f:
  btc_data = json.load(f)
# 打印每一天的信息
for btc_dict in btc_data:
  # date = btc_dict['date']
  # month = int(btc_dict['month'])
  # week = int(btc_dict['week'])
  # weekday = btc_dict['weekday']
  # close = int(float(btc_dict['close']))
  # print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))
  dates.append(btc_dict['date'])
  months.append(int(btc_dict['month']))
  weeks.append(int(btc_dict['week']))
  weekdays.append(btc_dict['weekday'])
  close.append(int(float(btc_dict['close'])))

import pygal

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价(元)'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图(元).svg')