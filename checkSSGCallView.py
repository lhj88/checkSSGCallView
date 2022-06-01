from urllib.request import Request, urlopen
import re
import datetime
import fcm


dateFormat = '%Y-%m-%d %H:%M:%S'

# 현재시간
now = datetime.datetime.now()
nowStr = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowStr)

# url 리스트
urlList = ['','','','','']

fcmFlag = False
for url in urlList:
    # 1번만 fcm 발송
    if fcmFlag:
        break

    try:
        # url 페이지 크롤링
        req = Request(url)
        res = urlopen(req)
        html = res.read().decode('cp949')

        # DB update 시간 가져옴
        pattern = "d\.viewTime\.innerText = \"([0-9- :]*)\""
        matchOB = re.findall(pattern, html)
        lastUpdateDt = matchOB[0]
        print(lastUpdateDt)

        # 갱신 갭(초) 가져옴
        diffSeconds = (now - datetime.datetime.strptime(lastUpdateDt, dateFormat)).total_seconds()
        print(diffSeconds)

        if diffSeconds > 300:
            print('DB갱신 차이 {0} 발생! ({1})'.format(diffSeconds, lastUpdateDt))
            fcm.sendFCMMessage('DB갱신 차이 {0} 발생! ({1})'.format(diffSeconds, lastUpdateDt))
            fcmFlag = True
    except Exception as e:
        print('오류발생!')
        fcm.sendFCMMessage('오류발생!')
        fcmFlag = True


