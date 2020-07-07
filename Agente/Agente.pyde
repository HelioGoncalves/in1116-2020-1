from Vehicle import Vehicle
from Comida import Comida
import random as rand

def setup():
    global v, c, cont,d
    size(640, 360)
    vel = PVector(0,-2)
    v = Vehicle(width / 2, height / 2)
    x = rand.uniform(0,640)
    y = rand.uniform(0,360)
    c = Comida(x, y)
    cont = 0
    d=1              
    
    
def display(num):
    textSize(32)
    text(str(num), 10, 30)
    fill(0, 102, 153)
    
def draw():
    background(255)    
    eixo = PVector(c.x,c.y)
    
    # Quadrado na tela
    stroke(1)
    noFill()
    rectMode(CENTER)
    rect(width / 2, height / 2, width - d * 2, height - d * 2)
    
    c.display()
    v.update()
    v.display()
    v.arrive(eixo)  
    
    
    #verifica se ocorreu a colisão e caso tenha ocorrido gera uma nova comida e atualiza o contador
    if(round(c.x,0) == round(v.position[0],0) and round(c.y,0) == round(v.position[1],0)):
        c.newFood()   
        c.captured = c.captured + 1
        #print(c.captured)
    
    display(c.captured) # imprime na tela a quantidade de comida capiturada
    #print(round(c.x,0),v.position[0],round(c.y,0),v.position[1])
    
    
    

    

    

   
    
    
