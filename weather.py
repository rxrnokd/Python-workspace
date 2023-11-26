import requests

def current_temp(date, time):
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params ={'serviceKey' : 'HcYIyLc612fqNjJ%2FNYs252txzi9CLPoCrXJ7odF8baDERTVYVxSOOPmeKEWFkzL88VMMAOlyv8nUgzu9MUauOA%3D%3D', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : date, 'base_time' : time, 'nx' : '98', 'ny' : '76' }

    response = requests.get(url, params=params)

    try:
        data = response.json()
        rain = data['response']['body']['items']['item'][0]['obsrValue']
        if rain == '0':
            rain = ' '
        elif rain == '1':
            rain = '비'
        elif rain == '2':
            rain = '비/눈'
        elif rain == '3':
            rain = '눈'
        elif rain == '5':
            rain = '빗방울'                
        elif rain == '6':
            rain = '빗방울/눈날림'
        else:
            rain = '눈날림'    

        return data['response']['body']['items']['item'][3]['obsrValue'] + '°C', rain

    except requests.exceptions.RequestException as e:
        return "", "" 