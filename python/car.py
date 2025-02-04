class Car:
    def __init__(self,model,color,year,is_available):
        self.model = model
        self.color = color
        self.year = year
        self.is_available = is_available
    
    def drive(self):
        print(f"driving {self.color} color {self.model} car")