# 开发者：康如帅
# 时间：2023/7/15 16:07
import requests
import datetime

appid = 'wx4310a47e79c9f991'
secret = 'bc24e208bae01dec35e0e9beec51772d'
templateId = 'ArowP5LTs666BHYwBrNS5z_eicA47-nDmxJEckrWUkA' # 模板ID
touserKang = 'oD02T6regpUw7PsH0CJwJz-UsI8c' # 目标微信号
touserZhao = 'oD02T6usvdZB68OHqwlE1yGGcxZo' # 目标微信号

def getAccessToken():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' \
          + appid + '&secret=' + secret
    res = requests.get(url).json()
    print(res['access_token'])
    return res['access_token']

def getWeatherInfo():
    url = "http://t.weather.sojson.com/api/weather/city/101120101"  # 获取用户输入的城市进行查询
    request = url
    re = requests.get(request).json()
    dicts = dict()
    if (re['status'] == 200):
        dicts['weather'] = re['data']['forecast'][0]['type']
        dicts['notice'] = re['data']['forecast'][0]['notice']
        dicts['max_temperature'] = re['data']['forecast'][0]['high'][3:]
        dicts['min_temperature'] = re['data']['forecast'][0]['low'][3:]
    return dicts

def sendMsg(token, dicts, touser):
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    week = week_list[datetime.datetime.now().weekday()]
    date = datetime.datetime.now().strftime('%Y-%m-%d') + week;
    loveday = (datetime.datetime.now() - datetime.datetime.strptime('2021-10-24', '%Y-%m-%d')).days
    msg = {
        "touser": touser,
        "template_id": templateId,
        "data": {
            "date": {
                "value": date,
            },
            "city": {
                "value": "济南",
            },
            "weather": {
                "value": dicts.get('weather'),
            },
            "min_temperature": {
                "value": dicts.get('min_temperature'),
            },
            "max_temperature": {
                "value": dicts.get('max_temperature'),
            },
            "love_day": {
                "value": loveday,
            },
            "notice": {
                "value": dicts.get('notice'),
            }
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + token
    res = requests.post(url=url, json=msg)
    print(res.text)

if __name__ == '__main__':
    dicts = getWeatherInfo()
    token = getAccessToken()
    # sendMsg(token, dicts, touserZhao)
    sendMsg(token, dicts, touserKang)

