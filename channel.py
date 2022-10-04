import requests as req
import json

def test_channel(): 

    url = 'http://8.219.83.66:8088/admin/v2/login'
    
    headers={ 
        "Content-Type": "application/json"
    }

    data = '{"password":"1234","username":"admin"}'

    r = req.post(url,headers=headers,data=data)

    #d = json.loads(r.text)
    #print (d ['token'])
    #print(r.text)
 
    url = ' http://8.219.83.66:8088/admin/v2/system/dict/data/channels'

    headers={ 
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImQyMDU4YTNmLTNjYzItNGEwNy04NTBiLTcxOGExYTBiYTVlZSJ9.k6qxvq32PuhBQeekMIzJuIz6IUddYiyIAzXCrfhaZ4OZio5wGBeBaiRkym_OLTpxAQlUsebsnzskxWsQa5sZVw"
    }

    data = '{"pageNum":"1","pageSize":"10000"}'

    r = req.post(url,headers=headers,data=data)

    print(r.text)

if __name__ == '__main__': 
    test_channel()
    
# SQL
