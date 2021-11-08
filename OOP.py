#practicing class and object
# class Flower:
#     print("Flower")
#
# #object instantiation
# flower =  Flower()
# print(flower)

#using constructors
class Mathematics:
    first = 0
    second = 0
    answer = 0
    #default constructor
    def __init__(self,f,s):
        self.first =f
        self.second = s

    def display(self):
        print("First number is " + str(self.first))
        print("Second number is " +  str(self.second))
        print("Sum of " + str(self.first) + " "+ "and" + " "+ str(self.second) +  " " + " " +"is" + " " + str(self.answer))

    def calculate_sum(self):
        self.answer = self.first + self.second


obj = Mathematics(10,20)
obj.calculate_sum()
obj.display()