import requests
import json
import simplejson
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url = "http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?lmt=0&klt=101&secid=0.002156&fields1=f1,f2,f3,f7&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65&ut=b2884a393a59ad64002292a3e90d46a5&cb=jQuery183021900406844669162_1588323703074&_=1588323703387"
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}
print(sys.getdefaultencoding())
r = requests.get(url,headers)
# print(r.content)
print(eval(r.content))
# json.loads(r.content)
# da = json.dumps(r.text, encoding="UTF-8", ensure_ascii=False)
# print(type(da))
# oo = json.loads(da)
# print(oo["data"])


