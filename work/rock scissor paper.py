import random
import tkinter
def click():
    rcp = random.choice(["가위", "바위", "보"])
    player["text"] = rcp
    rcp2 = random.choice(["가위", "바위", "보"])
    computer["text"] = rcp2

    if rcp == "가위":
        if rcp2 == "바위":
            result["text"] = "패배"
        elif rcp2 == "보":
            result["text"] = "승리"
        else:
            result["text"] = "Draw"

    elif rcp == "바위":
        if rcp2 == "보":
            result["text"] = "패배"
        elif rcp2 == "가위":
            result["text"] = "승리"
        else:
            result["text"] = "Draw"
    
    elif rcp == "보":
        if rcp2 == "가위":
            result["text"] = "패배"
        elif rcp2 == "바위":
            result["text"] = "승리"
        else:
            result["text"] = "Draw"
    player.update()
    computer.update()
    result.update()
    
root = tkinter.Tk()
root.title("가위 바위 보")
root.resizable(False, False)#윈도우 크기조절 가능여부
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="rcp.png")
canvas.create_image(200, 400, image=gazou)
player = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg="skyblue")
player.place(x=400, y=60)
button = tkinter.Button(root, text="가위바위보", font=("Times New Roman", 36), fg="skyblue", command=click)
button.place(x=400, y=500)
computer = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg="red")
computer.place(x=400, y=260)
result = tkinter.Label(root, text="결과는?", font=("Times New Roman", 70), bg="white")
result.place(x=30, y=60)
root.mainloop()