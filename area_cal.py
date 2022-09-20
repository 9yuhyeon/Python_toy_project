PIE = 3.14
class Area():
    def __init__(self, width, vertical):
        self.width = width
        self.vertical = vertical
    def square(self):     # 가로 * 세로
        result = self.width * self.vertical
        return result
    def triangle(self):  #  가로 * 세로 / 2
        result = self.width * self.vertical / 2
        return result
    def circle(self):  # 반지름 * 반지름 * 원주율
        result = (self.width / 2) ** 2 * PIE
        return result

# 호출
area = Area(10,20)


print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이