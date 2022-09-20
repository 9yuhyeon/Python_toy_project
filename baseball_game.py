from datetime import datetime
import random
import time

def Base_ball_game():
    count_input = int(input('몇 자리로 게임을 진행할지 입력해주세요! : '))
    if count_input < 1:
        print('최소 1자리 이상 최대 10자리 이하의 숫자만 입력이 가능합니다.')
        return
    
    random_numbers = set()
    while len(random_numbers) < count_input:
        random_numbers.add(random.randint(0,9))
    
    random_numbers = list(random_numbers)
    random.shuffle(random_numbers)

    start_time = time.time()
    
    try_count = 0
    while True:
        user_input = input('정답을 입력해주세요! (종료 : exit) : ')
        if user_input == 'exit':
            return
        
        try_count += 1
        
        out_count = 0
        ball_count = 0
        strike_count = 0
        
        for i,v in enumerate(user_input):
            v = int(v)
            
            if v not in random_numbers: # 유저가 입력한 값이 랜덤 숫자에 없으면 아웃
                out_count += 1
            
            else:
                if random_numbers[i] == v:
                    strike_count += 1
                else:
                    ball_count += 1
        print(f'{ball_count}볼 {strike_count}스트라이크 {out_count}아웃')
        
        if strike_count == count_input:
            print('################################')
            print('정답입니다!!!')
            print(f'도전 횟수 : {try_count}')
            print(f'소요시간 : {time.time() - start_time}')
            print(f'정답을 맞춘 날짜와 시간 {datetime.now()}')
            print('################################')

Base_ball_game()
