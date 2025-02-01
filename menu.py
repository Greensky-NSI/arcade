from p5 import *

def setup() :
    global img
    size(800,600)
    img = load_image('bomb-it.jpg')
    background(250)
    

def draw() :
    tint(150)
    image(img,0,0,800,600)
    fill(23,240,78)
    text_align(CENTER)
    stroke(0)
    stroke_weight(2)
    text("JOUER",400,300)
    fill(45,250,102,50)
    stroke(45,250,45)
    stroke_weight(5)
    rect(350,285,100,50)



run()
