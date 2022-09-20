def get_grade(score):
    
    if score > 90:
        print('A')
    elif score > 80:
        print('B')
    elif score > 70:
        print('C')
    else:
        print('F')        

score = int(input())
grade = get_grade(score)
print(grade)