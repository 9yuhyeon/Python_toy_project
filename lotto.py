import random
from pprint import pprint

def get_lotto_number(count):

    result = []
    if count < 1:
        print('1 이상의 값을 입력해주세요.')
        return
    for _ in range(count):
        set_number = set()
        
        while len(set_number) < 7:
            set_number.add(random.randint(1,45))
        
        result.append(set_number)
    return result

count = int(input('로또 번호 추첨기 입니다.\n\n원하는 매수를 입력하세요! : '))
lotto_numbers = get_lotto_number(count)
pprint(lotto_numbers)