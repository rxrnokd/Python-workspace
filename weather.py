import requests

def short_term_situation(date, time):
    # 기상청 초단기 실황 url, 요청변수 
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey' : 'HcYIyLc612fqNjJ%2FNYs252txzi9CLPoCrXJ7odF8baDERTVYVxSOOPmeKEWFkzL88VMMAOlyv8nUgzu9MUauOA%3D%3D', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : date, 'base_time' : time, 'nx' : '98', 'ny' : '76' }

    # 데이터 받아옴
    response = requests.get(url, params=params, timeout = 2)

    # 데이터 가공
    try:
        data = response.json()
        rain = data['response']['body']['items']['item'][0]['obsrValue']
        if rain == '0':
            rain = ' '
        elif rain == '1':
            rain = '🌧️'
        elif rain == '2':
            rain = '🌧️|🌨️'
        elif rain == '3':
            rain = '🌨️'
        elif rain == '5':
            rain = '💧'                
        elif rain == '6':
            rain = '💧|❄️'
        else:
            rain = '❄️'    

        return data['response']['body']['items']['item'][3]['obsrValue'] + '°C', rain

    except (requests.exceptions.RequestException, KeyError):
        return "", "" 