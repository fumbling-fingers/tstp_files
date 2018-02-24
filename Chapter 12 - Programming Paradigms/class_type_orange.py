
class Orange:
    def __init__(self, w, c):
        """weight is measured in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("object of Orange class created!")

    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)
