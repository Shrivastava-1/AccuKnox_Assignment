class  Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
    def __iter__(self):
        yield {'length' : self.length}
        yield {'width' : self.width}

cust_rent = Rectangle(5,3)

for attribute in cust_rent:
    print(attribute)
