count = 0

while count < 5:
    user_input = input()   
    
    if user_input == 'exit': 
        break

    if user_input.isdigit():
        print(int(user_input)*2)
        count += 1
    elif user_input.isalpha():
        print(f'입력한 문자는 {user_input} 입니다.')
