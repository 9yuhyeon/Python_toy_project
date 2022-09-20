from random import choice
import time

list = ['가위', '바위', '보']
cpu = choice(list)
user_count = 0
cpu_count = 0
print('게임을 시작합니다.\n3 게임 중 2 게임을 이겨야만 게임이 종료됩니다.')

while True:
    user_input = input('\n가위, 바위, 보 중 하나를 입력해주세요! : ')      
    
    if user_input in list:
        print(f'\n당신은 {user_input}를 냈습니다.')    
    else:
        print('입력값을 정확히 입력해주세요!')
        break
    
    print('\n3초 후 결과를 공개합니다!')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    
    print(F'상대는 {cpu}를 냈습니다.')        
    
    # 비기는 경우
    if user_input == cpu:
        print('결과 : 비겼습니다!')
        print(f'현재 스코어 {user_count} : {cpu_count}')
    
    # 유저가 이길 경우    
    elif user_input == '가위' and cpu == '보':
        user_count += 1
        print('결과 : 이겼습니다!')
        print(f'현재 스코어 {user_count} : {cpu_count}')
        
        
    elif user_input == '바위' and cpu == '가위':
        print('결과 : 이겼습니다!')
        print(f'현재 스코어 {user_count} : {cpu_count}')
        user_count += 1
        
    elif user_input == '보' and cpu == '바위':
        print('결과 : 이겼습니다!')
        print(f'현재 스코어 {user_count} : {cpu_count}')
        user_count += 1             
    
    # 유저가 질 경우
    elif cpu == '가위' and user_input == '보':
        print('결과 : 졌습니다!')
        print(f'현재 스코어 {user_count} : {cpu_count}')
        cpu_count += 1
    elif cpu == '바위' and user_input == '가위':
        print('결과 : 졌습니다!')
        print(f'현재 스코어 {user_count} : {cpu_count}')
        cpu_count += 1
    elif cpu == '보' and user_input == '바위':
        print('결과 : 졌습니다!')
        print(f'현재 스코어 {user_count} : {cpu_count}')
        cpu_count += 1
    # 플레이어와 cpu중 2판을 먼저 이기면 종료
    if user_count == 2:
        print('플레이어가 이겼습니다!')
        break
    elif cpu_count == 2:
        print('cpu가 이겼습니다.')
        break












