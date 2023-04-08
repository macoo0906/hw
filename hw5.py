def read_single_digit(a) :
    if a == '1' :
     print ('일')
    elif a == '2' :
     print ('이')
    elif a == '3' :
     print ('삼')
    elif a == '4' :
     print ('사')
    elif a == '5' :
     print ('오')
    elif a == '6' : 
     print ('육')
    elif a == '7' :
     print ('칠')
    elif a == '8' :
     print ('팔')
    elif a == '9' :
     print ('구')

def read_number(a) : 
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    if a1 == '1' :
     print ('일',end=' ')
    elif a1 == '2' :
     print ('이',end=' ')
    elif a1 == '3' :
     print ('삼',end=' ')
    elif a1 == '4' :
     print ('사',end=' ')
    elif a1 == '5' :
     print ('오',end=' ')
    elif a1 == '6' : 
     print ('육',end=' ')
    elif a1 == '7' :
     print ('칠',end=' ')
    elif a1 == '8' :
     print ('팔',end=' ')
    elif a1 == '9' :
     print ('구',end=' ')

    if a2 == '1' :
     print ('일',end=' ')
    elif a2 == '2' :
     print ('이',end=' ')
    elif a2 == '3' :
     print ('삼',end=' ')
    elif a2 == '4' :
     print ('사',end=' ')
    elif a2 == '5' :
     print ('오',end=' ')
    elif a2 == '6' : 
     print ('육',end=' ')
    elif a2 == '7' :
     print ('칠',end=' ')
    elif a2 == '8' :
     print ('팔',end=' ')
    elif a2 == '9' :
     print ('구',end=' ')
    
    if a3 == '1' :
     print ('일',end=' ')
    elif a3 == '2' :
     print ('이',end=' ')
    elif a3 == '3' :
     print ('삼',end=' ')
    elif a3 == '4' :
     print ('사',end=' ')
    elif a3 == '5' :
     print ('오',end=' ')
    elif a3 == '6' : 
     print ('육',end=' ')
    elif a3 == '7' :
     print ('칠',end=' ')
    elif a3 == '8' :
     print ('팔',end=' ')
    elif a3 == '9' :
     print ('구',end=' ')

integer = int(input('세 자리 정수 입력: '))
if 0 < integer < 10 :
    read_single_digit(str(integer))
else : 
    read_number(str(integer)) 