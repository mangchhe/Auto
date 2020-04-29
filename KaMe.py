import requests # http 요청을 보내는 모듈
import json # 효율적으로 데이터를 저장하고 교환하는데 사용하는 텍스트 데이터 포맷


url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
KAKAO_TOKEN = "P6JJtsuhGMuqkZg0whNVOGhgE6i11CNItnqLngo9c5sAAAFxi6RrTQ"

def send_message(msg): # 카카오톡 메시지 보내기

    header = {"Authorization" : "Bearer " + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": msg,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
    data = {"template_object" : json.dumps(post)}
    return requests.post(url, headers=header, data=data)
