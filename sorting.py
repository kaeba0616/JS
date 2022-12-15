import pandas as pd
import json

f = open('result.do', 'r', encoding='UTF-8')
line = f.readline()
f.close()

json_data = json.loads(line)
data = json_data['data']
df = pd.DataFrame(json.loads(data))
df.to_csv('out.csv', header = True, index = True, encoding= 'ms949')
