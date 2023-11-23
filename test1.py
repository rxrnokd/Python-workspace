from urllib.request import urlopen

domain = 'https://apihub.kma.go.kr/api/typ01/url/upp_temp.php?'
tm = 'tm1=202302132200&tm2=202302132210&'
stn_id = 'stn=104&'
option = 'disp=0&help=0&authKey'
auth = 're51Tkt5R1mudU5LeVdZ2A'

url = domain + tm + stn_id + option + auth

with  urlopen(url) as f:

    html = f.read()
    print(html)






        
