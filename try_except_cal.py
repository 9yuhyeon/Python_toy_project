class Calc():
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def plus(self):
        return self.num1 + self.num2
    def minus(self):
        return self.num1 - self.num2
    def multiple(self):
        return self.num1 * self.num2
    def div(self): 
        try:
            return self.num1 // self.num2
        except ZeroDivisionError: # 0으로 나누면서 에러가 발생했을 때
            print("0으로는 나눌수 없습니다.")
while True:
    try:
        num1,num2 = [int(x) for x in input().split(" ")]
        break
    except:
        print("숫자만 입력이 가능합니다.")


calc = Calc()
calc.set_number(num1,num2)
print(calc.plus())      # 더한 값
print(calc.minus())     # 뺀 값
print(calc.multiple())  # 곱한 값
print(calc.div())       # 나눈 값