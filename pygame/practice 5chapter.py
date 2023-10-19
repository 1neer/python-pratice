#CUI는 캐릭터 유저 인터페이스, GUI는 그래픽 유저 인터페이스
import random as ran
import datetime as date

"""print("유경자 씨의 남편의 이름은?")
ans = input()
if ans == "정현철" or ans == "Hyunchul Jung":
    print("정답입니다")
else:
    print("틀렸습니다")
문자열 조건문과 or 비교연산자"""

"""QUESTION = [
    "유경자 씨의 남편의 이름은?",
    "이경수 씨의 딸의 이름은?",
    "민주희 씨는 이경수 씨와 어떤 관계입니까?"]
R_ANS = ["정현철", "이현지", "조카"]
R_ANS2 = ["Hyunchul Jung", "Hyunji Lee", "niece"]
for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i] or ans == R_ANS2[i]:
        print("정답입니다")
    else:
        print("틀렸습니다")
리스트에 문자열 저장 후 for문을 통해 반복해서 질답시스템
구현"""

"""
#주사위 게임
import random as ran
pl_pos = 6
com_pos = 3
def borad():
    print("•" * (pl_pos - 1) + "P" + "•" * (30 - pl_pos))
    print("•" * (com_pos - 1) + "C" + "•" * (30 - com_pos))
while True: 
    input("Enter를 누르면 플레이어 말이 움직입니다")
    pl_pos = pl_pos + 1 + ran.randint(1, 6)
    if pl_pos > 30:
        pl_pos = 30
    borad()
    if pl_pos == 30:
        print("승리")
        break
    input("Enter를 누르면 컴퓨터 말이 움직입니다")
    com_pos = com_pos + 2 + ran.randint(1, 6)
    if com_pos > 30:
        com_pos = 30
    borad()
    if com_pos == 30:
        print("패배")
        break """

"""
#빠진 알파벳 찾기 게임
ALP = ["A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"]
r = ran.choice(ALP) #문자열 하나 랜덤선택
alp = ""
for i in ALP:
    if i != r: #선택한 문자열이 같지않으면
        alp = alp + i #alp에 추가
print(alp) #결론은 선택된 문자열이 출력안됨
st = date.datetime.now()
ans = input("빠진 알파벳은?")
if ans == r:
    print("정답")
    et = date.datetime.now()
    print((et - st).seconds)
else:
    print("오답")"""

