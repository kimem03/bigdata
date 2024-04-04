import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd

# 열린데이터광장 API 키
ServiceKey = "6b634174716b696d36346e564c5662"

# 요청 URL 생성 함수
def getRequestUrl(url):    
    req = urllib.request.Request(url)    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
        else:
            print("[%s] Error for URL : %s, Response Code: %s" % (datetime.datetime.now(), url, response.getcode()))
            return None
    except urllib.error.URLError as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        print(e.reason)
        return None
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        print(e)
        return None


# 열린데이터광장 API를 통해 데이터 가져오기
def getSeoulOpenData(search_key, start_page=1, end_page=10):
    base_url = "http://openapi.seoul.go.kr:8088/{key}/json/{search_key}/{start_page}/{end_page}/".format(
        key=ServiceKey,
        search_key=search_key,
        start_page=start_page,
        end_page=end_page
    )
    return getRequestUrl(base_url)

# 메인 함수
def main():
    jsonResult = []
    result = []

    print("<< 서울 열린데이터광장에서 데이터를 수집합니다. >>")
    search_key = input('데이터를 검색할 키워드를 입력하세요: ')
    start_page = int(input('시작 페이지를 입력하세요: '))
    end_page = int(input('종료 페이지를 입력하세요: '))

    # 서울 열린데이터광장 API로 데이터 수집
    data = getSeoulOpenData(search_key, start_page, end_page)
    print(data)  # 데이터 출력
    data_dict = json.loads(data)
    print(data_dict.keys())  # 반환된 데이터의 키 출력
    # 데이터 처리 코드를 여기에 추가

if __name__ == '__main__':
    main()


