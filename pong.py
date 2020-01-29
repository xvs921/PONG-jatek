import turtle
#ablak
ablak=turtle.Screen()
ablak.setup(width=800,height=600)
ablak.bgcolor("black")
ablak.title("PONG")
ablak.tracer(0)
#bal ütő
bal_uto=turtle.Turtle()
bal_uto.speed(0)
bal_uto.shape("square")
bal_uto.shapesize(stretch_wid=5,stretch_len=1)
bal_uto.color("blue")
bal_uto.penup()
bal_uto.goto(-350,0)
#jobb uto
jobb_uto=turtle.Turtle()
jobb_uto.speed(0)
jobb_uto=turtle.Turtle()
jobb_uto.shape("square")
jobb_uto.shapesize(stretch_wid=5,stretch_len=1)
jobb_uto.color("red")
jobb_uto.penup()
jobb_uto.goto(350,0)
#labda
labda=turtle.Turtle()
labda.speed(1)
labda.shape("circle")
labda.color("yellow")
labda.penup()
labda.goto(0,0)
labda.változásX=1
labda.változásY=-1


#pontszám
jobb_pontszám=0
bal_pontszám=0
pontszám=turtle.Turtle()
pontszám.speed(0)
pontszám.color("white")
pontszám.penup()
pontszám.hideturtle()
pontszám.goto(0,260)
pontszám.write(f"Jobb játékos: {jobb_pontszám} - Bal játékos: {bal_pontszám}", align="center", font=("Curier",24,"normal"))



def bal_uto_fel():
    y=bal_uto.ycor()
    y+=30
    bal_uto.sety(y)

def bal_uto_le():
    y=bal_uto.ycor()
    y-=30
    bal_uto.sety(y)

def jobb_uto_fel():
    y=jobb_uto.ycor()
    y+=60
    jobb_uto.sety(y)

def jobb_uto_le():
    y=jobb_uto.ycor()
    y-=60
    jobb_uto.sety(y)


ablak.onkey(bal_uto_fel, "w")
ablak.onkey(bal_uto_le, "s")

ablak.onkey(jobb_uto_fel, "Up")
ablak.onkey(jobb_uto_le, "Down")

ablak.listen()


while True:
    # a képernyő frissítése
    ablak.update()

    labda.setx(labda.xcor()+labda.változásX)
    labda.sety(labda.ycor()+labda.változásY)

    #tetejéről pattanjon vissza
    if labda.ycor()>288:
        labda.sety(288)
        labda.változásY*=-1

    #aljáról pattanjon vissza
    if labda.ycor()<-288:
        labda.sety(-288)
        labda.változásY*=-1

    #jobb oldal érintése
    if labda.xcor()>388:
        labda.goto(0,0)
        labda.változásX*=-1
        bal_pontszám+=1
        pontszám.clear()
        pontszám.write(f"Jobb játékos: {jobb_pontszám} - Bal játékos: {bal_pontszám}", align="center", font=("Curier",24,"normal"))


    #bal oldal érintése
    if labda.xcor()<-388:
        labda.goto(0,0)
        labda.változásX*=-1
        jobb_pontszám+=1
        pontszám.clear()
        pontszám.write(f"Jobb játékos: {jobb_pontszám} - Bal játékos: {bal_pontszám}", align="center", font=("Curier",24,"normal"))

    #jobb oldali ütőről visszapattan
    if jobb_uto.xcor()-20 < labda.xcor() < jobb_uto.xcor() and jobb_uto.ycor()-40 < labda.ycor() < jobb_uto.ycor()+40:
        labda.setx(jobb_uto.xcor()-20)
        labda.változásX*=-1

    #bal oldali ütőről visszapattan
    if bal_uto.xcor()+20 > labda.xcor() > bal_uto.xcor() and bal_uto.ycor()-40 < labda.ycor() < bal_uto.ycor()+40:
        labda.setx(bal_uto.xcor()+20)
        labda.változásX*=-1