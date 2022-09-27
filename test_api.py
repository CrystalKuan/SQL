import requests   #發送HTTP請求
import json   #使用json函數
import base64   #編碼函式
import hashlib   #計算資料各種雜湊值
#import pytest

# pp部分
# ctrl ={
# app_info
# caipiao_bet
# cash_class
# cash
# fs_finally_config
# fs_finally_scheme
# game_list
# game_log
# game_money_log
# game_type
# tg
# user_payway
# vip
# }

# live 部分
# ctrl ={
# channel
# diamond_exchange
# diamond
# item
# payment_class
# payment
# recharge
# room
# ticket_log
# user
# }

#baseUrl = "https://reqres.in/"
#baseUrl = "http://8.219.58.126:10086"

#PP数据后台
#http://8.219.58.126:1081/buyaojidezhu.html#/
ppbaseUrl = "http://8.219.58.126:10086"

#Live3管理后台
#http://8.219.58.126:2010/admin.html#/
livebaseUrl = "http://8.219.58.126:10086"

saltKey = "fd63b3e39a94acf8"

begin_time = "1660779600"
end_time = "1662528600"
tm = end_time

def genSignature(info):

    data = info + saltKey

    m = hashlib.md5()   #獲取一個加密算法
    m.update(data.encode("utf-8"))   #制定需要加密的字串符

    return m.hexdigest()   #返回16進制的str形式

def genInfo(dist):

    b = dist.encode("UTF-8")   #編碼用法

    return base64.b64encode(b).decode('UTF-8')   #編碼及解碼用法

"""
def test_list_user():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user","begin_time":1654732800,"ctl":"user","end_time":1652486400,"page":1,"page_size":500,"tm":1654573070}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200
"""

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X2ZzX2RhaWx5X3N0YXQiLCJjdGwiOiJ0ZyIsInBhZ2UiOjEsInBhZ2Vfc2l6ZSI6NTAwLCJyZXBvcnRfZGF0ZSI6MjAyMjA1MDQsInRtIjoxNjU0NTczMTkwfQ==&sign=398d18f79f36e7969db8eb8097400ffb
#{"act":"list_fs_daily_stat","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573190}
#{"data":[{"channel_ii":"LALALA","id":60169,"report_date":20220504,"channel_i":"tui1","game_income":0,"user_id":490468811,"live_income":95.88},{"channel_ii":"default","id":60170,"report_date":20220504,"channel_i":"tui1","game_income":0,"user_id":674222657,"live_income":20},{"channel_ii":"default","id":60171,"report_date":20220504,"channel_i":"tui1","game_income":128.85,"user_id":1380848598,"live_income":0},{"channel_ii":"default","id":60172,"report_date":20220504,"channel_i":"tui1","game_income":0,"user_id":150910759,"live_income":180}],"code":0,"count":"4"}
def test_list_fs_daily_stat():   #返利

    path = "/open_api/proxy_api"

    dist = '{"act":"list_fs_daily_stat","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573190}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    #if(response.json()["count"] == "0"):
        
    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X3RnX2RhaWx5X2JldF9zdGF0IiwiY3RsIjoidGciLCJwYWdlIjoxLCJwYWdlX3NpemUiOjUwMCwicmVwb3J0X2RhdGUiOjIwMjIwNTA0LCJ0bSI6MTY1NDU3MzM0OH0=&sign=0de87f6a09f602f708a36dc2b4e8c613
#{"act":"list_tg_daily_bet_stat","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573348}
#{"data":[{"game_fs_money":0,"id":94149,"live_fs_money":0,"bet":0.75,"user_id":145247033,"win":-0.75,"report_date":20220504,"recharge":31000,"exchange_diamond":230,"tg_tree_path":"\/tui1\/150910759\/674222657\/1605450225"},{"game_fs_money":0,"id":94158,"live_fs_money":0,"bet":20,"user_id":148233276,"win":9.4,"report_date":20220504,"recharge":0,"exchange_diamond":0,"tg_tree_path":"\/tui1\/321879324"},{"game_fs_money":128.85,"id":94153,"live_fs_money":0,"bet":43047.49,"user_id":173438251,"win":-14975.38,"report_date":20220504,"recharge":1630000,"exchange_diamond":0,"tg_tree_path":"\/tui1\/1380848598"},{"game_fs_money":0,"id":94154,"live_fs_money":95.88,"bet":0,"user_id":828514097,"win":0,"report_date":20220504,"recharge":5000,"exchange_diamond":3196,"tg_tree_path":"\/tui1\/490468811"},{"game_fs_money":0,"id":94155,"live_fs_money":0,"bet":0,"user_id":1146085804,"win":0,"report_date":20220504,"recharge":2600,"exchange_diamond":0,"tg_tree_path":"\/tui1\/1046283686"},{"game_fs_money":0,"id":94159,"live_fs_money":0,"bet":0,"user_id":1295199058,"win":0,"report_date":20220504,"recharge":0,"exchange_diamond":8000,"tg_tree_path":"\/pf\/1918450184"},{"game_fs_money":0,"id":94148,"live_fs_money":0,"bet":0,"user_id":1318320985,"win":0,"report_date":20220504,"recharge":0,"exchange_diamond":3098,"tg_tree_path":"\/pf\/293068506"},{"game_fs_money":0,"id":94157,"live_fs_money":100,"bet":80500,"user_id":1386796288,"win":-20720,"report_date":20220504,"recharge":7230000,"exchange_diamond":418914,"tg_tree_path":"\/tui1\/150910759"},{"game_fs_money":0,"id":94152,"live_fs_money":0,"bet":51,"user_id":1431800796,"win":-51,"report_date":20220504,"recharge":0,"exchange_diamond":0,"tg_tree_path":"\/tui1\/512308301"},{"game_fs_money":0,"id":94151,"live_fs_money":100,"bet":0,"user_id":1492772289,"win":0,"report_date":20220504,"recharge":0,"exchange_diamond":21876,"tg_tree_path":"\/tui1\/150910759\/674222657"},{"game_fs_money":0,"id":94156,"live_fs_money":0,"bet":0,"user_id":1509864132,"win":0,"report_date":20220504,"recharge":5000,"exchange_diamond":0,"tg_tree_path":"\/pf\/156099074"},{"game_fs_money":0,"id":94150,"live_fs_money":0,"bet":0,"user_id":1612616059,"win":0,"report_date":20220504,"recharge":5000,"exchange_diamond":3196,"tg_tree_path":"\/tui1\/939667933"}],"code":0,"count":"12"}
def test_list_tg_daily_bet_stat():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_tg_daily_bet_stat","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573348}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    #if(response.json()["count"] == "0"):
        
    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X3RnX2RhaWx5X2ZlbmhvbmdfbG9nIiwiY3RsIjoidGciLCJwYWdlIjoxLCJwYWdlX3NpemUiOjUwMCwicmVwb3J0X2RhdGUiOjIwMjIwNTA0LCJ0bSI6MTY1NDU3MzY5OH0=&sign=43ed550de81a8df9f84bdcafa22ee0cd
#{"act":"list_tg_daily_fenhong_log","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573698}
#{"data":[{"channel_id":"tui1","id":63434,"report_date":20220504,"from_user_id":173438251,"live_bonus":0,"game_bonus":128.85,"to_user_id":173438251},{"channel_id":"tui1","id":63435,"report_date":20220504,"from_user_id":828514097,"live_bonus":95.88,"game_bonus":0,"to_user_id":828514097},{"channel_id":"tui1","id":63437,"report_date":20220504,"from_user_id":1386796288,"live_bonus":100,"game_bonus":0,"to_user_id":1386796288},{"channel_id":"tui1","id":63436,"report_date":20220504,"from_user_id":1492772289,"live_bonus":80,"game_bonus":0,"to_user_id":1386796288},{"channel_id":"tui1","id":63433,"report_date":20220504,"from_user_id":1492772289,"live_bonus":20,"game_bonus":0,"to_user_id":1492772289}],"code":0,"count":"5"}
def test_list_tg_daily_fenhong_log():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_tg_daily_fenhong_log","ctl":"tg","page":1,"page_size":500,"report_date":20220504,"tm":1654573698}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    #if(response.json()["count"] == "0"):
        
    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

""""
def test_list_pp_user():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_pp_user","begin_time":1654732800,"ctl":"user","end_time":1652486400,"page":1,"page_size":500,"tm":1654573793}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200
"""

"""
def test_list_pp_user_change_ids():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_pp_user_change_ids","ctl":"user","page":1,"page_size":500,"report_date":20220521,"tm":1654573910}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200
"""

"""
def test_list_pp_user_by_id():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_pp_user_by_id","ctl":"user","ids":"[1,2,3]","page":1,"page_size":500,"tm":1654574025}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["data"][0]["username"] == ""):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False
    
    if(response.status_code != 200):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert True
"""

"""
def test_list_user_extern():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_extern","begin_time":1654732800,"ctl":"user","end_time":1652486400,"page":1,"page_size":500,"tm":1654574282}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200    
""" 

"""
def test_list_user_extern_change_ids():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_extern_change_ids","ctl":"user","page":1,"page_size":500,"report_date":202205041122,"tm":1654574450}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)
    
    if(response.json()["count"] == "0"):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200
"""

"""
def test_list_user_extern_by_id():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_extern_by_id", "ctl":"user", "ids":"[22762460, 23657643, 75020779]", "page":1, "page_size":500, "tm":1654678223}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["data"] == {}):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200
"""

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X2RpYW1vbmRfbG9nIiwiYmVnaW5fdCI6MTY1NDczMjgwMCwiY3RsIjoiZGlhbW9uZCIsImVuZF90IjoxNjUyNDg2NDAwLCJvcGVyX3R5cGUiOjEsInBhZ2UiOjEsInBhZ2Vfc2l6ZSI6NTAwLCJ0bSI6MTY1NDU3OTU1N30=&sign=186dfb54a7688a467683fbdf0acf0ea7
#{"act":"list_diamond_log","begin_t":1654732800,"ctl":"diamond","end_t":1652486400,"oper_type":1,"page":1,"page_size":500,"tm":1654579557}
#{"code":-1,"msg":"Table 'live3_logs.tb_diamond_log' doesn't exist"}
def test_list_diamond_log():   #鑽石支出

    path = "/open_api/proxy_api"

    dist = '{"act":"list_diamond_log","begin_t":1654732800,"ctl":"diamond","end_t":1652486400,"oper_type":1,"page":1,"page_size":500,"tm":1654579557}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)

    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJnZXRfb25saW5lX3BvZGNhc3RfY291bnQiLCJjdGwiOiJyb29tIiwidG0iOjE2NTQ1Nzk3NTB9&sign=2f48c4d598fe98a1f6d0d40c8f8f30ca
#{"act":"get_online_podcast_count","ctl":"room","tm":1654579750}
#{"code":0,"data":"179"}
def test_get_online_podcast_count():

    path = "/open_api/proxy_api"

    dist = '{"act":"get_online_podcast_count","ctl":"room","tm":1654579750}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)

    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")
    
    #if(response.json()["data"] == "0"):
        
    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0IiwiYmVnaW5fdGltZSI6MTYyNzMwOTEzNCwiY3RsIjoiY2FzaCIsImVuZF90aW1lIjoxNjI3MzA5MzM0LCJ0bSI6MTY1NDU3OTg0NX0=&sign=8d5fd11ec735f23e3f523c50853ef1bd
#{"act":"list","begin_time":1627309134,"ctl":"cash","end_time":1627309334,"tm":1654579845}
#{"code":0,"data":[{"id":1988,"user_id":39521845,"create_time":1627309183,"op_time":1627311869,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1160,"hosting_channel":"tui1","order_id":"CA273091830318","send_status":1,"send_time":1627311908,"bank_account_name":"王八蛋","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1989,"user_id":39521845,"create_time":1627309187,"op_time":1627375799,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1168,"hosting_channel":"tui1","order_id":"CA273091870319","send_status":2,"send_time":1627375987,"bank_account_name":"王八蛋","send_error":"签名错误","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1990,"user_id":39521845,"create_time":1627309191,"op_time":1627376264,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"{\"code\":200,\"pay_id\":\"CA273091910320\",\"ispay\":2}","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1169,"hosting_channel":"tui1","order_id":"CA273091910320","send_status":2,"send_time":1627395478,"bank_account_name":"王八蛋","send_error":"{\"code\":200,\"pay_id\":\"CA273091910320\",\"ispay\":2}","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1991,"user_id":39521845,"create_time":1627309194,"op_time":1627395614,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"{\"code\":200,\"pay_id\":\"CA273091940321\",\"ispay\":2}","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1169,"hosting_channel":"tui1","order_id":"CA273091940321","send_status":2,"send_time":1627395964,"bank_account_name":"王八蛋","send_error":"{\"code\":200,\"pay_id\":\"CA273091940321\",\"ispay\":2}","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1992,"user_id":39521845,"create_time":1627309198,"op_time":1627397056,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1160,"hosting_channel":"tui1","order_id":"CA273091980322","send_status":2,"send_time":1627397057,"bank_account_name":"王八蛋","send_error":"返回 数据解析失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1993,"user_id":39521845,"create_time":1627309202,"op_time":1627398655,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1160,"hosting_channel":"tui1","order_id":"CA273092020323","send_status":2,"send_time":1627399106,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1994,"user_id":39521845,"create_time":1627309205,"op_time":1627399145,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1160,"hosting_channel":"tui1","order_id":"CA273092050324","send_status":1,"send_time":1627399216,"bank_account_name":"王八蛋","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1995,"user_id":39521845,"create_time":1627309210,"op_time":1627407192,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1170,"hosting_channel":"tui1","order_id":"CA273092100325","send_status":1,"send_time":1627465950,"bank_account_name":"王八蛋","send_error":"paramters error!","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1996,"user_id":39521845,"create_time":1627309213,"op_time":1627466275,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1170,"hosting_channel":"tui1","order_id":"CA273092130326","send_status":2,"send_time":1627466874,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1997,"user_id":39521845,"create_time":1627309216,"op_time":1627467101,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1170,"hosting_channel":"tui1","order_id":"CA273092160327","send_status":1,"send_time":1627467290,"bank_account_name":"王八蛋","send_error":"paramters error!","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1998,"user_id":39521845,"create_time":1627309219,"op_time":1627490975,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1038,"hosting_channel":"tui1","order_id":"CA273092190328","send_status":2,"send_time":1627490976,"bank_account_name":"王八蛋","send_error":"签名校验失败001","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":1999,"user_id":39521845,"create_time":1627309222,"op_time":1627550761,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1173,"hosting_channel":"tui1","order_id":"CA273092220329","send_status":2,"send_time":1627550844,"bank_account_name":"王八蛋","send_error":"成功","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2000,"user_id":39521845,"create_time":1627309225,"op_time":1627550909,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1173,"hosting_channel":"tui1","order_id":"CA273092250330","send_status":1,"send_time":1627551245,"bank_account_name":"王八蛋","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2001,"user_id":39521845,"create_time":1627309228,"op_time":1627552833,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1173,"hosting_channel":"tui1","order_id":"CA273092280331","send_status":2,"send_time":1627553470,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2002,"user_id":39521845,"create_time":1627309231,"op_time":1627567833,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1172,"hosting_channel":"tui1","order_id":"CA273092310332","send_status":2,"send_time":1627574264,"bank_account_name":"王八蛋","send_error":"返回数据解析失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2003,"user_id":39521845,"create_time":1627309234,"op_time":1627724294,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1174,"hosting_channel":"tui1","order_id":"CA273092340333","send_status":2,"send_time":1627838853,"bank_account_name":"王八蛋","send_error":"","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2004,"user_id":39521845,"create_time":1627309237,"op_time":1627807767,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1175,"hosting_channel":"tui1","order_id":"CA273092370334","send_status":2,"send_time":1627832788,"bank_account_name":"王八蛋","send_error":"系统处理异常","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2005,"user_id":39521845,"create_time":1627309241,"op_time":1627838892,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1174,"hosting_channel":"tui1","order_id":"CA273092410335","send_status":2,"send_time":1627838956,"bank_account_name":"王八蛋","send_error":"","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2006,"user_id":39521845,"create_time":1627309243,"op_time":1627309779,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1160,"hosting_channel":"tui1","order_id":"CA273092430336","send_status":2,"send_time":1627397041,"bank_account_name":"王八蛋","send_error":"返回数据解析失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2007,"user_id":39521845,"create_time":1627309246,"op_time":1627839851,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1174,"hosting_channel":"tui1","order_id":"CA273092460337","send_status":1,"send_time":1627839935,"bank_account_name":"王八蛋","send_error":"","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2008,"user_id":39521845,"create_time":1627309249,"op_time":1627840075,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1174,"hosting_channel":"tui1","order_id":"CA273092490338","send_status":2,"send_time":1627840088,"bank_account_name":"王八蛋","send_error":"","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2009,"user_id":39521845,"create_time":1627309251,"op_time":1627929670,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1175,"hosting_channel":"tui1","order_id":"CA273092510339","send_status":3,"send_time":1628086652,"bank_account_name":"王八蛋","send_error":"系统处理异常","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2010,"user_id":39521845,"create_time":1627309254,"op_time":1627983456,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1176,"hosting_channel":"tui1","order_id":"CA273092540340","send_status":2,"send_time":1628002270,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2011,"user_id":39521845,"create_time":1627309257,"op_time":1628012124,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":500,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1177,"hosting_channel":"tui1","order_id":"CA273092570341","send_status":2,"send_time":1628012576,"bank_account_name":"王八蛋","send_error":"返回数据解析失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2012,"user_id":39521845,"create_time":1627309263,"op_time":1628012660,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":500,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1177,"hosting_channel":"tui1","order_id":"CA273092630342","send_status":2,"send_time":1628015321,"bank_account_name":"王八蛋","send_error":"返回数据解析失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2013,"user_id":39521845,"create_time":1627309265,"op_time":1628096379,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":10,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1178,"hosting_channel":"tui1","order_id":"CA273092650343","send_status":2,"send_time":1628176297,"bank_account_name":"王八蛋","send_error":"返回数据解析失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2014,"user_id":39521845,"create_time":1627309268,"op_time":1628097109,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1175,"hosting_channel":"tui1","order_id":"CA273092680344","send_status":3,"send_time":1628097422,"bank_account_name":"王八蛋","send_error":"签名验证不通过","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2015,"user_id":39521845,"create_time":1627309271,"op_time":1628153637,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1175,"hosting_channel":"tui1","order_id":"CA273092710345","send_status":3,"send_time":1628153638,"bank_account_name":"王八蛋","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2016,"user_id":39521845,"create_time":1627309282,"op_time":1628176484,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1175,"hosting_channel":"tui1","order_id":"CA273092820346","send_status":2,"send_time":1628180698,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2017,"user_id":39521845,"create_time":1627309285,"op_time":1628180746,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1175,"hosting_channel":"tui1","order_id":"CA273092850347","send_status":2,"send_time":1628181832,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2018,"user_id":39521845,"create_time":1627309287,"op_time":1628268128,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1175,"hosting_channel":"tui1","order_id":"CA273092870348","send_status":3,"send_time":1628268129,"bank_account_name":"王八蛋","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2019,"user_id":39521845,"create_time":1627309290,"op_time":1628268111,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1178,"hosting_channel":"tui1","order_id":"CA273092900349","send_status":2,"send_time":1628268112,"bank_account_name":"王八蛋","send_error":"返回数据解析失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2020,"user_id":39521845,"create_time":1627309293,"op_time":1628268616,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1180,"hosting_channel":"tui1","order_id":"CA273092930350","send_status":2,"send_time":1628268617,"bank_account_name":"王八蛋","send_error":"支付接口请求失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2021,"user_id":39521845,"create_time":1627309297,"op_time":1628416071,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1181,"hosting_channel":"tui1","order_id":"CA273092970351","send_status":2,"send_time":1628604657,"bank_account_name":"王八蛋","send_error":"支付接口请求失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2022,"user_id":39521845,"create_time":1627309301,"op_time":1628431985,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":" 失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1182,"hosting_channel":"tui1","order_id":"CA273093010352","send_status":2,"send_time":1628491248,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2023,"user_id":39521845,"create_time":1627309304,"op_time":1628444667,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1183,"hosting_channel":"tui1","order_id":"CA273093040353","send_status":2,"send_time":1628505152,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2024,"user_id":39521845,"create_time":1627309307,"op_time":1628527212,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1005,"hosting_channel":"tui1","order_id":"CA273093070354","send_status":2,"send_time":1628527213,"bank_account_name":"王八蛋","send_error":"bbpay接口请求失败","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2025,"user_id":39521845,"create_time":1627309311,"op_time":1628527233,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1185,"hosting_channel":"tui1","order_id":"CA273093110355","send_status":2,"send_time":1628527309,"bank_account_name":"王八蛋","send_error":"参数错误","bank_card":"622202147855222556","bank_name":"工商银行","status":1},{"id":2026,"user_id":39521845,"create_time":1627309315,"op_time":1628527413,"op_user_id":106,"charges_rate":0,"charges_value":0,"show_error":"失败，这家无错误信息","money":100,"is_manual":0,"pay_type":2,"channel_i":"tui1","channel_ii":"default","cash_class_id":1186,"hosting_channel":"tui1","order_id":"CA273093150356","send_status":2,"send_time":1628527473,"bank_account_name":"王八蛋","send_error":"失败，这家无错误信息","bank_card":"622202147855222556","bank_name":"工商银行","status":1}]}
def test_list_ctl_cash():   #提款

    path = "/open_api/proxy_api"

    dist = '{"act":"list","begin_time":1627309134,"ctl":"cash","end_time":1627309334,"tm":1654579845}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    #if(response.json()["data"] == {}):

    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0IiwiYmVnaW5fdGltZSI6MTY2MDc3OTYwMCwiY3RsIjoicGF5bWVudCIsImVuZF90aW1lIjoxNjYyNTI4NjAwLCJ0bSI6MTY2MjUyODYwMH0=&sign=8cb5cae8405647eb7a9c490ed5a008a1
#{"act":"list","begin_time":1660779600,"ctl":"payment","end_time":1662528600,"tm":1662528600}
def test_list_ctl_payment():   #充值

    path = "/open_api/proxy_api"

    # dist = '{"act":"list","begin_time":1662595200000,"ctl":"payment","end_time":1662728400000,"tm":1662728400}'
    dist = '{"act":"list","begin_time":' + begin_time + ',"ctl":"payment","end_time":' + end_time + ',"tm":'+ tm +'}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)
    
    #if(response.json()["data"][0]["pay_time"] == ""):
        
    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    # print(response.text+"\n")

    #   assert False

    # assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X2FjdGl2aXR5X2xvZyIsImJlZ2luX3RpbWUiOjE2NjI1MjUwMDAsImN0bCI6ImdhbWVfbW9uZXlfbG9nIiwiZW5kX3RpbWUiOjE2NjI1Mjg2MDAsInRtIjoxNjYyNTI4NjAwfQ==&sign=e8f77767284cd7f6eeda89cd3249dbe8
#{"act":"list_activity_log","begin_time":1662525000,"ctl":"game_money_log","end_time":1662528600,"tm":1662528600}
#nil
def test_list_activity_log():   #活動贈送

    path = "/open_api/proxy_api"
  
    # dist = '{"act":"list_activity_log","begin_time":1654617600,"ctl":"game_money_log","end_time":1654704000,"tm":1654580812}'
    dist = '{"act":"list_activity_log","begin_time":1662525000,"ctl":"game_money_log","end_time":1662528600,"tm":1662528600}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    #if(response.json()["data"] == {}):
        
    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

    #   assert False

    #ssert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X2NhaXBpYW9fYmV0IiwiYmVnaW5fdGltZSI6MTY2MDc3OTYwMCwiY3RsIjoiY2FpcGlhb19iZXQiLCJlbmRfdGltZSI6MTY2MjUyODYwMCwicGFnZSI6MSwicGFnZV9zaXplIjo1MDAsInRtIjoxNjYyNTI4NjAwfQ==&sign=de7f9746b455dfa15db2c26e30087458
#{"act":"list_caipiao_bet","begin_time":1660779600,"ctl":"caipiao_bet","end_time":1662528600,"page":1,"page_size":500,"tm":1662528600}
#{"result":{},"has_next":0,"tb_index":1,"code":0,"page":2}
def test_list_caipiao_bet():   #票數

    path = "/open_api/proxy_api"

    dist = '{"act":"list_caipiao_bet","begin_time":'+begin_time+',"ctl":"caipiao_bet","end_time":'+end_time+',"page":1,"page_size":500,"tm":'+tm+'}'
    
    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)
    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

    # if(response.json()["result"] == {}):
        
    #     print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    #     print(dist+"\n")
    #     print(response.text+"\n")

    #     assert False

    # assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0IiwiY3RsIjoiY2hhbm5lbCIsInRtIjoxNjU0NTgxMTI4fQ==&sign=92b4a5efb2408f2cc1484cf0e0b742bf
#{"act":"list","ctl":"channel","tm":1654581128}
#{"code":0,"result":[{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui2","channel_name":"tui2","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"tudou","channel_id":"tui3","channel_name":"tui3","open_channel_id":"default","hosting_channel":""},{"bloc_id":"pipi","channel_id":"tui11","channel_name":"tui11","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"pipi","channel_id":"tui12","channel_name":"tui12","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"pipi","channel_id":"robot","channel_name":"机器侠","open_channel_id":"default","hosting_channel":""},{"bloc_id":"pipi","channel_id":"tui13","channel_name":"tui13","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1_son1111","open_channel_id":"tui1_son1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1_son2","open_channel_id":"tui1_son2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui2","channel_name":"tui2","open_channel_id":"tui2_son1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui2","channel_name":"tui2","open_channel_id":"tui2_son2","hosting_channel":""},{"bloc_id":"pipi","channel_id":"tui11","channel_name":"tui11","open_channel_id":"tui1_son1","hosting_channel":""},{"bloc_id":"pipi","channel_id":"tui11","channel_name":"tui11","open_channel_id":"tui110","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui2","channel_name":"tui2","open_channel_id":"tui2_laotie4","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1-11","open_channel_id":"111","hosting_channel":""},{"bloc_id":"tudou","channel_id":"tui4","channel_name":"tui4","open_channel_id":"default","hosting_channel":""},{"bloc_id":"tudou","channel_id":"tui4","channel_name":"tui4","open_channel_id":"hudietui4","hosting_channel":""},{"bloc_id":"pipi","channel_id":"tui12","channel_name":"tui12","open_channel_id":"tui1212","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1-s1","open_channel_id":"s1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"s2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"s3","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"baidu_1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"X1","hosting_channel":""},{"bloc_id":"laot","channel_id":"test_neinei","channel_name":"测试","open_channel_id":"default","hosting_channel":""},{"bloc_id":"pipi","channel_id":"tuiN","channel_name":"tuiN","open_channel_id":"default","hosting_channel":""},{"bloc_id":"tudou","channel_id":"live1","channel_name":"live1","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"huoxing","channel_id":"hx1","channel_name":"hx1","open_channel_id":"default","hosting_channel":""},{"bloc_id":"huoxing","channel_id":"hx2","channel_name":"hx2","open_channel_id":"default","hosting_channel":""},{"bloc_id":"huoxing","channel_id":"hx3","channel_name":"hx3","open_channel_id":"default","hosting_channel":"hx1"},{"bloc_id":"pipi","channel_id":"hx4","channel_name":"hx4","open_channel_id":"default","hosting_channel":"hx1"},{"bloc_id":"huoxing","channel_id":"hx5","channel_name":"hx5","open_channel_id":"default","hosting_channel":""},{"bloc_id":"huoxing","channel_id":"hx6","channel_name":"hx6","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"huoxing","channel_id":"hx7","channel_name":"hx7","open_channel_id":"default","hosting_channel":""},{"bloc_id":"zhubo","channel_id":"zhubo","channel_name":"主播","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"test","channel_name":"test","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"QD1","channel_name":"QD1","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"live3","channel_id":"QD1","channel_name":"QD12","open_channel_id":"QD12","hosting_channel":""},{"bloc_id":"live3","channel_id":"QD3","channel_name":"QD3","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"live3","channel_id":"GD","channel_name":"GD","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"tj_3","hosting_channel":""},{"bloc_id":"new_live","channel_id":"xhm","channel_name":"小红帽","open_channel_id":"default","hosting_channel":""},{"bloc_id":"tiyan","channel_id":"tiyan","channel_name":"tiyan","open_channel_id":"default","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"1","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"2","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"3","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"4","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"5","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"6","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"7","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"8","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"9","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"10","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"11","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"12","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"13","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"14","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"15","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"16","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"17","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"18","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"19","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"20","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"21","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"22","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"23","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"24","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"25","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"26","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"27","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"28","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"29","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"30","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"31","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"32","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"33","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"34","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"35","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"36","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"37","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"38","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"39","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"40","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"41","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"42","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"43","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"44","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"45","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"46","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"47","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"48","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"49","hosting_channel":""},{"bloc_id":"hj","channel_id":"huajiao","channel_name":"huajiao","open_channel_id":"50","hosting_channel":""},{"bloc_id":"pf","channel_id":"pf","channel_name":"泡芙","open_channel_id":"default","hosting_channel":""},{"bloc_id":"youyou","channel_id":"youyou","channel_name":"优优","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"hhhjkk","hosting_channel":""},{"bloc_id":"honx","channel_id":"honx","channel_name":"红杏","open_channel_id":"default","hosting_channel":""},{"bloc_id":"xbt","channel_id":"xbt","channel_name":"xbt","open_channel_id":"default","hosting_channel":""},{"bloc_id":"pipi","channel_id":"tu","channel_name":"tu","open_channel_id":"default","hosting_channel":""},{"bloc_id":"tudou","channel_id":"tui","channel_name":"tui","open_channel_id":"default","hosting_channel":""},{"bloc_id":"fq","channel_id":"fq","channel_name":"番茄","open_channel_id":"default","hosting_channel":""},{"bloc_id":"dcm","channel_id":"dcm","channel_name":"大草莓","open_channel_id":"default","hosting_channel":""},{"bloc_id":"xhd","channel_id":"xhd","channel_name":"小红豆","open_channel_id":"default","hosting_channel":""},{"bloc_id":"xq","channel_id":"xq","channel_name":"小柒","open_channel_id":"default","hosting_channel":""},{"bloc_id":"siji","channel_id":"siji","channel_name":"四季","open_channel_id":"default","hosting_channel":""},{"bloc_id":"ltt","channel_id":"ltt","channel_name":"我测试","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"fd","channel_id":"fd","channel_name":"凤蝶","open_channel_id":"default","hosting_channel":""},{"bloc_id":"liuyue","channel_id":"liuyue","channel_name":"六月","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"test_0608","hosting_channel":""},{"bloc_id":"wy","channel_id":"wy","channel_name":"物业","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"test_0609","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"abcd","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ag","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"s_111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"test_0610","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"abc","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"tj_1","hosting_channel":""},{"bloc_id":"juzi","channel_id":"juzi","channel_name":"句子","open_channel_id":"default","hosting_channel":""},{"bloc_id":"jiujiu","channel_id":"jiujiu","channel_name":"九九","open_channel_id":"default","hosting_channel":""},{"bloc_id":"jiuai","channel_id":"jiuai","channel_name":"旧爱","open_channel_id":"default","hosting_channel":""},{"bloc_id":"xj","channel_id":"xj","channel_name":"橡胶","open_channel_id":"default","hosting_channel":""},{"bloc_id":"miai","channel_id":"miai","channel_name":"密爱","open_channel_id":"default","hosting_channel":""},{"bloc_id":"hc","channel_id":"hc","channel_name":"红尘","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"MMM1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"test","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qqq111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"test6666","hosting_channel":""},{"bloc_id":"mm","channel_id":"mm","channel_name":"美美","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"tu1_1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"aass","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"abaa","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ttt1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ttt2","hosting_channel":""},{"bloc_id":"dx","channel_id":"dx","channel_name":"大秀","open_channel_id":"default","hosting_channel":""},{"bloc_id":"qb","channel_id":"qb","channel_name":"趣播","open_channel_id":"default","hosting_channel":""},{"bloc_id":"qb","channel_id":"qb","channel_name":"qb","open_channel_id":"s2","hosting_channel":""},{"bloc_id":"cy","channel_id":"cy","channel_name":"初夜","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"xxuuww","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"sss1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"a1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"xxoo2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"cccc","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"aaaa","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"xx_22","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"dd_66","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"Android","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"IOS111","hosting_channel":""},{"bloc_id":"ccc","channel_id":"ccc","channel_name":"ccc","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"nbnb","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"kk88","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"kk222","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ldy2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ccxx2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"A_01","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"yyds","hosting_channel":""},{"bloc_id":"test","channel_id":"bointest","channel_name":"波音","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"new_888","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"new_999","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"rose","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"mm111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"5555","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"new111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ddddd","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"rrr1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"hahahaha","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"hello","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"tell","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"and2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"and5","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"and6","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"heiheihei","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qdb4","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qdb5","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qdb2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"tete1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qdb6","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"jjjj","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"anzhuo1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"TT66","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"PPP2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"KKK1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"SSSS","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"AAKK","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"QQWW","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qdtest","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"QQ111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"IOS11","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"manman","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"IISS","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"IIOOSS","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"QQOO","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"AABB","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qdz3","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"QWER","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"QQQQQQ","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"zdxz","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"zzzz","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"dntg1","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"dntg3","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"dntg2","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"dntg4","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"baobaobao","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"C111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"C222","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"C333","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"C888","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"lllll","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ROSS","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"e221","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"D111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"D222","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"D333","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"WWWff","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"d_","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"25","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"1d","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"2k","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"qwer1234","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ssdddaaa","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"asfffffff","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"sssaaaccc","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"_","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"INSTALL","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ananan","hosting_channel":""},{"bloc_id":"huoxing","channel_id":"hx1","channel_name":"hx1","open_channel_id":"ananan","hosting_channel":""},{"bloc_id":"ts","channel_id":"ts","channel_name":"天使","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"eeeeeee","hosting_channel":""},{"bloc_id":"tt","channel_id":"tt","channel_name":"天天","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"OOOPPP","hosting_channel":""},{"bloc_id":"ms","channel_id":"ms","channel_name":"暮色","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"webview","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"XSJ","hosting_channel":""},{"bloc_id":"hy","channel_id":"hy","channel_name":"花样","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"6y6y","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"7k7k","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"GGG","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"AXAX","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"mast","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"OP111","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"OP222","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"lao","hosting_channel":""},{"bloc_id":"live3","channel_id":"xmf","channel_name":"小蜜蜂","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"bobi","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"old_001","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"bobi0301","hosting_channel":""},{"bloc_id":"huoxing","channel_id":"hx1","channel_name":"hx1","open_channel_id":"old_001","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"ALAL","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"JKJK","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"sc001","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"new0307","hosting_channel":""},{"bloc_id":"live3","channel_id":"MK","channel_name":"MK","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"pipi","channel_id":"tui11","channel_name":"tui11","open_channel_id":"old_001","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"new_0309","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"0310bobi","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"BB0313","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"MAS","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"999","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"OOOAAA","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"LALALA","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"laolaolao","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"AQWER","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui2","channel_name":"tui2","open_channel_id":"AQWER","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"new_install","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"OPnew","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"newbao","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"0401bao","hosting_channel":""},{"bloc_id":"live3","channel_id":"KLC","channel_name":"可乐次","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"0404app","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"0405SSS","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"0408qqq","hosting_channel":""},{"bloc_id":"new_live","channel_id":"xhm","channel_name":"xhm","open_channel_id":"LALALA","hosting_channel":""},{"bloc_id":"youyou","channel_id":"youyou","channel_name":"youyou","open_channel_id":"LALALA","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"0411bbb","hosting_channel":""},{"bloc_id":"pf","channel_id":"pf","channel_name":"pf","open_channel_id":"LALALA","hosting_channel":""},{"bloc_id":"live3","channel_id":"ssss","channel_name":"ssss","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"qqqq","channel_name":"qqqq","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"3333","channel_name":"3333","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"5555","channel_name":"5555","open_channel_id":"default","hosting_channel":""},{"bloc_id":"pf","channel_id":"pf","channel_name":"pf","open_channel_id":"0418WWW","hosting_channel":""},{"bloc_id":"live3","channel_id":"lizhi","channel_name":"荔枝","open_channel_id":"default","hosting_channel":"tui1"},{"bloc_id":"live3","channel_id":"1111111","channel_name":"11111111","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"22222","channel_name":"22222","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"33333","channel_name":"33333","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"44444","channel_name":"44444","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"55555","channel_name":"55555","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"666666","channel_name":"666666","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"1","channel_name":"1222","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"2","channel_name":"2","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"tui1","channel_name":"tui1","open_channel_id":"aaaaa","hosting_channel":""},{"bloc_id":"live3","channel_id":"ddd","channel_name":"滴滴滴","open_channel_id":"default","hosting_channel":""},{"bloc_id":"live3","channel_id":"ddd","channel_name":"ddd","open_channel_id":"LALALA","hosting_channel":""},{"bloc_id":"huoxing","channel_id":"hx1","channel_name":"hx1","open_channel_id":"0411bbb","hosting_channel":""},{"bloc_id":"xq","channel_id":"xq","channel_name":"xq","open_channel_id":"0411bbb","hosting_channel":""},{"bloc_id":"pf","channel_id":"pf","channel_name":"pf","open_channel_id":"0411bbb","hosting_channel":""},{"bloc_id":"tudou","channel_id":"tui","channel_name":"tui","open_channel_id":"0411bbb","hosting_channel":""}]}
def test_list_ctl_channel():   #渠道

    path = "/open_api/proxy_api"

    dist = '{"act":"list","ctl":"channel","tm":1654581128}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)

    #if(response.json()["result"][0]["channel_id"] == ""):
        
    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X2V4Y2hhbmdlX2xvZyIsImJlZ2luX3QiOjE2NTE0MDc1NDgsImN0bCI6ImRpYW1vbmRfZXhjaGFuZ2UiLCJlbmRfdCI6MTY1Mjk2Mjc0OCwicGFnZSI6MSwicGFnZV9zaXplIjo1MDAsInRtIjoxNjU0NTgxNDA3fQ==&sign=4498894edb55ff3c4a12648587afa176
#{"act":"list_exchange_log","begin_t":1651407548,"ctl":"diamond_exchange","end_t":1652962748,"page":1,"page_size":500,"tm":1654581407}
#{"code":-1,"msg":"Table 'live3_logs.tb_exchange_log' doesn't exist"}
def test_list_exchange_log():   #鑽石存入

    path = "/open_api/proxy_api"

    dist = '{"act":"list_exchange_log","begin_t":1651407548,"ctl":"diamond_exchange","end_t":1652962748,"page":1,"page_size":500,"tm":1654581407}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)

    #if(response.json()["result"] == {}):
        
    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

"""
def test_list_user_by_id():

    path = "/open_api/proxy_api"

    dist = '{"act":"list_user_by_id","ctl":"user","ids":"[1,2,3]","tm":1654581541}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=baseUrl+path+"?"+queryString)

    if(response.json()["data"][0]["username"] == ""):
        
        print("\n"+baseUrl+path+"?"+queryString+"\n")
        print(dist+"\n")
        print(response.text+"\n")

        assert False

    assert response.status_code == 200
"""

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X2dhbWVfbG9nIiwiYmVnaW5fdGltZSI6MTY2MjU1MzgwMCwiY3RsIjoiZ2FtZV9sb2ciLCJlbmRfdGltZSI6MTY2MjU1NDEwMCwiaGFzX25leHQiOiIwIiwicGFnZSI6MSwicGFnZV9zaXplIjo1MDAsInRiX2luZGV4IjoiMiIsInRtIjoxNjU0NTgxNzA2fQ==&sign=3ae8690e5d51fd10848ea5a094d162bb
#{"act":"list_game_log","begin_time":1662553800,"ctl":"game_log","end_time":1662554100,"has_next":"0","page":1,"page_size":500,"tb_index":"2","tm":1654581706}
#nil
def test_list_game_log():   #遊戲數據

    path = "/open_api/proxy_api"

    dist = '{"act":"list_game_log","begin_time":1662553800,"ctl":"game_log","end_time":1662554100,"has_next":"0","page":1,"page_size":500,"tb_index":"2","tm":1654581706}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    #if(response.json()["result"][0]["user_id"] == ""):
        
    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

        #assert False

    #assert response.status_code == 200

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X2dhbWVfbG9nIiwiYmVnaW5fdGltZSI6MTY2MjU1MzgwMCwiY3RsIjoiZ2FtZV9sb2ciLCJlbmRfdGltZSI6MTY2MjU1NDEwMCwiaGFzX25leHQiOiIwIiwicGFnZSI6MSwicGFnZV9zaXplIjo1MDAsInRiX2luZGV4IjoiMiIsInRtIjoxNjYyNTU3NDE3fQ==&sign=b2ed2a7de63b591a0276792be50a6f26
#{"act":"list_game_log","begin_time":1662553800,"ctl":"game_log","end_time":1662554100,"has_next":"0","page":1,"page_size":500,"tb_index":"2","tm":1662557417}
#nil
def test_list_game_log2():   #遊戲數據

    path = "/open_api/proxy_api"

    dist = '{"act":"list_game_log","begin_time":1662553800,"ctl":"game_log","end_time":1662554100,"has_next":"0","page":1,"page_size":500,"tb_index":"2","tm":1662557417}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=ppbaseUrl+path+"?"+queryString)

    print("\n"+ppbaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

#http://8.219.58.126:10086/open_api/proxy_api?info=eyJhY3QiOiJsaXN0X3RpY2tldF9sb2ciLCJiZWdpbl90aW1lIjoxNjYyNTM1ODM3LCJjdGwiOiJ0aWNrZXRfbG9nIiwiZW5kX3RpbWUiOjE2NjI1Mzk0MzgsInBhZ2UiOjEsInBhZ2Vfc2l6ZSI6NTAwLCJ0bSI6MTY2MjUzOTQzOH0=&sign=07561243643d6518947015db11b85043
#{"act":"list_ticket_log","begin_time":1662535837,"ctl":"ticket_log","end_time":1662539438,"page":1,"page_size":500,"tm":1662539438}
#{"code":-1,"msg":"Table 'live3_logs.tb_ticket_log' doesn't exist"}
def test_list_ticket_log():   #送禮

    path = "/open_api/proxy_api"

    dist = '{"act":"list_ticket_log","begin_time":1662535837,"ctl":"ticket_log","end_time":1662539438,"page":1,"page_size":500,"tm":1662539438}'

    info = genInfo(dist)
    sign = genSignature(info)

    queryString = "info=" + info + "&sign=" + sign

    response = requests.get(url=livebaseUrl+path+"?"+queryString)

    print("\n"+livebaseUrl+path+"?"+queryString+"\n")
    print(dist+"\n")
    print(response.text+"\n")

if __name__ == '__main__': 
    #test_list_fs_daily_stat()
    #test_list_tg_daily_bet_stat()  
    #test_list_tg_daily_fenhong_log()
    #test_list_diamond_log()
    #test_get_online_podcast_count() 
    #test_list_ctl_cash()
    #test_list_ctl_payment()
    #test_list_activity_log()
    #test_list_caipiao_bet()  
    #test_list_ctl_channel()
    #test_list_exchange_log()
    #test_list_game_log()
    #test_list_game_log2()
    #test_list_ticket_log()
   

   

