class  Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        #The First value to iterate is the length, followed by the width
        yield {'length' : self.length}
        yield {'width' : self.width}

# Example usage:
rectanglee = Rectangle(5,3)

# Iterating over the instance
for attribute in rectanglee:
    print(attribute)