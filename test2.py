import requests

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'HcYIyLc612fqNjJ%2FNYs252txzi9CLPoCrXJ7odF8baDERTVYVxSOOPmeKEWFkzL88VMMAOlyv8nUgzu9MUauOA%3D%3D', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : '20231125', 'base_time' : '1200', 'nx' : '96', 'ny' : '75' }

response = requests.get(url, params=params)
data = response.json()
print(data['response']['body']['items']['item'][3]['obsrValue'])

