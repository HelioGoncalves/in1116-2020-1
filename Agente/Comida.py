class Comida():

    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.raio = 3
        self.captured = 0
    
    # Design da comida        
    def display(self):
        #noStroke()
        stroke(50)
        fill(50)
        ellipse(self.x,self.y,self.raio*2,self.raio*2)
    
    # Gera novos vetores de comida        
    def newFood(self):
        self.x = random(width)
        self.y = random(height)
        
        
