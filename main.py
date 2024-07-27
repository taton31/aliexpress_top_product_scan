import requests
import time
from random import random

from save import save_products_to_files

session = requests.Session()
cookies = {
    'xman_t': 'fs3T6UclTxFb4K9cC80V0BhI0zv40rfjBHAg2qYuWKN5eQ/1EgVByw89W/BkhgI7',
    'aep_usuc_f': 'b_locale=ru_RU&c_tp=RUB&region=RU&site=rus&province=917466760000000000&city=917466766582001000',
    'aer_rh': '292856345',
    'acs_usuc_t': 'acs_rt=69aade0a033a43ca8fa08fb5c9d3a417&x_csrf=8ffj1m7nqyxl',
    'xman_f': 'wDSYgUp6uXWGOrbHSyAEFz3yG4H7zvtkf5jwJaVqwUglLRp9EpK9perfr+/YSIw9+h93oSypTDnI8uJIESSL6hvpY5UsKAk4nmQ2iZhXQX0fpiQdd1kf2w==',
    'xman_us_f': 'x_locale=ru_RU&x_l=0&acs_rt=da2fe932758548f18a0876abee9b40fc',
    'intl_common_forever': 'BLYCOLKpqDo4YbXktZBPnYIetpU45KJKxHfwZXx6n/9dVG+FGv5cYg==',
    'ali_apache_id': '33.22.87.192.1722093436131.669850.1',
    'JSESSIONID': '55E6B9435FDAC2CAC7245B4E255B3B9F',
    'aer_ec': 'EWyPpnHAZyCR1c9U3abrh20X3fMxzbFxeDXFj79iTXtl71DMWqpfj8qQKTvI7fnYJnA9Ab3UPn6V4Nq5Y5zV9V0I6kB2/FkKG6mWwS8UWs8=',
    'aer_abid': '94a588f9a952029c..ff233b7e72814c5',
    'a_t_info': '%7B%22name%22%3A%22one-price%22%2C%22id%22%3A%228b1d95b6-8548-47c8-af6c-ccabf3dc4d4d%22%2C%22chinaName%22%3A%22one_price%22%7D',
    'tmr_lvid': 'c43a06be93b65d9553e1af9345d523f4',
    'tmr_lvidTS': '1722093437583',
    'tfstk': 'f_zS9ZTZVLv5-bNjK0Cq5AlgtK0QV8_NPBGLsWLy943-R6wzCpkEY_DKpxNe4Y3zTeabtWPzz_4QmeNgtz5o8_0uZ20dQO7aR7Vo-uRNZ2B4M6hHcnRnXNPuZIevL7PG7HTskSa-pJn-kIhrHXKK2J3vHfDvyXL-9KCjtxHKJv3LMKhr93pp2vhmVCGCVYV5Gfdplh_jp7HX5R4jwDxuwxTpJrZjVALZheLLlbNcR5qp5MkTjYoZB-Q2P2NxO-iaVOT7dWFgvmaBe_yTHkwKioXBAAZLal4q0BK8GyMSXznXt1PTZXeKAoX67bgzcca7q6vYwRk7X4Ve1TPjfoiiMmdB24ra_ymTya9i3ccQhcr5CUwO4xYZCDBDAIiMRjMNGstHYXmh-KM7Z4Jq2jcS0s1Xekm-ijMNGstHx0hmNx5fGLEh.',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'bx-v': '2.5.14',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'xman_t=fs3T6UclTxFb4K9cC80V0BhI0zv40rfjBHAg2qYuWKN5eQ/1EgVByw89W/BkhgI7; aep_usuc_f=b_locale=ru_RU&c_tp=RUB&region=RU&site=rus&province=917466760000000000&city=917466766582001000; aer_rh=292856345; acs_usuc_t=acs_rt=69aade0a033a43ca8fa08fb5c9d3a417&x_csrf=8ffj1m7nqyxl; xman_f=wDSYgUp6uXWGOrbHSyAEFz3yG4H7zvtkf5jwJaVqwUglLRp9EpK9perfr+/YSIw9+h93oSypTDnI8uJIESSL6hvpY5UsKAk4nmQ2iZhXQX0fpiQdd1kf2w==; xman_us_f=x_locale=ru_RU&x_l=0&acs_rt=da2fe932758548f18a0876abee9b40fc; intl_common_forever=BLYCOLKpqDo4YbXktZBPnYIetpU45KJKxHfwZXx6n/9dVG+FGv5cYg==; ali_apache_id=33.22.87.192.1722093436131.669850.1; JSESSIONID=55E6B9435FDAC2CAC7245B4E255B3B9F; aer_ec=EWyPpnHAZyCR1c9U3abrh20X3fMxzbFxeDXFj79iTXtl71DMWqpfj8qQKTvI7fnYJnA9Ab3UPn6V4Nq5Y5zV9V0I6kB2/FkKG6mWwS8UWs8=; aer_abid=94a588f9a952029c..ff233b7e72814c5; a_t_info=%7B%22name%22%3A%22one-price%22%2C%22id%22%3A%228b1d95b6-8548-47c8-af6c-ccabf3dc4d4d%22%2C%22chinaName%22%3A%22one_price%22%7D; tmr_lvid=c43a06be93b65d9553e1af9345d523f4; tmr_lvidTS=1722093437583; tfstk=f_zS9ZTZVLv5-bNjK0Cq5AlgtK0QV8_NPBGLsWLy943-R6wzCpkEY_DKpxNe4Y3zTeabtWPzz_4QmeNgtz5o8_0uZ20dQO7aR7Vo-uRNZ2B4M6hHcnRnXNPuZIevL7PG7HTskSa-pJn-kIhrHXKK2J3vHfDvyXL-9KCjtxHKJv3LMKhr93pp2vhmVCGCVYV5Gfdplh_jp7HX5R4jwDxuwxTpJrZjVALZheLLlbNcR5qp5MkTjYoZB-Q2P2NxO-iaVOT7dWFgvmaBe_yTHkwKioXBAAZLal4q0BK8GyMSXznXt1PTZXeKAoX67bgzcca7q6vYwRk7X4Ve1TPjfoiiMmdB24ra_ymTya9i3ccQhcr5CUwO4xYZCDBDAIiMRjMNGstHYXmh-KM7Z4Jq2jcS0s1Xekm-ijMNGstHx0hmNx5fGLEh.',
    'origin': 'https://aliexpress.ru',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://aliexpress.ru/one-price?bucketId=&debug=true&mixer_rcmd_bucket_id=aerabtestalgoRecommendAbV2_controlRu1&releaseId=&ru_algo_pv_id=e69e98-b97393-aa7814-9725ba-1722092400&scenario=aeg1pnnTabRcmd&traffic_source=recommendation&type_rcmd=core',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

json_data = {
    'lastIndex': 0,
    'pageIndex': 1,
    'pageSize': 21,
    'recommendInfo': {},
    'scenario': 'CountryItem',
    'scenarioParams': {
        'floorType': 'item',
        'skuFetch': 'Y',
        'scenario': 'CountryItem',
        'useScene': 'CAMPAIGN_SOP',
        'sceneId': '2',
        'hyperspaceAllParams': '{"hasSwarm":"0","horseRaceRule":"1|2|3|4|5 |6|7|8|9|10","lightPdpSwitchStr":"1"}',
        'summaryOff': 'true',
        'countryPrefer': '1',
        'recs_source': 'AEG',
        'channel_mode': 'bwh_nn_channel',
        'skuType': 'bwh_nn',
        'sceneType': 'bwh_nn',
        'dataSetId': '33899690',
        'originalDataSetId': '32708901',
        'floorId': '20151873718',
    },
}

params = {
    '_bx-v': '2.5.14',
}

# response = session.post(
#     'https://aliexpress.ru/aer-jsonapi/bx/web/recommend/1pnn-tab',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     json=json_data,
# )

# print (response.text)

res = []
for i in range(100):
    json_data['pageIndex'] = i+1
    response = session.post(
        'https://aliexpress.ru/aer-jsonapi/bx/web/recommend/1pnn-tab',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    for prod in response.json()['data']['products']:

        res.append({'productTitle': prod['productTitle'], 'productUrl': 'https://' + prod['productUrl'][2:], 'finalPrice': prod['finalPrice'].replace(' ₽', ''), 'sales': prod['sales']})
    print(len(res), res[-1]['productTitle'])
    save_products_to_files(res, 'productshome.xlsx', 'products.txt')
    time.sleep(5 + random() * 3)