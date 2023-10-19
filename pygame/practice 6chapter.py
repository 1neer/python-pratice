import tkinter as tk
'''root = tk.Tk()
root.mainloop() tkinter 활용해 윈도우창 띄우기'''

'''root = tk.Tk()
root.title("첫 번째 윈도우")#윈도우창 이름
root.geometry("800x600")#윈도우 창 크기
root.mainloop()'''

'''root = tk.Tk()
root.title("첫 번째 라벨")
root.geometry("800x600")
label = tk.Label(root, text="라벨 문자열", font=("System", 24))#라벨 설정
label.place(x=200, y=100)#라벨이 나올 위치
root.mainloop()'''

import tkinter.font
import random
'''root = tk.Tk()
print(tk.font.families())#폰트들 출력'''

'''root = tk.Tk()
root.title("첫 번째 버튼")#윈도우창 이름
root.geometry("800x600")#윈도우 창 크기
button = tk.Button(root, text="버튼 문자열", font=("Time New Roman", 24))#버튼 설정
button.place(x=200, y=100)#버튼 위치
root.mainloop()'''

'''#버튼 클릭시 트리거되는 함수
def click_btn():
    button["text"] = "클릭했습니다"

root = tk.Tk()
root.title("첫번째 버튼")
root.geometry("800x600")#윈도우 창 크기
button = tk.Button(root, text="클릭하십시오", font=("Time New Roman", 24), command = click_btn)#버튼 설정
button.place(x=200, y=100)#버튼 위치
root.mainloop()'''

"""root = tkinter.Tk()
root.title("첫번째 캔버스")
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="hyunju.png")
canvas.create_image(200, 300, image=gazou)
root.mainloop()"""#이미지 나타내기

'''
#제비뽑기 프로그램
def click_btn():
    label["text"] = random.choice(["대길", "중길", "소길", "흉"])
    label.update()

root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)#윈도우 크기조절 가능여부
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=gazou)
label = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)
button = tkinter.Button(root, text="제비뽑기", font=("Times New Roman", 36), fg="skyblue", command=click_btn)
button.place(x=360, y=400)
root.mainloop()
'''




