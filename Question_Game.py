import pgzrun
WIDTH=1000
HEIGHT=600
question = []
q_box = Rect(100,50,800,100)
ans_1 = Rect (61,175,325,175)
ans_2 = Rect (600,175,325,175)
ans_3 = Rect (61,400,325,175)
ans_4 = Rect (600,400,325,175)
timer = Rect (405,175,175,175)
ans = [ans_1,ans_2,ans_3,ans_4]
not_a_skip_box = Rect (405,400,175,175)
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(q_box,"yellow")
    screen.draw.filled_rect(ans_1,"yellow")
    screen.draw.filled_rect(ans_2,"yellow")
    screen.draw.filled_rect(ans_3,"yellow")
    screen.draw.filled_rect(ans_4,"yellow")
    screen.draw.filled_rect(timer,"purple")
    screen.draw.filled_rect(not_a_skip_box,"purple")
    screen.draw.textbox(me_no_english[0],q_box,color = "blue")
    screen.draw.textbox(me_no_english[1],ans_1,color = "blue")
    screen.draw.textbox(me_no_english[2],ans_2,color = "blue")
    screen.draw.textbox(me_no_english[3],ans_3,color = "blue")
    screen.draw.textbox(me_no_english[4],ans_4,color = "blue")
def reddit():
    global me_no_english
    if question:
        me_no_english = write()
        print (question)    
def on_mouse_down(pos):
    number = 1
    for i in ans:
        if i.collidepoint(pos):
            if number==int(me_no_english[5]):
                 pass
            else:
                    print ("HA YOU THINK YOUR SOOOOOOOOO SMART DONT YA KYS ILHAS TEEZY YA ZINGY")
        number = number+1
def quedtions():
    file = open("txt_a.txt","r")
    global question
    for i in file:
        question.append(i)
quedtions()
def write():
    global question
    return question.pop(0).split(",")
me_no_english = write()
print (question)
pgzrun.go()