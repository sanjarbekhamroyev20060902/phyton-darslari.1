class car:
    brand = 'GM'

    def ___init__(self, year, price, color):
        self.year = year
        self.price = price
        self.color = color

        def str (self):
            return f"(self.year) - yilgi mashina"
        
        def __repr__(self):
            return f"Car(year=(self.year), price = {self.prise})"
        
obj1 = car(year=2020, price=10000, color='oq')
obj2 = car(year=2021, price=15000, color='qora')
obj3 = car(year=2019, price=9000, color='qizil')
list()
print(repr(obj1)) 
print(repr(obj1))
print(obj2.year)
print(obj2.color)
print(obj2.price)


