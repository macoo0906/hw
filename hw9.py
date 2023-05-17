class Point :
    def __init__(self, x = 0, y = 0) :
        self.x = x
        self.y = y
    
class Rectangle :
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0) :
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)

    def show(self) :
        print(f'좌측 상단 꼭지점이 ({self.lt.x},{self.lt.y})이고 우측 상단 꼭지점이 ({self.rb.x},{self.rb.y})인 사각형입니다.', end = '')

    def getWidth(self) :
        w = self.rb.x - self.lt.x
        return w

    def getHeight(self) :
        h = self.rb.y - self.lt.y
        return h

    def getArea(self) :
        w = r1.getWidth()
        h = r1.getHeight()
        a = w * h
        return a

    def getPerimeter(self) :
        w = r1.getWidth()
        h = r1.getHeight()
        p = (w + h) * 2
        return p

r1 = Rectangle(5, 5, 20, 10)
a= r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')