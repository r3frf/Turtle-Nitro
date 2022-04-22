from turtle import Turtle,Screen
import time
import random
COLOR=["red", "orange", "yellow", "green", "blue", "purple"]
MOVE=8

class Score_board():
    def __init__(self):
        self.sc=Turtle()
        self.sc.hideturtle()
        self.sc.penup()
        self.score=1
        self.sc.goto(x=-280, y=280)
        self.update()


    def increase_score(self):
        self.score = self.score + 1
        self.sc.clear()
        self.update()

    def update(self):

        self.sc.write(f" level=>{self.score}", font=(25))

    def game_over(self):
        self.tc=Turtle()
        self.tc.hideturtle()
        self.tc.write(f" the game is over \n the score is => {self.score}", align="center", font=(25))




S=Score_board()






class car():
    def __init__(self):
        self.a=[]
    def creation(self):
        if random.randint(1,6)==2 or random.randint(1,6)==4 or random.randint(1,6)==6 or random.randint(1,6)==1 :
            self.T = Turtle(shape="square")
            self.T.color("white")
            self.T.goto(350,0)
            self.b=self.T.speed("fastest")
            self.T.penup()
            self.T.shapesize(stretch_wid=1, stretch_len=2)
            self.T.speed("fastest")
            self.T.color(random.choice(COLOR))
            self.T.goto(300,random.randint(-250,280))
            self.a.append(self.T)
            self.A=15
            self.B=self.A
    def move(self):
        for i in self.a:
            i.backward(self.B)
    def level(self):
        self.B=self.A+self.A




'''        self.newx = self.T.xcor() - random.randint(10)
        self.newy = self.T.ycor()
        self.T.goto(self.newx, self.newy)
'''
class tur():
    def __init__(self):

        self.T=Turtle(shape="turtle")
        self.T.color("black")
        self.T.penup()
        self.T.goto(0,-280)
        self.T.left(90)


    def up(self):

        self.T.forward(MOVE)
    def down(self):
        self.T.backward(MOVE)
    def left(self):
        self.x=self.T.xcor()
        self.x=self.x-MOVE
        self.T.goto(self.x,self.T.ycor())
    def right(self):
        self.x=self.T.xcor()
        self.x=self.x+MOVE
        self.T.goto(self.x,self.T.ycor())
    def gto(self):
        self.T.goto(0,-290)
        S.increase_score()


#class level():


s=Screen()
S=Score_board()
s.tracer(0)
s.setup(width=600,height=600)
t=tur()
c = car()
s.listen()
s.onkey(t.up,"Up")
s.onkey(t.up,"a")
s.onkey(t.down,"Down")
s.onkey(t.left,"Left")
s.onkey(t.right,"Right")
A=True
while A:
    time.sleep(0.1)
    s.update()
    c.creation()
    c.move()
    if t.T.ycor()>=300:
        t.gto()
        c.level()
    for i in c.a:

        if i.distance(t.T)<26:
            S.game_over()
            A=False


s.exitonclick()