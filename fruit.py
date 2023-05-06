class Fruits:
    bank_name = "Equity"
    def __init__(self,color,taste,price,name):
        self.color = color
        self.taste = taste
        self.price = price
        self.name = name
        
    def flavour(self):
        return f"A {self.name} is {self.taste}"
    
    def market_sales(self):
        return f"The market sells {self.name} at {self.price}"
    
    def description(self):
        return f"{self.name} is {self.color} and it tastes {self.taste}"
    
    
    
    
    

    
    
    
 