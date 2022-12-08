import requests as req
import json
from colorama import init, Fore, Back
import datetime
import time
import jsonpath

def timestamp():   #抓取timestamp 
    nowdate = datetime.datetime.today()
    nowdate = nowdate.replace(hour = 0,minute = 0,second = 0)
    day_range = datetime.timedelta(days = 1)
    sec_range = datetime.timedelta(seconds = 1) 
    nowdate = nowdate-day_range  #取前一天 
    timestampnowdate = int(datetime.datetime.timestamp(nowdate))
    #print("nowdate :",nowdate,"timestamp",timestampnowdate)   #開始timestamp
    nowdateEnd = nowdate+day_range-sec_range 
    timestampnowdateEnd = int(datetime.datetime.timestamp(nowdateEnd))
    #print("nowdateEnd :",nowdateEnd,"timestamp",timestampnowdateEnd)   #結束timestamp
    return timestampnowdate, timestampnowdateEnd

def rechargeCashoutDiff():   #会员与财务数据一級頁面---充提差(13) 
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/rechargeCashoutDiff/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    #print(d["data"]["activityDetailCount"])
    print('---------- 会员与财务数据一級頁面---充提差(13) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):         
            if value <= 0:
                print(Fore.RED + key,"NULL value = ",value)
            else:
                print(Fore.GREEN + key,"PASS value = ",value)
   
def newRegCount():   #会员与财务数据一級頁面---新增会员/会员总数(5)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/dataSummary/newRegCount/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 会员与财务数据一級頁面---新增会员/会员总数(5) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int): 
            if key != "activeOnline" and key !="onlineUser" and key!="totalBindCount":             
                if value <= 0:
                    print(Fore.RED + key,"NULL value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)

def firstDayPayRate():   #会员与财务数据一級頁面---付费率(5) 
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/firstDayPayRate/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 会员与财务数据一級頁面---付费率(5) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):      
             if key != "secondRechargeMoney" and key !="secondRecharge" :                  
                if value <= 0:
                    print(Fore.RED + key,"NULL value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)

def gameData():   #游戏数据一級頁面(52) 
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/gameData/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 游戏数据一級頁面(52) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):   
            if key != "djAvailableBetSum" and key !="djCount" and key!="djIncome" and key!="djKillRate" and key!="djTotalBet" and key!="djUserCount":                  
                if abs(value) <= 0:
                    print(Fore.RED + key,"NULL value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)

def agentData():   #代理数据一級頁面(3) 
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/agentData/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 代理数据一級頁面(3) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):   
            if key != "agentAvailableBetNum"and key !="agentSubChannelCount"and key!="agentUserCount"and key!="totalAgentTotalBonus"and key!="totalAgentGameBonus"and key!="totalAgentLiveBonus":                  
                if abs(value) <= 0:
                    print(Fore.RED + key,"NULL value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)

def podcastDiamond():   #直播数据一級頁面(9)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/podcastDiamond/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 直播数据一級頁面(9) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):   
            if key != "podcastTotalTicket" and key !="compareRechargeDiamond" :                  
                if abs(value) <= 0:
                    print(Fore.RED + key,"NULL value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)

def diamondConsumption():   #钻石消耗一級頁面(2)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/diamondConsumption/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 钻石消耗一級頁面(2) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):                            
            if abs(value) <= 0:
                print(Fore.RED + key,"NULL value = ",value)
            else:
                print(Fore.GREEN + key,"PASS value = ",value)

def profiles():   #會員與財務數據二級頁面---會員數據(3)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/users/profiles/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 會員與財務數據二級頁面---會員數據(3) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):                            
            if abs(value) <= 0:
                print(Fore.RED + key,"NULL value = ",value)
            else:
                print(Fore.GREEN + key,"PASS value = ",value)

def online():   #會員與財務數據二級頁面---在線與活躍(3)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/users/online/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 會員與財務數據二級頁面---在線與活躍(3) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):   
            if key != "totalActive" and key !="totalOnline" :                           
                if abs(value) <= 0:
                    print(Fore.RED + key,"NULL value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)

def recharge():   #會員與財務數據二級頁面---首充/二充數據(20)   
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/users/recharge/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 會員與財務數據二級頁面---首充/二充數據(20) ----------')
    firstRechargeCount = []
    secondRechargeCount = []
    firstRechargeRate = []
    secondRechargeRate = []
    dict_temp = json.loads(r.content.decode())
    firstRechargeCount.extend(jsonpath.jsonpath(dict_temp, '$..firstRechargeCount'))
    secondRechargeCount.extend(jsonpath.jsonpath(dict_temp, '$..secondRechargeCount'))
    firstRechargeRate.extend(jsonpath.jsonpath(dict_temp, '$..firstRechargeRate'))
    secondRechargeRate.extend(jsonpath.jsonpath(dict_temp, '$..secondRechargeRate'))   
    if abs(firstRechargeCount[1]) <= 0:
        print(Fore.RED + "firstRechargeCount[3日首充人數]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeCount[3日首充人數]","PASS ")
    if abs(firstRechargeCount[2]) <= 0:
        print(Fore.RED + "firstRechargeCount[5日首充人數]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeCount[5日首充人數]","PASS ")
    if abs(firstRechargeCount[3]) <= 0:
        print(Fore.RED + "firstRechargeCount[7日首充人數]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeCount[7日首充人數]","PASS ")
    if abs(firstRechargeCount[4]) <= 0:
        print(Fore.RED + "firstRechargeCount[14日首充人數]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeCount[14日首充人數]","PASS ")
    if abs(firstRechargeCount[5]) <= 0:
        print(Fore.RED + "firstRechargeCount[30日首充人數]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeCount[30日首充人數]","PASS ") 
    if abs(secondRechargeCount[1]) <= 0:
        print(Fore.RED + "secondRechargeCount[3日二充人數]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeCount[3日二充人數]","PASS ")

    if abs(secondRechargeCount[2]) <= 0:
        print(Fore.RED + "secondRechargeCount[5日二充人數]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeCount[5日二充人數]","PASS ")
    if abs(secondRechargeCount[3]) <= 0:
        print(Fore.RED + "secondRechargeCount[7日二充人數]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeCount[7日二充人數]","PASS ")
    if abs(secondRechargeCount[4]) <= 0:
        print(Fore.RED + "secondRechargeCount[14日二充人數]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeCount[14日二充人數]","PASS ")
    if abs(secondRechargeCount[5]) <= 0:
        print(Fore.RED + "secondRechargeCount[30日二充人數]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeCount[30日二充人數]","PASS ") 
    if abs(firstRechargeRate[1]) <= 0:
        print(Fore.RED + "firstRechargeRate[3日首充率]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeRate[3日首充率]","PASS ")

    if abs(firstRechargeRate[2]) <= 0:
        print(Fore.RED + "firstRechargeRate[5日首充率]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeRate[5日首充率]","PASS ")
    if abs(firstRechargeRate[3]) <= 0:
        print(Fore.RED + "firstRechargeRate[7日首充率]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeRate[7日首充率]","PASS ")
    if abs(firstRechargeRate[4]) <= 0:
        print(Fore.RED + "firstRechargeRate[14日首充率]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeRate[14日首充率]","PASS ")
    if abs(firstRechargeRate[5]) <= 0:
        print(Fore.RED + "firstRechargeRate[30日首充率]","NULL ")
    else:
        print(Fore.GREEN + "firstRechargeRate[30日首充率]","PASS ")
    if abs(secondRechargeRate[1]) <= 0:
        print(Fore.RED + "secondRechargeRate[3日二充轉換]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeRate[3日二充轉換]","PASS ")

    if abs(secondRechargeRate[2]) <= 0:
        print(Fore.RED + "secondRechargeRate[5日二充轉換]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeRate[5日二充轉換]","PASS ")
    if abs(secondRechargeRate[3]) <= 0:
        print(Fore.RED + "secondRechargeRate[7日二充轉換]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeRate[7日二充轉換]","PASS ")
    if abs(secondRechargeRate[4]) <= 0:
        print(Fore.RED + "secondRechargeRate[14日二充轉換]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeRate[14日二充轉換]","PASS ")
    if abs(secondRechargeRate[5]) <= 0:
        print(Fore.RED + "secondRechargeRate[30日二充轉換]","NULL ")
    else:
        print(Fore.GREEN + "secondRechargeRate[30日二充轉換]","PASS ")

def gameblocks():   #遊戲數據二級頁面(4)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/bets/blocks'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 遊戲數據二級頁面(4) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):                       
            if abs(value) <= 0:
                print(Fore.RED + key,"NULL value = ",value)
            else:
                print(Fore.GREEN + key,"PASS value = ",value)

def liveblocks():   #直播數據二級頁面(15)---钻石支出类型(8)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/stream/blocks'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 直播數據二級頁面(15) ----------')
    for key, value in d["data"].items():
        t = type(value)
        if (t == float or t == int):                     
            if abs(value) <= 0:
                print(Fore.RED + key,"NULL value = ",value)
            else:
                print(Fore.GREEN + key,"PASS value = ",value)
    print('---------- 直播數據二級頁面---钻石支出类型(8) ----------')
    giftGiving = []
    itemBuy = []
    routineConsumption = []
    byLiveConsumption = []
    barrage = []
    buyVip = []
    proceedVip = []
    totalUsedDiamond = []
    dict_temp = json.loads(r.content.decode())
    giftGiving.extend(jsonpath.jsonpath(dict_temp, '$..giftGiving'))
    itemBuy.extend(jsonpath.jsonpath(dict_temp, '$..itemBuy'))
    routineConsumption.extend(jsonpath.jsonpath(dict_temp, '$..routineConsumption'))
    byLiveConsumption.extend(jsonpath.jsonpath(dict_temp, '$..byLiveConsumption'))
    barrage.extend(jsonpath.jsonpath(dict_temp, '$..barrage'))
    buyVip.extend(jsonpath.jsonpath(dict_temp, '$..buyVip'))
    proceedVip.extend(jsonpath.jsonpath(dict_temp, '$..proceedVip'))
    totalUsedDiamond.extend(jsonpath.jsonpath(dict_temp, '$..totalUsedDiamond')) 
    if (giftGiving) == 0:
        print(Fore.RED + "giftGiving","NULL ")
    else:
        print(Fore.GREEN + "giftGiving","PASS ")
    if (itemBuy) == 0:
        print(Fore.RED + "itemBuy","NULL ")
    else:
        print(Fore.GREEN + "itemBuy","PASS ")
    if (routineConsumption) == 0:
        print(Fore.RED + "routineConsumption","NULL ")
    else:
        print(Fore.GREEN + "routineConsumption","PASS ")
    if (byLiveConsumption) == 0:
        print(Fore.RED + "byLiveConsumption","NULL ")
    else:
        print(Fore.GREEN + "byLiveConsumption","PASS ")
    if (barrage) == 0:
        print(Fore.RED + "barrage","NULL ")
    else:
        print(Fore.GREEN + "barrage","PASS ")
    if (buyVip) == 0:
        print(Fore.RED + "buyVip","NULL ")
    else:
        print(Fore.GREEN + "buyVip","PASS ")
    if (proceedVip) == 0:
        print(Fore.RED + "proceedVip","NULL ")
    else:
        print(Fore.GREEN + "proceedVip","PASS ")
    if (totalUsedDiamond) == 0:
        print(Fore.RED + "totalUsedDiamond","NULL ")
    else:
        print(Fore.GREEN + "totalUsedDiamond","PASS ")

businessReportCheckList = ['tui1']
businessReportcheckkeylist = ['regCount', 'recharge', 'firstRecharge','firstRechargeCount','cash','exchangeDiamond','rechargeCashDiff','cashRechargeRate','winBetDiff','winBetDiffRechargeRate','betSum','availableBetSum','totalBindCount','fsMoneyt','fsMoney','totalUserCount']
def businessReport():   #經營報表---統計(15)---商戶tui1(15)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/businessReport/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 經營報表---統計(15) ----------')
    for key, value in d["totalData"].items():
        t = type(value)
        if (t == float or t == int):  
            if key !="playerCount":                     
                if abs(value) == 0:
                    print(Fore.RED + key,"Error value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)
        elif(value == "null"):
            print(Fore.RED + key,"Error value = ",value)
    print('---------- 經營報表---商戶tui1(15) ----------')
    dict_temp = json.loads(r.content.decode()) 
    for item in dict_temp['data']:
         for CheckGameName in businessReportCheckList:
            if item['channelId'] == CheckGameName:
                businessReportcheckGAMEValue( CheckGameName, item.items())

def businessReportcheckGAMEValue(gamename, itemlist):
    for item_key , value in itemlist:
        for key in businessReportcheckkeylist:
            if  key == item_key:
                if  value == 0:
                    color = Fore.RED
                    result = " ERROR "
                else:
                    color = Fore.GREEN
                    result = " PASS "
                print(color, gamename, key, " value = ", value, result) 

def dailyReport():   #日報表(7)---遊戲數據(5)---遊戲數據(48)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/dailyReport/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{ "channelId": "","openChannelId": "","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"channelId": "","openChannelId": "","pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 日報表(7) ----------')
    recharge = []
    cashout = []
    diamondRecharge = []
    diamondRechargeCount = []
    diamondUse = []
    diamondGift = []
    activityMoney = []
    dict_temp = json.loads(r.content.decode())
    recharge.extend(jsonpath.jsonpath(dict_temp, '$..recharge'))
    cashout.extend(jsonpath.jsonpath(dict_temp, '$..cashout'))
    diamondRecharge.extend(jsonpath.jsonpath(dict_temp, '$..diamondRecharge'))
    diamondRechargeCount.extend(jsonpath.jsonpath(dict_temp, '$..diamondRechargeCount'))
    diamondUse.extend(jsonpath.jsonpath(dict_temp, '$..diamondUse'))
    diamondGift.extend(jsonpath.jsonpath(dict_temp, '$..diamondGift'))
    activityMoney.extend(jsonpath.jsonpath(dict_temp, '$..activityMoney'))
    if abs(recharge[0]) <= 0:
        print(Fore.RED + "recharge","NULL ")
    else:
        print(Fore.GREEN + "recharge","PASS ")
    if abs(cashout[0]) <= 0:
        print(Fore.RED + "cashout","NULL ")
    else:
        print(Fore.GREEN + "cashout","PASS ")
    if abs(diamondRecharge[0]) <= 0:
        print(Fore.RED + "diamondRecharge","NULL ")
    else:
        print(Fore.GREEN + "diamondRecharge","PASS ")
    if abs(diamondRechargeCount[0]) <= 0:
        print(Fore.RED + "diamondRechargeCount","NULL ")
    else:
        print(Fore.GREEN + "diamondRechargeCount","PASS ")
    if abs(diamondUse[0]) <= 0:
        print(Fore.RED + "diamondUse","NULL ")
    else:
        print(Fore.GREEN + "diamondUse","PASS ")
    if abs(diamondGift[0]) <= 0:
        print(Fore.RED + "diamondGift","NULL ")
    else:
        print(Fore.GREEN + "diamondGift","PASS ")
    if abs(activityMoney[0]) <= 0:
        print(Fore.RED + "activityMoney","NULL ")
    else:
        print(Fore.GREEN + "activityMoney","PASS ")
    print('---------- 日報表---遊戲數據(5) ----------')
    bet = []
    availableBetSum = []
    income = []
    betUserCount = []
    fsMoney = []
    dict_temp = json.loads(r.content.decode())
    availableBetSum.extend(jsonpath.jsonpath(dict_temp, '$..availableBetSum'))
    income.extend(jsonpath.jsonpath(dict_temp, '$..income'))
    bet.extend(jsonpath.jsonpath(dict_temp, '$..bet'))
    betUserCount.extend(jsonpath.jsonpath(dict_temp, '$..betUserCount'))
    fsMoney.extend(jsonpath.jsonpath(dict_temp, '$..fsMoney'))
    if abs(bet[0]) <= 0:
        print(Fore.RED + "bet","NULL ")
    else:
        print(Fore.GREEN + "bet","PASS ")
    if abs(availableBetSum[0]) <= 0:
        print(Fore.RED + "availableBetSum","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum","PASS ")
    if abs(income[0]) <= 0:
        print(Fore.RED + "income","NULL ")
    else:
        print(Fore.GREEN + "income","PASS ")
    if abs(betUserCount[0]) <= 0:
        print(Fore.RED + "betUserCount","NULL ")
    else:
        print(Fore.GREEN + "betUserCount","PASS ")
    if abs(fsMoney[0]) <= 0:
        print(Fore.RED + "fsMoney","NULL ")
    else:
        print(Fore.GREEN + "fsMoney","PASS ")
    print('---------- 日報表---遊戲數據(48) ----------')
    killRate = []
    betCount = []
    betUserCount = []
    bet = []
    availableBetSum = []
    income = []
    dict_temp = json.loads(r.content.decode())
    killRate.extend(jsonpath.jsonpath(dict_temp, '$..killRate'))
    betCount.extend(jsonpath.jsonpath(dict_temp, '$..betCount'))
    betUserCount.extend(jsonpath.jsonpath(dict_temp, '$..betUserCount'))
    bet.extend(jsonpath.jsonpath(dict_temp, '$..bet'))
    availableBetSum.extend(jsonpath.jsonpath(dict_temp, '$..availableBetSum'))
    income.extend(jsonpath.jsonpath(dict_temp, '$..income'))  
    if abs(killRate[0]) <= 0:
        print(Fore.RED + "killRate[波音彩票]","NULL ")
    else:
        print(Fore.GREEN + "killRate[波音彩票]","PASS ")
    if abs(betCount[0]) <= 0:
        print(Fore.RED + "betCount[波音彩票]","NULL ")
    else:
        print(Fore.GREEN + "betCount[波音彩票]","PASS ")
    if abs(betUserCount[1]) <= 0:
        print(Fore.RED + "betUserCount[波音彩票]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[波音彩票]","PASS ")
    if abs(bet[1]) <= 0:
        print(Fore.RED + "bet[波音彩票]","NULL ")
    else:
        print(Fore.GREEN + "bet[波音彩票]","PASS ")
    if abs(availableBetSum[1]) <= 0:
        print(Fore.RED + "availableBetSum[波音彩票]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[波音彩票]","PASS ")
    if abs(income[1]) <= 0:
        print(Fore.RED + "income[波音彩票]","NULL ")
    else:
        print(Fore.GREEN + "income[波音彩票]","PASS ")  
    if abs(killRate[1]) <= 0:
        print(Fore.RED + "killRate[彩票]","NULL ")
    else:
        print(Fore.GREEN + "killRate[彩票]","PASS ")
    if abs(betCount[1]) <= 0:
        print(Fore.RED + "betCount[彩票]","NULL ")
    else:
        print(Fore.GREEN + "betCount[彩票]","PASS ")
    if abs(betUserCount[2]) <= 0:
        print(Fore.RED + "betUserCount[彩票]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[彩票]","PASS ")
    if abs(bet[2]) <= 0:
        print(Fore.RED + "bet[彩票]","NULL ")
    else:
        print(Fore.GREEN + "bet[彩票]","PASS ")
    if abs(availableBetSum[2]) <= 0:
        print(Fore.RED + "availableBetSum[彩票]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[彩票]","PASS ")
    if abs(income[2]) <= 0:
        print(Fore.RED + "income[彩票]","NULL ")
    else:
        print(Fore.GREEN + "income[彩票]","PASS ")
    if abs(killRate[2]) <= 0:
        print(Fore.RED + "killRate[真人]","NULL ")
    else:
        print(Fore.GREEN + "killRate[真人]","PASS ")
    if abs(betCount[2]) <= 0:
        print(Fore.RED + "betCount[真人]","NULL ")
    else:
        print(Fore.GREEN + "betCount[真人]","PASS ")
    if abs(betUserCount[3]) <= 0:
        print(Fore.RED + "betUserCount[真人]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[真人]","PASS ")
    if abs(bet[3]) <= 0:
        print(Fore.RED + "bet[真人]","NULL ")
    else:
        print(Fore.GREEN + "bet[真人]","PASS ")
    if abs(availableBetSum[3]) <= 0:
        print(Fore.RED + "availableBetSum[真人]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[真人]","PASS ")
    if abs(income[3]) <= 0:
        print(Fore.RED + "income[真人]","NULL ")
    else:
        print(Fore.GREEN + "income[真人]","PASS ")
    if abs(killRate[3]) <= 0:
        print(Fore.RED + "killRate[电子]","NULL ")
    else:
        print(Fore.GREEN + "killRate[电子]","PASS ")
    if abs(betCount[3]) <= 0:
        print(Fore.RED + "betCount[电子]","NULL ")
    else:
        print(Fore.GREEN + "betCount[电子]","PASS ")
    if abs(betUserCount[4]) <= 0:
        print(Fore.RED + "betUserCount[电子]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[电子]","PASS ")
    if abs(bet[4]) <= 0:
        print(Fore.RED + "bet[电子]","NULL ")
    else:
        print(Fore.GREEN + "bet[电子]","PASS ")
    if abs(availableBetSum[4]) <= 0:
        print(Fore.RED + "availableBetSum[电子]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[电子]","PASS ")
    if abs(income[4]) <= 0:
        print(Fore.RED + "income[电子]","NULL ")
    else:
        print(Fore.GREEN + "income[电子]","PASS ")   
    if abs(killRate[4]) <= 0:
        print(Fore.RED + "killRate[捕鱼]","NULL ")
    else:
        print(Fore.GREEN + "killRate[捕鱼]","PASS ")
    if abs(betCount[4]) <= 0:
        print(Fore.RED + "betCount[捕鱼]","NULL ")
    else:
        print(Fore.GREEN + "betCount[捕鱼]","PASS ")
    if abs(betUserCount[5]) <= 0:
        print(Fore.RED + "betUserCount[捕鱼]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[捕鱼]","PASS ")
    if abs(bet[5]) <= 0:
        print(Fore.RED + "bet[捕鱼]","NULL ")
    else:
        print(Fore.GREEN + "bet[捕鱼]","PASS ")
    if abs(availableBetSum[5]) <= 0:
        print(Fore.RED + "availableBetSum[捕鱼]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[捕鱼]","PASS ")
    if abs(income[5]) <= 0:
        print(Fore.RED + "income[捕鱼]","NULL ")
    else:
        print(Fore.GREEN + "income[捕鱼]","PASS ")   
    if abs(killRate[5]) <= 0:
        print(Fore.RED + "killRate[体育]","NULL ")
    else:
        print(Fore.GREEN + "killRate[体育]","PASS ")
    if abs(betCount[5]) <= 0:
        print(Fore.RED + "betCount[体育]","NULL ")
    else:
        print(Fore.GREEN + "betCount[体育]","PASS ")
    if abs(betUserCount[6]) <= 0:
        print(Fore.RED + "betUserCount[体育]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[体育]","PASS ")
    if abs(bet[6]) <= 0:
        print(Fore.RED + "bet[体育]","NULL ")
    else:
        print(Fore.GREEN + "bet[体育]","PASS ")
    if abs(availableBetSum[6]) <= 0:
        print(Fore.RED + "availableBetSum[体育]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[体育]","PASS ")
    if abs(income[6]) <= 0:
        print(Fore.RED + "income[体育]","NULL ")
    else:
        print(Fore.GREEN + "income[体育]","PASS ")  
    if abs(killRate[6]) <= 0:
        print(Fore.RED + "killRate[棋牌]","NULL ")
    else:
        print(Fore.GREEN + "killRate[棋牌]","PASS ")
    if abs(betCount[6]) <= 0:
        print(Fore.RED + "betCount[棋牌]","NULL ")
    else:
        print(Fore.GREEN + "betCount[棋牌]","PASS ")
    if abs(betUserCount[7]) <= 0:
        print(Fore.RED + "betUserCount[棋牌]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[棋牌]","PASS ")
    if abs(bet[7]) <= 0:
        print(Fore.RED + "bet[棋牌]","NULL ")
    else:
        print(Fore.GREEN + "bet[棋牌]","PASS ")
    if abs(availableBetSum[7]) <= 0:
        print(Fore.RED + "availableBetSum[棋牌]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[棋牌]","PASS ")
    if abs(income[7]) <= 0:
        print(Fore.RED + "income[棋牌]","NULL ")
    else:
        print(Fore.GREEN + "income[棋牌]","PASS ")  
    if abs(killRate[7]) <= 0:
        print(Fore.RED + "killRate[其他]","NULL ")
    else:
        print(Fore.GREEN + "killRate[其他]","PASS ")
    if abs(betCount[7]) <= 0:
        print(Fore.RED + "betCount[其他]","NULL ")
    else:
        print(Fore.GREEN + "betCount[其他]","PASS ")
    if abs(betUserCount[8]) <= 0:
        print(Fore.RED + "betUserCount[其他]","NULL ")
    else:
        print(Fore.GREEN + "betUserCount[其他]","PASS ")
    if abs(bet[8]) <= 0:
        print(Fore.RED + "bet[其他]","NULL ")
    else:
        print(Fore.GREEN + "bet[其他]","PASS ")
    if abs(availableBetSum[8]) <= 0:
        print(Fore.RED + "availableBetSum[其他]","NULL ")
    else:
        print(Fore.GREEN + "availableBetSum[其他]","PASS ")
    if abs(income[8]) <= 0:
        print(Fore.RED + "income[其他]","NULL ")
    else:
        print(Fore.GREEN + "income[其他]","PASS ")

gameBetCheckList = ['波音彩票']
gameBetcheckkeylist = ['betCount', 'betSum', 'availableBetSum','income','killRate','ticketForPodcast']
def gameBet():   #遊戲注單列表---統計(6)---波音彩票(6)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/gameBet/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data)  
    d = json.loads(r.text)
    print('---------- 遊戲注單列表---統計(6) ----------')
    for key, value in d["totalData"].items():
        t = type(value)
        if (t == float or t == int):                       
            if abs(value) <= 0:
                print(Fore.RED + key,"NULL value = ",value)
            else:
                print(Fore.GREEN + key,"PASS value = ",value)
    print('---------- 遊戲注單列表---波音彩票(6) ----------')
    dict_temp = json.loads(r.content.decode()) 
    for item in dict_temp['data']:
         for CheckGameName in gameBetCheckList:
            if item['gameTypeName'] == CheckGameName:
                gameBetcheckGAMEValue( CheckGameName, item.items())

def gameBetcheckGAMEValue(gamename, itemlist):
    for item_key , value in itemlist:
        for key in gameBetcheckkeylist:
            if  key == item_key:
                if  value == 0:
                    color = Fore.RED
                    result = " ERROR "
                else:
                    color = Fore.GREEN
                    result = " PASS "
                print(color, gamename, key, " value = ", value, result)  

gameBetDetailCheckList = ['六合','時時彩']
gameBetDetailcheckkeylist = ['betCount', 'betNum', 'availableBetNum','income','killRate']
def gameBetDetail():   #遊戲數據列表---統計---(5)---波音彩票---六合(5)
    url = 'http://8.219.83.66:8088/admin/v2/login'
    headers={ 
        "Content-Type": "application/json"
    }
    data = '{"password":"1234","username":"admin"}'
    r = req.post(url,headers=headers,data=data)
    d = json.loads(r.text)
    token = d ["token"]
    url = 'http://8.219.83.66:8088/admin/dataCenter/gameBetDetail/'
    headers={ 
        "Content-Type": "application/json",
        "Authorization": token
    }
    timestampnowdate, timestampnowdateEnd = timestamp()
    data = '{"pageNum":"1","pageSize":"10000","beginTime":' + str(timestampnowdate) +"000"',"endTime":' + str(timestampnowdateEnd) +"000" '}'
    #data = '{"pageNum":"1","pageSize":"10000","beginTime":"1661961600000","endTime":"1662047999999"}'
    r = req.post(url,headers=headers,data=data) 
    d = json.loads(r.text)
    print('---------- 遊戲數據列表---統計---(5) ----------')
    for key, value in d["totalData"].items():
        t = type(value)
        if (t == float or t == int):  
            if key !="tip":                     
                if abs(value) <= 0:
                    print(Fore.RED + key,"NULL value = ",value)
                else:
                    print(Fore.GREEN + key,"PASS value = ",value)
    print('---------- 遊戲數據列表---波音彩票---六合(5) ----------')
    dict_temp = json.loads(r.content.decode()) 
    for item in dict_temp['data']:
        for CheckGameName in gameBetDetailCheckList:
            if item['gameName'] == CheckGameName:
                gameBetDetailcheckGAMEValue( CheckGameName, item.items())
                
def gameBetDetailcheckGAMEValue(gamename, itemlist):
    for item_key , value in itemlist:
        for key in gameBetDetailcheckkeylist:
            if  key == item_key:
                if  value == 0:
                    color = Fore.RED
                    result = " ERROR "
                else:
                    color = Fore.GREEN
                    result = " PASS "
                print(color, gamename, key, " value = ", value, result)   

if __name__ == '__main__': 
    timestamp()                #抓取timestamp
    rechargeCashoutDiff()      #会员与财务数据一級頁面---充提差(13) 
    newRegCount()              #会员与财务数据一級頁面---新增会员/会员总数(5)
    firstDayPayRate()          #会员与财务数据一級頁面---付费率(5)
    gameData()                 #游戏数据一級頁面(52)
    agentData()                #代理数据一級頁面(3)
    podcastDiamond()           #直播数据一級頁面(9)
    diamondConsumption()       #钻石消耗一級頁面(2)
    profiles()                 #會員與財務數據二級頁面---會員數據(3)
    online()                   #會員與財務數據二級頁面---在線與活躍(3)
    recharge()                 #會員與財務數據二級頁面---首充/二充數據(20)
    gameblocks()               #遊戲數據二級頁面(4)
    liveblocks()               #直播數據二級頁面(15)---钻石支出类型(8)
    businessReport()           #經營報表---統計(15)---商戶tui1(15)v
    dailyReport()              #日報表(7)---遊戲數據(5)---遊戲數據(48)
    gameBet()                  #遊戲注單列表---統計(6)---波音彩票(6)v
    gameBetDetail()            #遊戲數據列表---統計---(5)---波音彩票---六合(5)v

