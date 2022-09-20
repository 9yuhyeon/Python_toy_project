import a

print("프로그램을 실행하여 num1, num2 값을 입력 후 operator 값을 입력하면 결과가 출력됩니다.")

def Calculator():
    num1, num2 = map(int, input().split())
    operator = input()

    if operator == '+':
        result = a.plus(num1, num2)
        print(result)
    elif operator == '-':
        result = a.minus(num1, num2)
        print(result)
    elif operator == '*':
        result = a.multiply(num1, num2)
        print(result)
    elif operator == '/':
        result = a.division(num1, num2)
        print(result)

Calculator()


