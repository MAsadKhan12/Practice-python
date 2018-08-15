class circle(object):
    
    
    def __init__(self,radius,a,b):
       self.radius=radius
       self.a=a
       self.b=b

    def display(self):
        print(self.radius,self.a)


a=circle(3,4,6)
a.display()


