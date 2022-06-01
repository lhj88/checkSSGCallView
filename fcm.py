from pyfcm import FCMNotification


def sendFCMMessage(msg):
    APIKEY = ""

    # 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
    push_service = FCMNotification(api_key=APIKEY)

    result = push_service.notify_topic_subscribers(topic_name="SSG", message_body=msg)
    print(result)
