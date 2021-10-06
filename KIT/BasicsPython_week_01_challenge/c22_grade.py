def grade(score):
    if 90<=score<=100:
        print('A')
    elif 80<=score<90:
        print('B')
    elif 70<=score<80:
        print('C')
    elif 60<=score<70:
        print('D')
    else:
        print('F')


grade(100)
grade(91)
grade(89)
grade(80)
grade(75)
grade(66)
grade(59)
grade(1)
res1=grade(100)
print(res1)
print(type(res1))
