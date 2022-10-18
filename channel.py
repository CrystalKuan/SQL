import requests as req
import json

def test_channel(): 

    url = 'http://8.219.83.66:8088/admin/v2/login'
    
    headers={ 
        "Content-Type": "application/json"
    }

    data = '{"password":"1234","username":"admin"}'

    r = req.post(url,headers=headers,data=data)

    d = json.loads(r.text)

    token = d ["token"]
 
    url = ' http://8.219.83.66:8088/admin/v2/system/dict/data/channels'

    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }

    data = '{"pageNum":"1","pageSize":"10000"}'

    r = req.post(url,headers=headers,data=data)

    print(r.text)

if __name__ == '__main__': 
    test_channel()
    
"# SQL" 
