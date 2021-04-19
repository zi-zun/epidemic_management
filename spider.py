# -*- coding: utf-8 -*-
from pyecharts.charts import Line
from requests import get
from time import time
from json import loads
from operator import itemgetter

data = loads(get(f"https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_="
             f"{int(time() * 1000)}").json()['data'])["chinaDayList"][-15:]

line = Line()
line.add_xaxis([*map(itemgetter("date"), data)])
line.add_yaxis("确诊", [*map(lambda x: int(x["confirm"]), data)])
line.add_yaxis("疑似", [*map(lambda x: int(x["suspect"]), data)])
line.add_yaxis("治愈", [*map(lambda x: int(x["heal"]), data)])
line.add_yaxis("死亡", [*map(lambda x: int(x["dead"]), data)])
line.render("疫情最新动态.html")

