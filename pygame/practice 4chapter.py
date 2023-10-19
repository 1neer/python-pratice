import calendar as ca
import datetime as date
import random as ran

#print(ca.month(2020, 2)) 달력 출력
#print(ca.isleap(2020)) 윤년인지 확인
#print(date.date.today()) 오늘이 몇년 몇월 몇일인지
#print(date.datetime.now()) 위에서 더해서 시간 분 초 까지 알려줌
"""d = date.datetime.now()
print(d.hour)
print(d.minute)
print(d.second) 몇시 몇분 몇초인지 따로 알려주는법"""

"""today = date.date.today()
birth = date.date(1971, 2, 2)
print(today - birth) 현재와 태어난 날까지 흐른 일 수"""

"""r = ran.random()
print(r) 난수 생성"""

"""r = ran.randint(1, 6)
print(r) 범위내의 랜덤한 정수 생성"""

"""srp = ran.choice(["가위", "바위", "보"])
print(srp) 리스트 요소중 랜덤으로 뽑음"""

"""cnt = 0
while True:
    r = ran.randint(1, 100)
    print(r)
    cnt = cnt + 1
    if r == 77:
        break
    print(str(cnt) + "번째에 희귀 아이템 겟!")
반복문과 조건문, 랜덤정수뽑기를 이용한 간단한 시뮬"""


