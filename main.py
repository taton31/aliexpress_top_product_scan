import requests
import time
from random import random

from save import save_products_to_files

session = requests.Session()

cookies = {
    'xman_f': 'uCOFQxJQTsiObPD31Bk/f7gSajwqR6K18JhC5Ex760+BZ1yqTcmT4WHEMYGXTJOQtXmLp9ray5v+4BUA9akBqRaNJfohwQtt3hvjMiU2R6yOgmWOs+kBOA==',
    'aer_ec': 'HRaIROCC1oGvXL7fQX72ZXWJo8M4M5LBZaN1dKibtdzUqVIn1Ncojn73wPKEb8q1ffbo26R+lscv1Ve3PY8FMmnihfHJQrUK9Jw+QwAlz3c=',
    'aer_abid': '8cf23ef1f9d5b8ee..b4f7b1dfae343273',
    'cna': 'u+02Hv6O7QQCAdWHUFILzm8u',
    'tmr_lvid': 'a11d420cd0d2bcc344a84e363649d656',
    'tmr_lvidTS': '1706033085083',
    '_ym_uid': '170603308595014975',
    '_ym_d': '1710243193',
    '_ga': 'GA1.2.137661743.1710243193',
    'xman_us_f': 'x_locale=en_US&x_l=0&x_c_chg=1&x_c_synced=1&acs_rt=cc48c4cb45ff4c1398af91b08a3de22b',
    'aer_rh': '1443581356',
    'ae_ru_pp_v': '1.0.2',
    'xman_t': 'TOKkcoge11KuRxd/ssA2zI0OYBA4Z9IqVntBjRy8FNZ3GVnBnzkq5rveuIZjf4F1',
    'xlly_s': '1',
    'autoRegion': 'lastGeoUpdate=1722090733&regionCode=917466760000000000&cityCode=917466766582001000&countryCode=RU&postalCode=309850&latitude=50.627&longitude=38.7041',
    '_gid': 'GA1.2.371722810.1722090735',
    '_ym_isad': '1',
    '_ym_visorc': 'b',
    'draftAddress': '%7B%22gps%22%3A%7B%22latitude%22%3A51.164912%2C%22longitude%22%3A37.944218%7D%7D',
    'aer_lang': 'ru_RU',
    'aep_usuc_f': 'b_locale=ru_RU&c_tp=RUB&region=RU&site=rus&province=917466760000000000&city=917466769714000000',
    'a_r_t_info': '%7B%22name%22%3A%22%22%2C%22id%22%3A%22%22%2C%22chinaName%22%3A%22%22%7D',
    '_gat_UA-164782000-1': '1',
    'a_t_info': '%7B%22name%22%3A%22one-price%22%2C%22id%22%3A%22fc044257-c9ea-4e1a-9757-ab160cd97d7c%22%2C%22chinaName%22%3A%22one_price%22%7D',
    'intl_common_forever': 'f8RkvisXNWzyZs4eKU735tTw78LJuAIhaNUcGKq7z3Fcw2h1S3Gb2g==',
    'ali_apache_id': '33.22.87.203.1722091588198.677818.8',
    'JSESSIONID': '34EC3004A03EDF143C529B9B93513622',
    'isg': 'BDEx5CRd82W3Dlx7fFx127MBQL3LHqWQZL73bxNGGvgNOlGMW2zzYt9cXNZc8j3I',
    'tfstk': 'fOIEtwMvbkEF75Qk_Ctygmsm48xpmnFbTgOWETXkdBA3J_Zr49BkFwOBON8lhCdBPJBhEUfCww1PeJpkZ_fyNwa_c9Bp23VfaoZfpgNoXvjeqb6Gcx_BnSZbc9VyVa-aG8eZpRdvE3vHrevgQLJvKLfkrcXM6LpotLm3QOA9E3vkEQ0MILpE-vvogMBhEcJX--qg02VmIyYHi9AhN_sMfjOcKnooqB868J6H_0mlbNVeGIO3kAOJABBHL_ExvHYPrMtGx5qkmZCN4Ex4PJLhUN5JAG2o-IbCOUsp7X0H3HReoMY_0Rx9rNSwAMV-kO6wtE-15PFBPH5FkIL3W5CPQB1lYFcU1Q_fCMYNi5iNwU7lAhj3soSyJbpgrySR8b0y-dpwGRygjlFjnCU47Nu-yFxvQIwBd43J-dpwGRyZy4LMHdRbdp1..',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'bx-v': '2.5.14',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'xman_f=uCOFQxJQTsiObPD31Bk/f7gSajwqR6K18JhC5Ex760+BZ1yqTcmT4WHEMYGXTJOQtXmLp9ray5v+4BUA9akBqRaNJfohwQtt3hvjMiU2R6yOgmWOs+kBOA==; aer_ec=HRaIROCC1oGvXL7fQX72ZXWJo8M4M5LBZaN1dKibtdzUqVIn1Ncojn73wPKEb8q1ffbo26R+lscv1Ve3PY8FMmnihfHJQrUK9Jw+QwAlz3c=; aer_abid=8cf23ef1f9d5b8ee..b4f7b1dfae343273; cna=u+02Hv6O7QQCAdWHUFILzm8u; tmr_lvid=a11d420cd0d2bcc344a84e363649d656; tmr_lvidTS=1706033085083; _ym_uid=170603308595014975; _ym_d=1710243193; _ga=GA1.2.137661743.1710243193; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=1&x_c_synced=1&acs_rt=cc48c4cb45ff4c1398af91b08a3de22b; aer_rh=1443581356; ae_ru_pp_v=1.0.2; xman_t=TOKkcoge11KuRxd/ssA2zI0OYBA4Z9IqVntBjRy8FNZ3GVnBnzkq5rveuIZjf4F1; xlly_s=1; autoRegion=lastGeoUpdate=1722090733&regionCode=917466760000000000&cityCode=917466766582001000&countryCode=RU&postalCode=309850&latitude=50.627&longitude=38.7041; _gid=GA1.2.371722810.1722090735; _ym_isad=1; _ym_visorc=b; draftAddress=%7B%22gps%22%3A%7B%22latitude%22%3A51.164912%2C%22longitude%22%3A37.944218%7D%7D; aer_lang=ru_RU; aep_usuc_f=b_locale=ru_RU&c_tp=RUB&region=RU&site=rus&province=917466760000000000&city=917466769714000000; a_r_t_info=%7B%22name%22%3A%22%22%2C%22id%22%3A%22%22%2C%22chinaName%22%3A%22%22%7D; _gat_UA-164782000-1=1; a_t_info=%7B%22name%22%3A%22one-price%22%2C%22id%22%3A%22fc044257-c9ea-4e1a-9757-ab160cd97d7c%22%2C%22chinaName%22%3A%22one_price%22%7D; intl_common_forever=f8RkvisXNWzyZs4eKU735tTw78LJuAIhaNUcGKq7z3Fcw2h1S3Gb2g==; ali_apache_id=33.22.87.203.1722091588198.677818.8; JSESSIONID=34EC3004A03EDF143C529B9B93513622; isg=BDEx5CRd82W3Dlx7fFx127MBQL3LHqWQZL73bxNGGvgNOlGMW2zzYt9cXNZc8j3I; tfstk=fOIEtwMvbkEF75Qk_Ctygmsm48xpmnFbTgOWETXkdBA3J_Zr49BkFwOBON8lhCdBPJBhEUfCww1PeJpkZ_fyNwa_c9Bp23VfaoZfpgNoXvjeqb6Gcx_BnSZbc9VyVa-aG8eZpRdvE3vHrevgQLJvKLfkrcXM6LpotLm3QOA9E3vkEQ0MILpE-vvogMBhEcJX--qg02VmIyYHi9AhN_sMfjOcKnooqB868J6H_0mlbNVeGIO3kAOJABBHL_ExvHYPrMtGx5qkmZCN4Ex4PJLhUN5JAG2o-IbCOUsp7X0H3HReoMY_0Rx9rNSwAMV-kO6wtE-15PFBPH5FkIL3W5CPQB1lYFcU1Q_fCMYNi5iNwU7lAhj3soSyJbpgrySR8b0y-dpwGRygjlFjnCU47Nu-yFxvQIwBd43J-dpwGRyZy4LMHdRbdp1..',
    'origin': 'https://aliexpress.ru',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://aliexpress.ru/one-price?spm=a2g2w.home.shelf.1.75df5586Tugprf&_immersiveMode=true&bucketId=&ignoreNavigationBar=true&releaseId=&spmC=shelf&spmD=more&wx_navbar_hidden=true&wx_navbar_transparent=true&wx_statusbar_hidden=true',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    '_bx-v': '2.5.14',
}

json_data = {
    'lastIndex': 0,
    'pageIndex': 0,
    'pageSize': 101,
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
        'originalDataSetId': '32708896',
        'floorId': '20151873727',
    },
}

# response = session.post(
#     'https://aliexpress.ru/aer-jsonapi/bx/web/recommend/1pnn-tab',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     json=json_data,
# )

# print (response.text)

for i in range(100):
    json_data['pageIndex'] = i
    response = session.post(
        'https://aliexpress.ru/aer-jsonapi/bx/web/recommend/1pnn-tab',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    for prod in response.json()['data']['products']:
        print (prod['productTitle'], prod['productUrl'], prod['finalPrice'].replace(' ₽', ''), prod['sales'])

    time.sleep(2 + random() * 3)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"lastIndex":0,"pageIndex":3,"pageSize":21,"recommendInfo":{},"scenario":"CountryItem","scenarioParams":{"floorType":"item","skuFetch":"Y","scenario":"CountryItem","useScene":"CAMPAIGN_SOP","sceneId":"2","hyperspaceAllParams":"{\\"hasSwarm\\":\\"0\\",\\"horseRaceRule\\":\\"1|2|3|4|5 |6|7|8|9|10\\",\\"lightPdpSwitchStr\\":\\"1\\"}","summaryOff":"true","countryPrefer":"1","recs_source":"AEG","channel_mode":"bwh_nn_channel","skuType":"bwh_nn","sceneType":"bwh_nn","dataSetId":"33899690","originalDataSetId":"32708896","floorId":"20151873727"}}'
#response = requests.post(
#    'https://aliexpress.ru/aer-jsonapi/bx/web/recommend/1pnn-tab',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)